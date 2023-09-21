from sqlalchemy import Column,Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'person_1'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True, default='')
    sales = relationship('Sale', back_populates='person')