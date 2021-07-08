from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from . import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    active = Column(Boolean, default=True)