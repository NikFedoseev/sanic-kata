import enum
import json
import re
import time

from lib.json_encoder import DateTimeAndEnumJSONEncoder, StandartDateTimeJSONEncoder


def custom_dumps(obj, isoformat=True):
    if isoformat:
        return json.dumps(obj, cls=DateTimeAndEnumJSONEncoder)
    return json.dumps(obj, cls=StandartDateTimeJSONEncoder)