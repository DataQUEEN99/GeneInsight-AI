"""Disease Model"""

from sqlalchemy import Column, String, Text, JSON
from .base import BaseModel


class Disease(BaseModel):
    """Disease Model"""

    __tablename__ = "diseases"

    name = Column(String(255), unique=True, nullable=False, index=True)
    icd10_code = Column(String(20))
    omim_id = Column(String(50))
    mondo_id = Column(String(50))
    
    description = Column(Text)
    inheritance_pattern = Column(String(100))
    
    associated_genes = Column(JSON, default=list)
    clinical_features = Column(JSON, default=list)
