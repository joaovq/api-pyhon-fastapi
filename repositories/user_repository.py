from sqlalchemy.orm import Session

from models.user import User


def get_users(db: Session):
    return db.query(User).all()

def login(db: Session, username: str, password: str):
    return db.query(User).filter(username=username, password=password).first()