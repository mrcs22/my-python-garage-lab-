import os
import time


def ping_hosts(file_path):
    with open(file_path) as file:
        dump = file.read()
        dump_lines = dump.splitlines()

        os.system("clear")

        for ip in dump_lines:
            print("#" * 60, "\n\nVerificando o ip: {}\n".format(ip))

            os.system("ping -n 2 {}".format(ip))

            print("\n\n")
            time.sleep(5)


if(__name__ == "__main__"):
    ping_hosts("hosts.txt")
