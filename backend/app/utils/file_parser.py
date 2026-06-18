"""CSV/TSV File Parser"""

import csv
import pandas as pd
from typing import List, Dict, Any
from io import StringIO, BytesIO
from app.core.exceptions import ValidationException


def parse_csv_file(file_content: str, delimiter: str = ",") -> List[Dict[str, Any]]:
    try:
        reader = csv.DictReader(StringIO(file_content), delimiter=delimiter)
        rows = list(reader)
        return rows
    except Exception as e:
        raise ValidationException(f"Failed to parse CSV file: {str(e)}")


def parse_tsv_file(file_content: str) -> List[Dict[str, Any]]:
    return parse_csv_file(file_content, delimiter="\t")


def parse_excel_file(file_bytes: bytes) -> List[Dict[str, Any]]:
    try:
        df = pd.read_excel(BytesIO(file_bytes))
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValidationException(f"Failed to parse Excel file: {str(e)}")
