import uuid, hashlib, datetime
from typing import List


from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, Text, UUID
from sqlalchemy.orm import relationship, Mapped

from Postgresql import BaseModel

class Users(BaseModel):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = Column(String(255), unique=True, nullable=False)
    password: Mapped[str] = Column(String(255), nullable=False)
    telephone: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), nullable=False)
    is_superuser: Mapped[bool] = Column(Boolean, default=False)
    
    