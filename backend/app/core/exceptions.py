"""Custom Exception Classes"""

from fastapi import HTTPException, status
from typing import Any, Optional


class APIException(HTTPException):
    """Base API Exception"""

    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: str = "Internal server error",
        headers: Optional[dict] = None,
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class AuthenticationException(APIException):
    """Authentication Error"""

    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )


class AuthorizationException(APIException):
    """Authorization Error"""

    def __init__(self, detail: str = "Insufficient permissions"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class NotFoundException(APIException):
    """Resource Not Found Error"""

    def __init__(self, detail: str = "Resource not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class ValidationException(APIException):
    """Validation Error"""

    def __init__(self, detail: str = "Validation failed"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
        )


class ConflictException(APIException):
    """Conflict Error (e.g., duplicate entry)"""

    def __init__(self, detail: str = "Conflict with existing resource"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )
