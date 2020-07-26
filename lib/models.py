import os

import json
from typing import Any, Dict

from django.conf import settings

app_path = settings.BASE_DIR


class BaseModel:
    keys = []

    def __init__(self, data):
        self.data = self._load_data(data)

    def _load_data(self, app_name: str) -> list:
        file_path = os.path.join(app_path, app_name, 'data.json')
        with open(file_path) as fl:
            data = json.load(fl)
        return data

    def _serialize(self, obj):
        result = {}
        for k in self.keys:
            description = None
            if '/' in k:
                k, description = k.split('/')
            if '.' in k:
                k1, k2 = k.split('.')
                val = obj[k1][k2]
                k = k2
            else:
                val = obj[k]
            if description is not None:
                k = description
            result[k] = val
        return result

    def get_by_key(self, key: str, value: int) -> Any:
        obj = list(filter(lambda o: o[key] == value, self.data))
        if obj:
            return self._serialize(obj[0])
        return None

    def eq_gt_then(self, key: str, value: int) -> Any:
        obj = list(filter(lambda o: int(o[key]) >= value, self.data))
        if obj:
            return [self._serialize(o) for o in obj]
        return None

    def all(self) -> list:
        return [self._serialize(o) for o in self.data]

