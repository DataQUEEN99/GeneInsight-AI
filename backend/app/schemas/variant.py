"""Variant Schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class VariantCreate(BaseModel):
    gene: str
    hgvs_notation: str
    chromosome: Optional[str] = None
    position: Optional[str] = None
    ref: Optional[str] = None
    alt: Optional[str] = None
    variant_type: Optional[str] = None


class VariantResponse(BaseModel):
    id: str
    gene: str
    hgvs_notation: str
    protein_change: Optional[str]
    clinical_significance: Optional[str]
    pathogenicity_score: Optional[float]
    ai_interpretation: Optional[str]
    acmg_classification: Optional[str]
    diseases: List[str]
    evidence_codes: List[str]
    created_at: datetime

    class Config:
        from_attributes = True


class VariantAnalysisCreate(BaseModel):
    name: str
    description: Optional[str] = None
    file_type: str


class VariantAnalysisResponse(BaseModel):
    id: str
    user_id: str
    name: str
    status: str
    total_variants: int
    processed_variants: int
    created_at: datetime

    class Config:
        from_attributes = True
