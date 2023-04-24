"""JSON-RPC 2.0 spec objects."""
from typing import Any, Optional, Union

from pydantic import BaseModel, StrictInt, StrictStr

__all__ = (
    "ErrorType",
    "NotificationType",
    "RequestType",
    "ResponseType",
    "Error",
    "ErrorData",
    "ErrorResponse",
    "Notification",
    "NotificationParams",
    "Request",
    "RequestParams",
    "ResultResponse",
)

ErrorType = Union["ErrorData", "Error"]
NotificationType = Union["Notification", "NotificationParams"]
RequestType = Union["RequestParams", "Request"]
ResponseType = Union["ErrorResponse", "ResultResponse"]


class RequestParams(BaseModel):
    """JSON-RPC 2.0 request object with parameters."""

    id: Union[StrictInt, StrictStr]
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class Request(BaseModel):
    """JSON-RPC 2.0 request object."""

    id: Union[StrictInt, StrictStr]
    method: str
    jsonrpc: str = "2.0"


class NotificationParams(BaseModel):
    """JSON-RPC 2.0 notification object with parameters."""

    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class Notification(BaseModel):
    """JSON-RPC 2.0 notification object."""

    method: str
    jsonrpc: str = "2.0"


class ErrorData(BaseModel):
    """JSON-RPC 2.0 error object with data."""

    code: int
    message: str
    data: Any


class Error(BaseModel):
    """JSON-RPC 2.0 error object."""

    code: int
    message: str


class ErrorResponse(BaseModel):
    """JSON-RPC 2.0 error response object."""

    id: Optional[Union[StrictInt, StrictStr]]
    error: ErrorType
    jsonrpc: str = "2.0"


class ResultResponse(BaseModel):
    """JSON-RPC 2.0 result response object."""

    id: Union[StrictInt, StrictStr]
    result: Any
    jsonrpc: str = "2.0"
