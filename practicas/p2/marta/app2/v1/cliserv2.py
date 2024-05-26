import os
import time

def servidor(pipe):
    """escribe la fecha y hora actual en la tuberia del servidor"""
    fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S")
    os.write(pipe, fecha_hora.encode())
    os.close(pipe)

def cliente(pipe):
    """lee la fecha y hora del servidor desde la tubería del cliente 
     y la imprime en la salida estandar"""
    fecha_hora = os.read(pipe, 100).decode()
    print("Fecha y hora recibidas del servidor:", fecha_hora)
    os.close(pipe)

if __name__ == "__main__":
    # r, w = os.pipe() --> cliente lee, servidor escribe:
    pipe_cliente, pipe_servidor = os.pipe()

    pid = os.fork() # crea nuevo proceso (hijo)

    if pid == 0:
        """proceso hijo, actua como servidor"""
        os.close(pipe_cliente) # cierra el extremo de escritura de la tubería del cliente
        servidor(pipe_servidor)
    else:
        os.close(pipe_servidor) # cierra el extremo de lectura de la tubería del servidor
        cliente(pipe_cliente)
