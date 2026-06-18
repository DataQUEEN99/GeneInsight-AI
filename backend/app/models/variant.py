"""Variant and VariantAnalysis Models"""

from sqlalchemy import Column, String, Float, Text, ForeignKey, Index, JSON, Integer
from .base import BaseModel


class Variant(BaseModel):
    """Genomic Variant Model"""

    __tablename__ = "variants"

    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    analysis_id = Column(String(36), ForeignKey("variant_analyses.id"), nullable=True)
    
    gene = Column(String(50), nullable=False, index=True)
    hgvs_notation = Column(String(255), unique=True, nullable=False)
    chromosome = Column(String(5))
    position = Column(String(20))
    ref = Column(String(255))
    alt = Column(String(255))
    
    protein_change = Column(String(255))
    variant_type = Column(String(50))
    
    clinical_significance = Column(String(50))
    pathogenicity_score = Column(Float)
    
    ai_interpretation = Column(Text)
    acmg_classification = Column(String(50))
    acmg_confidence = Column(Float)
    
    diseases = Column(JSON, default=list)
    evidence_codes = Column(JSON, default=list)
    citations = Column(JSON, default=list)


class VariantAnalysis(BaseModel):
    """Variant Analysis Batch Model"""

    __tablename__ = "variant_analyses"

    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    
    name = Column(String(255), nullable=False)
    description = Column(Text)
    file_name = Column(String(255))
    file_type = Column(String(10))
    
    status = Column(String(50), default="pending")
    total_variants = Column(Integer, default=0)
    processed_variants = Column(Integer, default=0)
    
    parameters = Column(JSON, default=dict)
    results = Column(JSON, default=dict)
    error_message = Column(Text)
