import socket

SIZE = 1024
CONNECT_LIST = []


def run_server(ip='127.0.0.1', port=8080):
    print('Server is running...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socker:
        server_socker.bind((ip, port))
        server_socker.listen()

        while True:
            client_socket, client_addr = server_socker.accept()
            msg = client_socket.recv(SIZE)
            print("[{}] message : {}".format(client_addr, msg))

            client_socket.send("welcome!".encode())


run_server()