import socket
import sys


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("socket criado com sucesso")

    host = "localhost"
    port = 5432

    s.bind((host, port))

    message = "Servidor: Hey Client"

    while 1:
        data, address = s.recvfrom(4096)

        if data:
            sys.stdout.flush()

            s.sendto((message.encode()), address)
            s.shutdown(2)
            break


if(__name__ == "__main__"):
    main()
