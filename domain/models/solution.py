import copy


class Solution:
    def __init__(self, **kwargs):
        self._data = {}
        for key, value in kwargs.items():
            self.set(key, value)

    def __repr__(self):
        return f"Solution({self._data})"

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value

    def __getattr__(self, item):
        data = self.__dict__.get("_data", None)

        if data is not None and item in data:
            return data[item]

        raise AttributeError(f"'Solution' object has no attribute '{item}'")

    def copy(self):
        return copy.deepcopy(self)