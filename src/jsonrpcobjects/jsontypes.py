from typing import Union, Optional

JSONPrimitive = Optional[Union[str, int, float, bool]]
JSONArray = list['JSON']
JSONObject = dict[str, 'JSON']
JSONStructured = Union[JSONObject, JSONArray]
JSON = Union[JSONPrimitive, JSONStructured]
