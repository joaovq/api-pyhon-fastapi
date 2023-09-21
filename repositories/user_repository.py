from sqlalchemy.orm import Session
from core.auth.app_security import get_password_hash, verify_password
from models.user import User
from schemas import user as sa

def get_users(db: Session):
    return db.query(User).all()

# Private method two dunders
def __authenticate_user(user_in_db: User, password: str):
    if not user_in_db:
        return False
    if not verify_password(password, user_in_db.password):
        return False
    return user_in_db

def login(db: Session, username: str, password: str):
    user_in_db = db.query(User).filter(User.username==username).first()
    is_authenticated = __authenticate_user(user_in_db=user_in_db, password=password)
    if not is_authenticated: 
        user_in_db = None
    return user_in_db

def register_user(db: Session, user: sa.UserCreate):
    new_user = User(username= user.username, email=user.email, name=user.name, password=user.password)
    hashed_pw = get_password_hash(new_user.password)
    new_user.password = hashed_pw
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user