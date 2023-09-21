from database import Base
from sqlalchemy import schema as sm, types


class User(Base):
    __tablename__ = 'users'
    id = sm.Column(types.Integer, primary_key=True)
    name = sm.Column(types.String)
    username = sm.Column(types.String, unique=True)
    password = sm.Column(types.String)
    email = sm.Column(types.String, unique=True)
    is_active = sm.Column(types.Boolean, default=True)