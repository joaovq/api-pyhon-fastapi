from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonCreate:
    name:str
    age: int
    email:str