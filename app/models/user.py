from app.db.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="technician")
    

    queries = relationship("Query", back_populates="user")