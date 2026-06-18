"""Report Schemas"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ReportGenerateRequest(BaseModel):
    variant_ids: List[str]
    format: str
    include_sections: List[str]


class ReportResponse(BaseModel):
    report_id: str
    download_url: str
    format: str
    size_bytes: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True
