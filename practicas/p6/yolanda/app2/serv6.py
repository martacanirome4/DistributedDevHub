# p6/yolanda/app2/serv6.py

import socket, datetime, os

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dir_servidor = '127.0.0.1'
puerto_servidor = 5557

servidor_socket.bind((dir_servidor, puerto_servidor))
servidor_socket.listen(1)

print("- Servidor -")
while True:
    print("Esperando solicitud...")
    cliente_socket, cliente_direccion = servidor_socket.accept()
    print("Conexión establecida con", cliente_direccion)
    try:
        mensaje_recibido = cliente_socket.recv(1024)
        if mensaje_recibido:
            fecha_actual = datetime.datetime.now()
            fecha = fecha_actual.strftime("%A, %d %B %Y, %H:%M:%S")
            cliente_socket.send(fecha.encode('utf8'))
    except Exception as e:
        print("Error:", e)
    finally:
        cliente_socket.close()
