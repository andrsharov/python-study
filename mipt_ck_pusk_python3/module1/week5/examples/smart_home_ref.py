import time


def send_message(address: str, message: str) -> str:
    # TODO
    print(f'Sending message {message!r} to {address}...')
    if 'TEMP' in message:
        return 'TEMP 23.5'
    return '23.5'


class KineticSensor:
    def __init__(self, address):
        self.address = address

    def read(self):
        response = send_message(self.address, 'SENSOR READ 0')
        return float(response)


class SmartApp:
    def __init__(self, address):
        self.address = address

    def read(self):
        response = send_message(self.address, 'GET TEMP')
        return float(response[5:])


class HeatingController:
    def __init__(self, address, pin):
        self.address = address
        self.pin = pin

    def _set_heating(self, action):
        send_message(self.address, f'RELAY-SET-255-{self.pin}-{action}')

    def increase(self):
        self._set_heating(1)

    def decrease(self):
        self._set_heating(0)


class Room:
    def __init__(self, name, sensor, controller, target_temp, dt):
        self.name = name
        self.dt = dt
        self.target_temp = target_temp
        self.controller = controller
        self.sensor = sensor

    def check_temp(self):
        fact = self.sensor.read()
        if fact > self.target_temp + self.dt:
            self.controller.decrease()
        elif fact < self.target_temp - self.dt:
            self.controller.increase()


rooms = [
    Room('Гостиная', KineticSensor('192.168.1.45'),
         HeatingController('192.168.1.60', 1),
         22.5, 0.3),
    Room('Спальня', SmartApp('192.168.1.46'),
         HeatingController('192.168.1.60', 2),
         23.0, 0.2),
    Room('Кухня', SmartApp('192.168.1.47'),
         HeatingController('192.168.1.61', 1),
         23.0, 0.5),
    Room('Ванная', KineticSensor('192.168.1.48'),
         HeatingController('192.168.1.61', 2),
         24.0, 0.1)
]

while True:
    for room in rooms:
        room.check_temp()
    time.sleep(5)
