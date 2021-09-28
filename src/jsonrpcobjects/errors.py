from typing import Optional, Type

from jsonrpcobjects.objects import ErrorObject, ErrorObjectData, ErrorType

__all__ = (
    "INTERNAL_ERROR",
    "INVALID_PARAMS",
    "INVALID_REQUEST",
    "InternalError",
    "InvalidParams",
    "InvalidRequest",
    "JSONRPCError",
    "METHOD_NOT_FOUND",
    "MethodNotFound",
    "PARSE_ERROR",
    "ParseError",
    "ServerError",
    "get_exception_by_code",
)

INVALID_REQUEST = ErrorObject(code=-32600, message="Invalid Request")
METHOD_NOT_FOUND = ErrorObject(code=-32601, message="Method not found")
INVALID_PARAMS = ErrorObject(code=-32602, message="Invalid params")
INTERNAL_ERROR = ErrorObject(code=-32603, message="Internal error")
PARSE_ERROR = ErrorObject(code=-32700, message="Parse error")


class JSONRPCError(Exception):
    def __init__(self, error: ErrorType) -> None:
        msg = f"{error.code}: {error.message}"
        if isinstance(error, ErrorObjectData):
            msg += f"\nError Data: {error.data}"
        super(JSONRPCError, self).__init__(error)


class ParseError(JSONRPCError):
    def __init__(self, error: Optional[ErrorType] = None) -> None:
        super(ParseError, self).__init__(error or PARSE_ERROR)


class InvalidRequest(JSONRPCError):
    def __init__(self, error: Optional[ErrorType] = None) -> None:
        super(InvalidRequest, self).__init__(error or INVALID_REQUEST)


class MethodNotFound(JSONRPCError):
    def __init__(self, error: Optional[ErrorType] = None) -> None:
        super(MethodNotFound, self).__init__(error or METHOD_NOT_FOUND)


class InvalidParams(JSONRPCError):
    def __init__(self, error: Optional[ErrorType] = None) -> None:
        super(InvalidParams, self).__init__(error or INVALID_PARAMS)


class InternalError(JSONRPCError):
    def __init__(self, error: Optional[ErrorType] = None) -> None:
        super(InternalError, self).__init__(error or INTERNAL_ERROR)


class ServerError(JSONRPCError):
    def __init__(self, error: ErrorType) -> None:
        super(ServerError, self).__init__(error)


def get_exception_by_code(code: int) -> Optional[Type]:
    return {
        -32600: InvalidRequest,
        -32601: MethodNotFound,
        -32602: InvalidParams,
        -32603: InternalError,
        -32700: ParseError,
    }.get(code)
