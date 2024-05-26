# p6/yolanda/app2/serv6.py

import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dir_servidor = "127.0.0.1"
puerto_servidor = 5557

print("- Cliente -")

try:
    cliente_socket.connect((dir_servidor, puerto_servidor))
    mensaje = "Dime fecha y hora"
    cliente_socket.send(mensaje.encode('utf-8'))
    respuesta = cliente_socket.recv(1024).decode('utf-8')
    print(respuesta)
    cliente_socket.close()
except ConnectionRefusedError:
    print("No se ha podido conectar con el servidor.")
except Exception as e:
    print("Error:", e)
finally:
    cliente_socket.close()
