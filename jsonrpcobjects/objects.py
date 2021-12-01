"""JSON-RPC 2.0 spec objects."""
import typing
from abc import ABC
from typing import Any, Optional, Union

from pydantic import BaseModel

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


class SafeModel(ABC):
    """A BaseModel may extend this to avoid union type coercion.

    Pydantic recklessly coerces union types, this is a hacky fix.
    """

    def __init__(self, *args, **kwargs) -> None:
        super(SafeModel, self).__init__(*args, **kwargs)
        # To get this far, validation already passed.
        for k, v in kwargs.items():
            origin = typing.get_origin(self.__annotations__.get(k))
            if origin == Union and type(self.__dict__.get(k)) != type(v):
                self.__dict__[k] = v


class RequestObjectParams(SafeModel, BaseModel):
    """JSON-RPC 2.0 request object with parameters."""

    id: Union[int, str]
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class RequestObject(SafeModel, BaseModel):
    """JSON-RPC 2.0 request object."""

    id: Union[int, str]
    method: str
    jsonrpc: str = "2.0"


class NotificationObjectParams(SafeModel, BaseModel):
    """JSON-RPC 2.0 notification object with parameters."""

    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class NotificationObject(SafeModel, BaseModel):
    """JSON-RPC 2.0 notification object."""

    method: str
    jsonrpc: str = "2.0"


class ErrorObjectData(SafeModel, BaseModel):
    """JSON-RPC 2.0 error object with data."""

    code: int
    message: str
    data: Any


class ErrorObject(SafeModel, BaseModel):
    """JSON-RPC 2.0 error object."""

    code: int
    message: str


class ErrorResponseObject(SafeModel, BaseModel):
    """JSON-RPC 2.0 error response object."""

    id: Optional[Union[int, str]]
    error: ErrorType
    jsonrpc: str = "2.0"


class ResultResponseObject(SafeModel, BaseModel):
    """JSON-RPC 2.0 result response object."""

    id: Union[int, str]
    result: Any
    jsonrpc: str = "2.0"
