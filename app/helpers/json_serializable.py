""" helpers.json_serializable """
from flask.json.provider import DefaultJSONProvider
from json import dumps
from app.mixins import Record


# pylint: disable=super-with-arguments
class CustomJSONProvider(DefaultJSONProvider):
    @staticmethod
    def default(o):
        if isinstance(o, Record):
            return o.deserialize()
        return DefaultJSONProvider.default(obj)
