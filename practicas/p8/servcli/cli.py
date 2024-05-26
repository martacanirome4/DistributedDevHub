# p8/servcli/cli.py

import socket
import os
import sys

bufferSize = 100

def client(server_address, server_port, file_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server_address, server_port))
        s.sendall(file_name.encode("utf-8"))

        while True:
            data = s.recv(bufferSize)
            if data.endswith(b"fin_de_fichero"):
                break
            print(data.decode("utf-8"), end="")
    except Exception as e:
        print("An error occurred while communicating with the server:")
        print(e)
    finally:
        s.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        address = "127.0.0.1"
        port = 5111
        file = sys.argv[1]
    elif len(sys.argv) == 4:
        address = sys.argv[1]
        port = int(sys.argv[2])
        file = sys.argv[3]
    else:
        print("Usage: python cli.py [address] [port] [file]")
        exit(1)

    client(address, port, file)
