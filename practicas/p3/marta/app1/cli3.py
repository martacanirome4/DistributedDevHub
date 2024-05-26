import os

def cliente(ruta_archivo):
    fifo_cliente_path = '/tmp/fifo_cliente_grupo7'
    os.mkfifo(fifo_cliente_path)

    with open(fifo_cliente_path, 'w') as fifo_cliente:
        fifo_cliente.write(ruta_archivo)

    fifo_servidor_path = '/tmp/fifo_servidor_grupo7'
    with open(fifo_servidor_path) as fifo_servidor:
        respuesta = fifo_servidor.read()
        print("Respuesta recibida del servidor:", respuesta)
