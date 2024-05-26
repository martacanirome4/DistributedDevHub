import os
import time
import threading

def servidor(pipe):
    while True:
        fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S")
        os.write(pipe, fecha_hora.encode())

def cliente(pipe):
    while True:
        fecha_hora = os.read(pipe, 100).decode()
        print("Fecha y hora recibidas del servidor:", fecha_hora)

if __name__ == "__main__":
    pipe_cliente, pipe_servidor = os.pipe()

    # Crear un hilo para el servidor
    hilo_servidor = threading.Thread(target=servidor, args=(pipe_servidor,))
    hilo_servidor.start()

    # Crear varios hilos para los clientes
    for _ in range(5):  # Cambia el número de clientes según sea necesario
        hilo_cliente = threading.Thread(target=cliente, args=(pipe_cliente,))
        hilo_cliente.start()

    # Esperar a que todos los hilos terminen
    hilo_servidor.join()
