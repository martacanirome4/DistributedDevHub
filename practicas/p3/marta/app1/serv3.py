import os

def servidor():
    fifo_cliente_path = '/tmp/fifo_cliente_grupo7'
    os.mkfifo(fifo_cliente_path)

    while True:
        print("Esperando conexión del cliente...")
        with open(fifo_cliente_path) as fifo_cliente:
            nombre_archivo = fifo_cliente.read().strip()
            print("Nombre del archivo recibido:", nombre_archivo)

            try:
                with open(nombre_archivo, 'r') as archivo:
                    contenido = archivo.read()
                    fifo_servidor_path = '/tmp/fifo_servidor_grupo7'
                    with open(fifo_servidor_path, 'w') as fifo_servidor:
                        fifo_servidor.write(contenido)
                    print("Contenido del archivo enviado al cliente.")
            except FileNotFoundError:
                with open(fifo_servidor_path, 'w') as fifo_servidor:
                    fifo_servidor.write("Error: El archivo no existe.")
                print("Error: El archivo no existe.")

if __name__ == "__main__":
    servidor()
