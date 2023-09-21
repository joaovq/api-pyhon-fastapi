from dataclasses import dataclass

@dataclass
class Token:
    access_token: str
    token_type: str

@dataclass
class TokenData:
    username: str | None = None

@dataclass
class User:
    username: str
    email: str | None = None

class UserInDB(User):
    hashed_password: str
    
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)