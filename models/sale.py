from sqlalchemy import types, schema
from database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Sale(Base):
    __tablename__ = 'sales'
    id = schema.Column(types.Integer, primary_key=True, index=True)
    value = schema.Column(types.Double)
    created_at = schema.Column(type_=types.TIMESTAMP, server_default=func.now())
    person_id = schema.Column(types.Integer, schema.ForeignKey('person.id'))
    person = relationship('Person', back_populates='sales') 