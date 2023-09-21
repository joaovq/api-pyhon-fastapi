from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class SalesCreate:
    value: float 
