from dataclasses import dataclass
from typing import Union

@dataclass()
class Token:
    access_token: str
    token_type: str

@dataclass()
class TokenData:
    username: Union[str,None] = None

@dataclass()
class User:
    username: str
    email: Union[str,None] = None
    
@dataclass
class UserCreate(User):
    name: str = ""
    password: str = ""

class UserInDB(User):
    password: str
    
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)