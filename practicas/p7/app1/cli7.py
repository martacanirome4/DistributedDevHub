# p7/app1/cli7.py

import socket
import threading

def recibir_mensajes(sock):
    try:
        while True:
            mensaje = sock.recv(1024).decode()
            if not mensaje:
                print("Servidor desconectado.")
                break
            print(mensaje)
    except ConnectionResetError:
        print("Conexión con el servidor perdida.")

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dir_servidor = "127.0.0.1"  
puerto_servidor = 5545
print("Cliente:")

try:
    cliente_socket.connect((dir_servidor, puerto_servidor))
    cliente_nombre = input("Ingrese su nombre: ")
    cliente_socket.send(cliente_nombre.encode())

    respuesta = cliente_socket.recv(1024).decode()

    print(respuesta)

    if respuesta == "Nombre aceptado":

        print("- - - ¡Bienvenido! Escriba 'exit' para abandorar el chat - - -")

        # iniciar un nuevo hilo para recibir mensajes del servidor
        recibir_thread = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
        recibir_thread.start()
        try:
            while True:
                mensaje = input("")
                if not recibir_thread.is_alive():
                    break
                cliente_socket.send(mensaje.encode())
                if mensaje.lower() == "exit":
                    print("Saliendo del chat...")
                    break

        except KeyboardInterrupt:
            print("Saliendo forzosamente del chat...")
        except ConnectionAbortedError:
            print("La conexión al servidor se ha interrumpido.")
            
    else:
        print("La conexión al servidor ha sido rechazada, nombre de usuario no disponible. Inténtelo de nuevo.")

except ConnectionRefusedError:
    print("No se puede conectar al servidor.")


finally:
    cliente_socket.close()
    print("Conexion cerrada.")
