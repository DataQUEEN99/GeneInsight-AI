"""Chat Schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any


class ChatMessageCreate(BaseModel):
    message: str
    context: Optional[Dict[str, Any]] = None


class CitationSchema(BaseModel):
    doi: Optional[str] = None
    title: str
    source: str
    snippet: Optional[str] = None
    url: Optional[str] = None


class ChatMessageResponse(BaseModel):
    id: str
    message: str
    response: str
    citations: List[CitationSchema]
    created_at: datetime

    class Config:
        from_attributes = True
