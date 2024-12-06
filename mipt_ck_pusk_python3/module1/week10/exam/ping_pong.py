from select import select
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            s, *_ = select([self.request], [], [], 20)
            if not s:
                print(f'{self.client_address[0]} disconnected due to timeout')
                break
            try:
                self.data = self.request.recv(4)
            except ConnectionResetError:
                print(f'{self.client_address[0]} disconnected')
                break
            if self.data != b'PING':
                print(f'{self.client_address[0]} disconnected')
                break
            self.request.sendall(b'PONG')


class MyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    HOST, PORT = "localhost", 5000
    with MyServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
