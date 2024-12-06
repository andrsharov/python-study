import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip().decode('utf-8')
            if not self.data:
                break
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            self.request.sendall(self.data.upper().encode('utf-8'))

class MyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == "__main__":
    HOST, PORT = "localhost", 5000
    with MyServer((HOST, PORT), MyTCPHandler) as server:
        server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)
        server.serve_forever()
