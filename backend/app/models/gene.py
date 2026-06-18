"""Gene Model"""

from sqlalchemy import Column, String, Text, JSON
from .base import BaseModel


class Gene(BaseModel):
    """Gene Model"""

    __tablename__ = "genes"

    symbol = Column(String(50), unique=True, nullable=False, index=True)
    entrez_id = Column(String(20), unique=True, nullable=False)
    ensembl_id = Column(String(50))
    chromosome = Column(String(5))
    start_position = Column(String(20))
    end_position = Column(String(20))
    
    gene_name = Column(String(255))
    gene_description = Column(Text)
    gene_type = Column(String(50))
    
    function = Column(Text)
    associated_diseases = Column(JSON, default=list)
    pathways = Column(JSON, default=list)
    omim_id = Column(String(50))
