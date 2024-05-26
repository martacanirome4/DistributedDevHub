# p9/server.py
import socket
from KataRomanos import KataRomanos

def main():
    p1 = KataRomanos()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 2225)
    print('Estableciendo conexión con {} en el puerto {}'.format(*server_address))
    sock.bind(server_address)

    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            while True:
                data = connection.recv(1024)    
                if not data:
                    break
                
                decodeData = data.decode("utf8")

                if decodeData.isdigit():
                    numero_entero = int(decodeData)
                    numero_traducido = p1.entero_a_romano(numero_entero)
                    numero_convertido_en_cadena = str(numero_traducido)
                    numero_binario = numero_convertido_en_cadena.encode("utf8")
                    connection.sendall(numero_binario)
                
                elif p1.es_numero_romano(decodeData):
                    romanoConvertidoEntero = p1.romano_a_entero(decodeData)
                    entero_string = str(romanoConvertidoEntero)
                    entero_bytes = entero_string.encode("utf8")
                    connection.sendall(entero_bytes)
                
                else:
                    mensaje = "ERROR"
                    connection.sendall(mensaje.encode("utf8"))
        finally:
            connection.close()

if __name__ == "__main__":
    main()
