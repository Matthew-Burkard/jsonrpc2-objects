# JSON-RPC 2.0 Objects

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://mit-license.org/)

A collection of objects for use in JSON-RPC 2.0 implementations.

## Installation

```shell
pip install jsonrpc2-objects
```

```shell
poetry add jsonrpc2-objects
```

## Objects

Available in `objects` are the following:

| Object             | Description                 |
|--------------------|-----------------------------|
| ParamsRequest      | Request with params         |
| Request            | Request without params      |
| ParamsNotification | Notification with params    |
| Notification       | Notification without params |
| ErrorResponse      | Response with result        |
| ResultResponse     | Response with error         |

## Errors

Python exceptions are available for each JSON-RPC 2.0 error. Each error
extends `JSONRPCError`.

- JSONRPCError
- ParseError
- InvalidRequest
- MethodNotFound
- InvalidParams
- InternalError
- ServerError
