"""Report Model"""

from sqlalchemy import Column, String, Text, ForeignKey, JSON
from .base import BaseModel


class Report(BaseModel):
    """Generated Report Model"""

    __tablename__ = "reports"

    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    analysis_id = Column(String(36), ForeignKey("variant_analyses.id"))
    
    name = Column(String(255), nullable=False)
    description = Column(Text)
    report_format = Column(String(20), default="pdf")
    
    variant_ids = Column(JSON, default=list)
    sections = Column(JSON, default=list)
    
    content = Column(Text)
    file_path = Column(String(500))
    file_size = Column(String(36))
    
    status = Column(String(50), default="completed")
