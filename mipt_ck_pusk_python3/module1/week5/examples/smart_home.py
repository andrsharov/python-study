import time


def send_message(address: str, message: str) -> str:
    # TODO
    print(f'Sending message {message!r} to {address}...')
    if 'TEMP' in message:
        return 'TEMP 23.5'
    return '23.5'


room_sensors = [
    # список содержит пары (адрес, производитель)
    ('192.168.1.45', 'KineticSensor'),  # Гостиная
    ('192.168.1.46', 'SmartApp'),       # Спальня
    ('192.168.1.47', 'SmartApp'),       # Кухня
    ('192.168.1.48', 'KineticSensor'),  # Ванная
]

room_controller = [
    # содержит пары (адрес контроллера, номер пина)
    ('192.168.1.60', 1),  # Гостиная
    ('192.168.1.60', 2),  # Спальня
    ('192.168.1.61', 1),  # Кухня
    ('192.168.1.61', 2),  # Ванная
]

target_temperature = [
    # содержит пары (требуемая температура, допустимая дельта)
    (22.5, 0.3),
    (23.0, 0.2),
    (23.0, 0.5),
    (24.0, 0.1)
]


def get_temperatures():
    result = []
    for address, manufacturer in room_sensors:
        if manufacturer == 'KineticSensor':
            response = send_message(address, 'SENSOR READ 0')
            t = float(response)
        elif manufacturer == 'SmartApp':
            response = send_message(address, 'GET TEMP')
            t = float(response[5:])
        result.append(t)
    return result


def set_heating(address, pin, action):
    send_message(address, f'RELAY-SET-255-{pin}-{action}')


while True:
    temps = get_temperatures()
    for (addr, pin), (target, dt), fact in zip(room_controller, target_temperature, temps):
        if fact > target + dt:
            set_heating(addr, pin, 0)
        elif fact < target - dt:
            set_heating(addr, pin, 1)
    time.sleep(5)
