from typing import Optional, Union

JSONPrimitive = Optional[Union[bool, int, float, str]]
JSONArray = list["JSON"]
JSONObject = dict[str, "JSON"]
JSONStructured = Union[JSONArray, JSONObject]
JSON = Union[JSONPrimitive, JSONStructured]
