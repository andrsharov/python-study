import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip().decode('utf-8')
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper().encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 5000
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
