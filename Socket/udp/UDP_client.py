import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Cliente socket acriado com sucesso")

    host = "localhost"
    port = 5430

    message = "Opa!"

    try:
        print("client: {}".format(message))
        s.sendto(message.encode(), (host, port))

        data, server = s.recvfrom(4096)
        print(data.decode())
    finally:
        print("cliente fechando")
        s.close()


if(__name__ == "__main__"):
    main()
