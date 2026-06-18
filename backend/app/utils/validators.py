"""Data Validators"""

import re
from typing import List
from app.core.exceptions import ValidationException


def validate_hgvs_notation(hgvs: str) -> bool:
    pattern = r"^(NM_|chr).*:[cg]\.[0-9]+[ATCG]>[ATCG]$"
    return bool(re.match(pattern, hgvs))


def validate_gene_symbol(gene: str) -> bool:
    return bool(re.match(r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)?$", gene))


def validate_file_extension(filename: str, allowed: List[str]) -> bool:
    extension = filename.split(".")[-1].lower()
    return extension in [ext.lower() for ext in allowed]


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))
