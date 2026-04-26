from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    data: Optional[T] = None
    message: str = "success"
    error: Optional[str] = None

def success_response(data: Any = None, message: str = "success") -> ApiResponse:
    return ApiResponse(data=data, message=message)

def error_response(message: str, error: str = None) -> ApiResponse:
    return ApiResponse(data=None, message=message, error=error)
