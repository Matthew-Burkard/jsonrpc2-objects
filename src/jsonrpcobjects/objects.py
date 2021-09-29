from typing import Any, Optional, Union

from pydantic import BaseModel

ErrorType = Union["ErrorObjectData", "ErrorObject"]
NotificationType = Union["NotificationObject", "NotificationObjectParams"]
RequestType = Union["RequestObjectParams", "RequestObject"]
ResponseType = Union["ErrorResponseObject", "ResultResponseObject"]


class RequestObjectParams(BaseModel):
    id: Union[str, int]
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class RequestObject(BaseModel):
    id: Union[str, int]
    method: str
    jsonrpc: str = "2.0"


class NotificationObject(BaseModel):
    method: str
    jsonrpc: str = "2.0"


class NotificationObjectParams(BaseModel):
    method: str
    params: Union[list, dict]
    jsonrpc: str = "2.0"


class ErrorObjectData(BaseModel):
    code: int
    message: str
    data: Any


class ErrorObject(BaseModel):
    code: int
    message: str


class ErrorResponseObject(BaseModel):
    id: Optional[Union[str, int]]
    error: ErrorType
    jsonrpc: str = "2.0"


class ResultResponseObject(BaseModel):
    id: Union[str, int]
    result: Any
    jsonrpc: str = "2.0"
