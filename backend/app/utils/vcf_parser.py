"""VCF File Parser"""

import vcf
from typing import List, Dict, Any
from io import StringIO
from app.core.exceptions import ValidationException


def parse_vcf_file(file_content: str) -> List[Dict[str, Any]]:
    try:
        reader = vcf.Reader(StringIO(file_content))
        variants = []
        
        for record in reader:
            variant = {
                "chromosome": record.CHROM,
                "position": record.POS,
                "ref": record.REF,
                "alt": str(record.ALT[0]) if record.ALT else None,
                "quality": record.QUAL,
                "filter": record.FILTER,
                "info": dict(record.INFO) if record.INFO else {},
            }
            variants.append(variant)
        
        return variants
    except Exception as e:
        raise ValidationException(f"Failed to parse VCF file: {str(e)}")


def vcf_to_hgvs(chromosome: str, position: int, ref: str, alt: str) -> str:
    return f"chr{chromosome}:g.{position}{ref}>{alt}"
