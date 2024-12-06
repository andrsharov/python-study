import socket

response = '''HTTP/1.1 {code} {code_name}
Content-Type: text/html; charset=utf-8
Content-Length: {byte_len}

'''.replace('\n', '\r\n')


def generate_response(code, text):
    codes = {
        200: 'OK',
        403: 'Forbidden',
        404: 'Not Found',
    }
    content = text.encode('utf-8')
    return response.format(
        code=code,
        code_name=codes[code],
        byte_len=len(content)
    ).encode('utf-8') + content


with socket.create_server(('0.0.0.0', 5000)) as server:
    while True:
        client, addr = server.accept()
        request = client.recv(4096).decode('utf-8')
        print(request)
        method, resource, *other = request.split()
        if resource == '/':
            code, text = 200, 'Привет!'
        elif resource == '/admin':
            code, text = 403, 'Сюда нельзя'
        else:
            code, text = 404, 'Такого нет'
        client.sendall(generate_response(code, text))
