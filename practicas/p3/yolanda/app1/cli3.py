import os

fifo_cliente_servidor = "/tmp/fifo_cliente_servidor"
fifo_servidor_cliente ="/tmp/fifo_servidor_cliente"


if not os.path.exists(fifo_cliente_servidor):
    os.mkfifo(fifo_cliente_servidor)

if not os.path.exists(fifo_servidor_cliente):
    os.mkfifo(fifo_servidor_cliente)

print("cliente iniciado") 
cliente_escribe = os.open(fifo_cliente_servidor, os.O_WRONLY)
path_archivo = input()
os.write(cliente_escribe, path_archivo.encode())
path_archivo = input( )
os.write(cliente_escribe, path_archivo.encode())
os.close(cliente_escribe)

cliente_lectura = os.open(fifo_servidor_cliente,os.O_RDONLY)
leer =os.read(cliente_lectura,4096).decode()
print("Respuesta del servidor", leer)

os.close(cliente_lectura)

 