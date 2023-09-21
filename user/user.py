from datetime import timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.auth.app_security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_active_user
from database import get_db
from models.user import User
from repositories import user_repository
from sqlalchemy.orm import Session
from schemas import user

router = APIRouter()

# Login for multipart form


@router.post("/login/", response_model=user.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = user_repository.login(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


# TODO Get real items in db and modify for sales

@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return [{"item_id": "Foo", "owner": current_user.username}]


@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    return user_repository.register_user(db, user)
