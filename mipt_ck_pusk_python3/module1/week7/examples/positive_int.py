class PositiveInt:
    def __init__(self, value: int):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError('value of PositiveInt must be positive')
        self._value = new_value
