import os

fifo_cliente_servidor = "/tmp/fifo_cliente_servidor"
fifo_servidor_cliente ="/tmp/fifo_servidor_cliente"


if not os.path.exists(fifo_cliente_servidor):
    os.mkfifo(fifo_cliente_servidor)

if not os.path.exists(fifo_servidor_cliente):
    os.mkfifo(fifo_servidor_cliente)

while True:
    servidor_lee = os.open (fifo_cliente_servidor, os.O_RDONLY)
    buffer_size = 4096  
    path_archivo = os.read(servidor_lee, buffer_size).decode()
    print("ruta archivo:", path_archivo)
    os.close(servidor_lee)
    servidor_escribir = os.open(fifo_servidor_cliente, os.O_WRONLY)
    print("servidor")
    try:
        archivo = open(path_archivo, os.O_RDONLY)
        contenido = archivo.read()
        mensaje = contenido.encode('utf8')
       
    
    except FileNotFoundError:
        mensaje_error = f"El archivo {path_archivo} noexiste"
        mensaje = mensaje_error.encode('utf8')
       

    os.write(servidor_escribir, mensaje)
    os.close(servidor_escribir)
    