"""JSON-RPC 2.0 spec objects."""

from __future__ import annotations

__all__ = (
    "DataError",
    "Error",
    "ErrorResponse",
    "ErrorType",
    "Notification",
    "NotificationType",
    "ParamsNotification",
    "ParamsRequest",
    "Request",
    "RequestType",
    "ResponseType",
    "ResultResponse",
)

from typing import Any, Union

from pydantic import BaseModel

ErrorType = Union["DataError", "Error"]
NotificationType = Union["Notification", "ParamsNotification"]
RequestType = Union["ParamsRequest", "Request"]
ResponseType = Union["ErrorResponse", "ResultResponse"]


class ParamsRequest(BaseModel):
    """JSON-RPC 2.0 request object with parameters."""

    id: int | str
    method: str
    params: list | dict
    jsonrpc: str = "2.0"


class Request(BaseModel):
    """JSON-RPC 2.0 request object."""

    id: int | str
    method: str
    jsonrpc: str = "2.0"


class ParamsNotification(BaseModel):
    """JSON-RPC 2.0 notification object with parameters."""

    method: str
    params: list | dict
    jsonrpc: str = "2.0"


class Notification(BaseModel):
    """JSON-RPC 2.0 notification object."""

    method: str
    jsonrpc: str = "2.0"


class DataError(BaseModel):
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

    id: int | str | None
    error: ErrorType
    jsonrpc: str = "2.0"


class ResultResponse(BaseModel):
    """JSON-RPC 2.0 result response object."""

    id: int | str
    result: Any
    jsonrpc: str = "2.0"
