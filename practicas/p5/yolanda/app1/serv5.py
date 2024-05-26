# app1/serv5.py

import socket

s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dir_servidor = '127.0.0.1'  
puerto_servidor = 5555
print("Servidor esperando peticiones... ")

try:
    s_socket.bind((dir_servidor, puerto_servidor))
    while True:
        data, addr = s_socket.recvfrom(4096)
        path_fichero = data.decode()
        try:
            with open(path_fichero, 'r') as file:
                contenido = file.read()
                respuesta = contenido.encode()     
        except FileNotFoundError:
            respuesta = b"El fichero solicitado no existe."
        s_socket.sendto(respuesta, addr)
        
except OSError as e:
        print(f"Error al enlazar con el socket: {e}")
finally:
    s_socket.close()
