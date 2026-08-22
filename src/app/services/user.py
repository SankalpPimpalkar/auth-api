from sqlmodel import Session, select
from ..models.user import User, UpdateUser, CreateUser
from ..utils.hashing import get_password_hash
from ..utils.exceptions import UserAlreadyExistsError, UserNotFoundError

def create_user(session: Session, user_create: CreateUser) -> User:
    existing_user = session.exec(select(User).where(User.email == user_create.email)).first()
    if existing_user:
        raise UserAlreadyExistsError(f"Email {user_create.email} is taken.")

    user_data = user_create.model_dump()
    user_data.pop("password") 
    hashed_password = get_password_hash(user_create.password)

    db_user = User(**user_data, password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def update_user(session: Session, user_id: int, user_update: UpdateUser) -> User:
    db_user = session.get(User, user_id)
    if not db_user:
        raise UserNotFoundError()

    update_data = user_update.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(update_data)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_user_by_email(session: Session, email: str) -> User | None:
    db_user = session.exec(select(User).where(User.email == email)).first()
    if not db_user:
            raise UserNotFoundError()
    
    return db_user

def delete_user(session: Session, user_id: int) -> None:
    db_user = session.get(User, user_id)
    if not db_user:
        raise UserNotFoundError(f"User with ID {user_id} not found.")

    session.delete(db_user)
    session.commit()