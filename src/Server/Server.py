import threading
import socket


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.all_clients = []

        # Initializing a server socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)

        # Running a connection handler for accepting new connections
        self.handleConnection()

    def handleConnection(self):
        # Server is continuously accepting new connections
        while True:
            client, client_addr = self.server.accept()
            if client not in self.all_clients:
                self.all_clients.append(client)
                threading.Thread(target=self.handleMessage, args=(client, )).start()

    def handleMessage(self, client):
        while True:
            try:
                msg = client.recv(1024)
                print(msg.decode('utf-8'))

                for person in self.all_clients:
                    if person != client:
                        person.send(msg)
            except ConnectionError:
                self.all_clients.remove(client)
                client.close()
                break


def main():
    server = Server('192.168.0.14', 2000)


if __name__ == '__main__':
    main()
