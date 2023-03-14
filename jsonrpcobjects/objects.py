"""JSON-RPC 2.0 spec objects."""
from typing import Any, Optional, Union

from pydantic import BaseModel, StrictInt, StrictStr

__all__ = (
    "ErrorType",
    "NotificationType",
    "RequestType",
    "ResponseType",
    "ErrorObject",
    "ErrorObjectData",
    "ErrorResponseObject",
    "NotificationObject",
    "NotificationObjectParams",
    "RequestObject",
    "RequestObjectParams",
    "ResultResponseObject",
)

ErrorType = Union["ErrorObjectData", "ErrorObject"]
NotificationType = Union["NotificationObject", "NotificationObjectParams"]
RequestType = Union["RequestObjectParams", "RequestObject"]
ResponseType = Union["ErrorResponseObject", "ResultResponseObject"]


class RequestObjectParams(BaseModel):
    """JSON-RPC 2.0 request object with parameters."""

    id: Union[StrictInt, StrictStr]
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class RequestObject(BaseModel):
    """JSON-RPC 2.0 request object."""

    id: Union[StrictInt, StrictStr]
    method: str
    jsonrpc: str = "2.0"


class NotificationObjectParams(BaseModel):
    """JSON-RPC 2.0 notification object with parameters."""

    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class NotificationObject(BaseModel):
    """JSON-RPC 2.0 notification object."""

    method: str
    jsonrpc: str = "2.0"


class ErrorObjectData(BaseModel):
    """JSON-RPC 2.0 error object with data."""

    code: int
    message: str
    data: Any


class ErrorObject(BaseModel):
    """JSON-RPC 2.0 error object."""

    code: int
    message: str


class ErrorResponseObject(BaseModel):
    """JSON-RPC 2.0 error response object."""

    id: Optional[Union[StrictInt, StrictStr]]
    error: ErrorType
    jsonrpc: str = "2.0"


class ResultResponseObject(BaseModel):
    """JSON-RPC 2.0 result response object."""

    id: Union[StrictInt, StrictStr]
    result: Any
    jsonrpc: str = "2.0"
