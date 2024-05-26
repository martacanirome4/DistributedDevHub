# p7/app1/serv7.py

import socket
import threading
import select

def manejar_cliente(cliente_socket, cliente_nombre):
    try:
        while True:
            mensaje = cliente_socket.recv(1024).decode()
            if mensaje:
                if mensaje.lower() == "exit":
                    print("Cliente {} ha salido del chat.".format(cliente_nombre))
                    cliente_socket.close()
                    # sacarlo, destruir al clienrte y borrarlo
                    del clientes_conectados[cliente_socket]
                    break

                remitente = cliente_nombre
                print("{}: {}".format(remitente, mensaje)) 

                # reenviar mensaje a todos los clientes conectados
                for cliente in clientes_conectados:
                    if cliente != cliente_socket:
                        cliente.send(("{}: {}".format(remitente, mensaje)).encode())
            else:
                print("Cliente {} se ha desconectado.".format(cliente_nombre))
                cliente_socket.close()
                del clientes_conectados[cliente_socket]
                break

    except ConnectionResetError:
        print("El cliente {} se ha desconectado inesperadamente.".format(cliente_nombre))
        cliente_socket.close()
        del clientes_conectados[cliente_socket]

    except Exception as e:
        print("Error en la conexión con {}: {}".format(cliente_nombre, e))
        cliente_socket.close()
        del clientes_conectados[cliente_socket]

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dir_servidor = '127.0.0.1'
puerto_servidor = 5545

# intentar enlazar y escuchar el socket del servidor
try:
    servidor_socket.bind((dir_servidor, puerto_servidor))
    servidor_socket.listen(1)
    print("Servidor escuchando en {}:{}".format(dir_servidor, puerto_servidor))
except Exception as e:
    print("Error al iniciar el servidor:", e)
    exit(1)

clientes_conectados = {}
# usar como clave los nicks
try:
    while True:
        socket_lectura, _, _ = select.select(list(clientes_conectados.keys()) + [servidor_socket], [], [])

        for socket_preparado in socket_lectura:
            if socket_preparado is servidor_socket:
                cliente_socket, cliente_direccion = servidor_socket.accept()
                cliente_nombre = cliente_socket.recv(1024).decode()
                    
                if cliente_nombre in clientes_conectados.values():
                    print("El nombre de usuario '{}' ya está en uso.".format(cliente_nombre))
                    cliente_socket.send("Nombre de usuario no disponible".encode())
                    cliente_socket.close()
                else:
                    print("Conexión establecida con {}:{} como '{}'".format(cliente_direccion[0], cliente_direccion[1], cliente_nombre))
                    clientes_conectados[cliente_socket] = cliente_nombre
                    cliente_socket.send("Nombre aceptado".encode())
                    # iniciar un nuevo hilo para manejar la conexion del cliente
                    cliente_thread = threading.Thread(target=manejar_cliente, args=(cliente_socket, cliente_nombre))
                    cliente_thread.start()




except KeyboardInterrupt:
    print("\nServidor detenido.")
    # Informar a los clientes conectados que el servidor se está cerrando
    for cliente in list(clientes_conectados.keys()):
        try:
            cliente.send("El servidor se está cerrando...".encode())
            cliente.close()
        except Exception as e:
            print(f"Error al cerrar la conexión del cliente: {e}")

finally:
    servidor_socket.close()
    print("Conexiones cerradas. El servidor ha terminado.")