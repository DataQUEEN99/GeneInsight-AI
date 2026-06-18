"""User Model"""

from sqlalchemy import Column, String, Boolean, Index
from .base import BaseModel


class User(BaseModel):
    """User Model"""

    __tablename__ = "users"

    email = Column(String(255), unique=True, nullable=False, index=True)
    full_name = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email})>"
