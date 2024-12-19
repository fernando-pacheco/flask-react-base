from flask_apispec import marshal_with
from src.schemas.message import (
    MessageErro400,
    MessageErro401,
    MessageErro403,
    MessageErro404,
)


def error_decorators(status_codes=None):
    mapper = [
        (400, MessageErro400),
        (401, MessageErro401),
        (403, MessageErro403),
        (404, MessageErro404),
    ]

    if status_codes is None:
        status_codes = [400, 401, 403, 404]

    def decorator(cls):
        for code, schema in mapper:
            if code in status_codes:
                cls = marshal_with(schema, code=code)(cls)

        return cls

    return decorator
