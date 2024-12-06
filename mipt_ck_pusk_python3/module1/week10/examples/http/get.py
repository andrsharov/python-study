import socket

request = b'''GET /python HTTP/1.1
Host: cs.mipt.ru
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
DNT: 1
Sec-GPC: 1

'''.replace(b'\n', b'\r\n')

data = b''
with socket.create_connection(('cs.mipt.ru', 80)) as con:
    con.sendall(request)
    while True:
        chunk = con.recv(4096)
        if not chunk:
            break
        data += chunk

headers, data = data.split(b'\r\n\r\n', 1)
print(headers.decode())
