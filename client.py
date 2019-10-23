import socket
import time

# 접속 정보 설정
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)


def connect() -> socket.socket:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDR)

    return client_socket


def send(client_socket: socket.socket, massage: str) -> None:
    client_socket.send(massage.encode())
    msg = client_socket.recv(SIZE)
    print("resp from server : {}".format(msg))


def main() -> None:
    start = time.time()

    for i in range(1):
        print(time.time()-start)
        client_socket1 = connect()
        send(client_socket1, str(i))
        client_socket1.close()


main()
