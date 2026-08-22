from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from ..database import get_session
from ..models.user import CreateUser, User
from ..models.token import Token, TokenData
from ..services import user as user_service
from ..services import token as token_service
from ..utils.exceptions import UserAlreadyExistsError
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Authentication"])

class RegisterResponse(BaseModel):
    user: User
    token: Token

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    user_create: CreateUser, 
    session: Session = Depends(get_session)
):
    try:
        db_user = user_service.create_user(session=session, user_create=user_create)
        token_payload = TokenData(email=db_user.email)
        access_token = token_service.create_accesstoken(data=token_payload)
        
        return RegisterResponse(user=db_user, token=access_token)
        
    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
        )
