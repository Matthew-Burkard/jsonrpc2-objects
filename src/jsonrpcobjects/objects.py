"""JSON-RPC 2.0 spec objects."""
from typing import Any, Optional, Union

from pydantic import BaseModel

ErrorType = Union["ErrorObjectData", "ErrorObject"]
NotificationType = Union["NotificationObject", "NotificationObjectParams"]
RequestType = Union["RequestObjectParams", "RequestObject"]
ResponseType = Union["ErrorResponseObject", "ResultResponseObject"]


# noinspection PyMissingOrEmptyDocstring
class RequestObjectParams(BaseModel):
    id: Union[str, int]
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


# noinspection PyMissingOrEmptyDocstring
class RequestObject(BaseModel):
    id: Union[str, int]
    method: str
    jsonrpc: str = "2.0"


# noinspection PyMissingOrEmptyDocstring
class NotificationObject(BaseModel):
    method: str
    jsonrpc: str = "2.0"


# noinspection PyMissingOrEmptyDocstring
class NotificationObjectParams(BaseModel):
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


# noinspection PyMissingOrEmptyDocstring
class ErrorObjectData(BaseModel):
    code: int
    message: str
    data: Any


# noinspection PyMissingOrEmptyDocstring
class ErrorObject(BaseModel):
    code: int
    message: str


# noinspection PyMissingOrEmptyDocstring
class ErrorResponseObject(BaseModel):
    id: Optional[Union[str, int]]
    error: ErrorType
    jsonrpc: str = "2.0"


# noinspection PyMissingOrEmptyDocstring
class ResultResponseObject(BaseModel):
    id: Union[str, int]
    result: Any
    jsonrpc: str = "2.0"
