import time
import random


def get_lucky_number():
    time.sleep(3)  # Здесь может быть какое-то вычисление
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class DataProvider:
    def __init__(self):
        self.data = {}

    def get_data(self):
        time.sleep(3)  # Здесь может быть обращение к внешнему сервису
        self.data = {"field1": 100, "field2": 200}
        return self.data
