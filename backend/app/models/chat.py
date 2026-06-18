"""Chat Message Model"""

from sqlalchemy import Column, String, Text, ForeignKey, JSON
from .base import BaseModel


class ChatMessage(BaseModel):
    """Chat Message Model"""

    __tablename__ = "chat_messages"

    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    
    context = Column(JSON, default=dict)
    citations = Column(JSON, default=list)
    
    is_helpful = Column(String(36))
    feedback_text = Column(Text)
