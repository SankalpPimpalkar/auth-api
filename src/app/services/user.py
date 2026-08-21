from ..models.user import User
from sqlmodel import Session, select
from fastapi import Depends
from database import get_session

def get_user(session: Session = Depends(get_session), id: str = "") -> User | None:
    user = session.exec(select(User).where(User.id == id)).first()
    return user