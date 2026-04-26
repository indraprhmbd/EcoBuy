import enum

from sqlalchemy import Column, DateTime, Enum, Integer
from sqlalchemy.sql import func

from app.db.database import Base


class UserRole(str, enum.Enum):
    farmer = "farmer"
    processor = "processor"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
