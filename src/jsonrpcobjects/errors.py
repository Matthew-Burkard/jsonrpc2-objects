from typing import Type, Optional

from pydantic import BaseModel

from jsonrpcobjects.objects import ErrorObjectData, ErrorType

__all__ = (
    'PARSE_ERROR',
    'INVALID_REQUEST',
    'METHOD_NOT_FOUND',
    'INVALID_PARAMS',
    'INTERNAL_ERROR',
    'JSONRPCError',
    'ParseError',
    'InvalidRequest',
    'MethodNotFound',
    'InvalidParams',
    'InternalError',
    'ServerError',
    'get_exception_by_code',
)


class _ErrorData(BaseModel):
    code: int
    message: str


PARSE_ERROR = _ErrorData(code=-32700, message='Parse error')
INVALID_REQUEST = _ErrorData(code=-32600, message='Invalid Request')
METHOD_NOT_FOUND = _ErrorData(code=-32601, message='Method not found')
INVALID_PARAMS = _ErrorData(code=-32602, message='Invalid params')
INTERNAL_ERROR = _ErrorData(code=-32603, message='Internal error')


class JSONRPCError(Exception):
    def __init__(self, *args) -> None:
        super(JSONRPCError, self).__init__(*args)


class ParseError(JSONRPCError):
    def __init__(self) -> None:
        error = PARSE_ERROR
        super(ParseError, self).__init__(
            f'JSON-RPC Error: {error.code}: {error.message}',
        )


class InvalidRequest(JSONRPCError):
    def __init__(self) -> None:
        error = INVALID_REQUEST
        super(InvalidRequest, self).__init__(
            f'JSON-RPC Error: {error.code}: {error.message}',
        )


class MethodNotFound(JSONRPCError):
    def __init__(self) -> None:
        error = METHOD_NOT_FOUND
        super(MethodNotFound, self).__init__(
            f'JSON-RPC Error: {error.code}: {error.message}',
        )


class InvalidParams(JSONRPCError):
    def __init__(self) -> None:
        error = INVALID_PARAMS
        super(InvalidParams, self).__init__(
            f'JSON-RPC Error: {error.code}: {error.message}',
        )


class InternalError(JSONRPCError):
    def __init__(self) -> None:
        error = INTERNAL_ERROR
        super(InternalError, self).__init__(
            f'JSON-RPC Error: {error.code}: {error.message}',
        )


class ServerError(JSONRPCError):
    def __init__(self, error: ErrorType) -> None:
        msg = f'{error.code}: {error.message}'
        if isinstance(error, ErrorObjectData):
            msg += f'\nError Data: {error.data}'
        super(ServerError, self).__init__(msg)


def get_exception_by_code(code: int) -> Optional[Type]:
    return {
        -32700: ParseError,
        -32600: InvalidRequest,
        -32601: MethodNotFound,
        -32602: InvalidParams,
        -32603: InternalError,
    }.get(code)
