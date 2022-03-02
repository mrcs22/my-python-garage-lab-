import socket
import sys


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "localhost"
    port = 5430

    s.bind((host, port))

    print("socket server criado com sucesso")
    sys.stdout.flush()

    message = "Servidor: Hey Client"

    s.listen(1)

    while 1:
        connection, address = s.accept()

        if connection:
            print("servdior recebeu conexão")
            sys.stdout.flush()

            data = connection.recv(4096)
            print(f"Recebeu mensagem: {data.decode()} de {address}")
            sys.stdout.flush()
            
            connection.sendall(message.encode())

            break


if(__name__ == "__main__"):
    main()
