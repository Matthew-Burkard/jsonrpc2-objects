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

| Object                   | Description                 |
|--------------------------|-----------------------------|
| RequestObjectParams      | Request with params         |
| RequestObject            | Request without params      |
| NotificationObjectParams | Notification with params    |
| NotificationObject       | Notification without params |
| ErrorResponseObject      | Response with result        |
| ResultResponseObject     | Response with error         |

## Errors

Python exceptions are available for each JSON-RPC 2.0 error. Each error
extends `JSONRPCError`.

Example use with a client implementing these errors:

```python
from jsonrpcobjects.errors import JSONRPCError, MethodNotFound

try:
    client.example_method(params)
except MethodNotFound:
    print("Handle method not found")
except JSONRPCError:
    print("Handle any JSON RPC error.")
```
