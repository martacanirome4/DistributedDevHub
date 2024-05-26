# p9/client.py

import socket
from datetime import datetime
import os
import time

def main():
    now = datetime.now()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dirServer = input("Introduce la dirección del servidor: ")
    server_address = (dirServer, 2225)
    sock.connect(server_address)

    queQuiereElCliente = input("Introduce el número que deseas traducir: ")

    try:
        solicitudEnBytes = queQuiereElCliente.encode("utf8")
        sock.sendall(solicitudEnBytes)
        
        data = sock.recv(1024)
        os.write(1, data)
    finally:
        print('\nCerrando socket...')
        sock.close()

if __name__ == "__main__":
    main()
