from sqlalchemy.orm import Session
from core.auth.security import get_password_hash

from models.user import User
from schemas import user as sa

def get_users(db: Session):
    return db.query(User).all()

def login(db: Session, username: str, password: str):
    return db.query(User).filter(User.username==username, User.password==password).first()

def register_user(db: Session, user: sa.UserCreate):
    new_user = User(**user.dict())
    hashed_pw = get_password_hash(new_user.password)
    new_user.password = hashed_pw
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user