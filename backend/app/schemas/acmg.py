"""ACMG Classification Schemas"""

from pydantic import BaseModel
from typing import Optional, Dict, List


class ACMGRequest(BaseModel):
    hgvs_notation: str
    gene: str
    phenotype: Optional[str] = None
    inheritance: Optional[str] = None


class ACMGResponse(BaseModel):
    classification: str
    confidence: float
    evidence_codes: List[str]
    reasoning: Dict[str, str]
    clinical_explanation: str
