# app2/cli4.py

import socket, os

cliente_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
path = '/tmp/soc1.sock'
print("- Cliente -")

try:
    cliente_socket.connect(path)
    mensaje = "Dime fecha y hora"
    cliente_socket.send(mensaje.encode('utf-8'))
    respuesta = cliente_socket.recv(1024)
    print(respuesta.decode('utf-8'))  # Decodificar antes de imprimir
    cliente_socket.close()
except ConnectionRefusedError:
    print("No se puede conectar al servidor")
except FileNotFoundError:
    print("No encontrado archivo", path)
except Exception as e:
    print("Error:", e)
finally:
    cliente_socket.close()
