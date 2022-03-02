import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print("erro: {}".format(e))
        sys.exit()

    print("socket client criado com sucesso")
    sys.stdout.flush()

    host = "localhost"
    port = 5430

    try:
        s.connect((host, int(port)))
        s.send("Hey ho! Let's go!".encode())
        print("conectado com sucesso em {} porta {}".format(host, port))
        sys.stdout.flush()

        data = s.recv(4096)
        print(data.decode())

        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()


if(__name__ == "__main__"):
    main()
