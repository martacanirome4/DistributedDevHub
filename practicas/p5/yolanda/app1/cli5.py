# app1/cli5.py

import socket, datetime, os
import signal
c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


dir_servidor = "127.0.0.1"  
puerto_servidor = 5554
path_archivo = "fichero.txt"

print("Cliente")
c_socket.sendto(path_archivo.encode(), (dir_servidor, puerto_servidor))


respuesta, dir = c_socket.recvfrom(4096)
print("Respuesta del Servidor: ",respuesta.decode())

c_socket.close()
