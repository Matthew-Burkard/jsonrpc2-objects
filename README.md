# JSON-RPC 2.0 Objects

A collection of objects for use in JSON-RPC 2.0 implementations.

## Installation

```shell
pip install jsonrpc2-objects
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

Python exceptions are available for each JSON-RPC 2.0 error.
Each error extends `JSONRPCError`.

Example use with client:
```python
from jsonrpcobjects.errors import MethodNotFound, JSONRPCError 

try:
    client.example_method(params)
except MethodNotFound:
    print('Handle method not found')
except JSONRPCError:
    print('Handle any JSON RPC error.')
```

## JSON Types

Type hints are provided for the following JSON types.
- JSONPrimitive
- JSONArray
- JSONObject
- JSONStructured
- JSON
