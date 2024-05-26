# app2/serv4.py

import socket, datetime, os

servidor_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
path = '/tmp/soc1.sock'

if os.path.exists(path):
    os.remove(path)
servidor_socket.bind(path)
servidor_socket.listen(1)

print("- Servidor -")
while True:
    print("Esperando solicitud... ")
    cliente_socket, cliente_direccion = servidor_socket.accept()
    print("Conexión establecida con cliente.")
    try:
        mensaje_recibido = cliente_socket.recv(1024)
        if mensaje_recibido:
            fecha_actual = datetime.datetime.now()
            fecha = fecha_actual.strftime("%A, %d %B %Y, %H:%M:%S")
            cliente_socket.send(fecha.encode('utf-8'))
    except Exception as e:
        print("Error: ", e)
    finally:
        cliente_socket.close()
