# Proyecto de Cliente-Servidor con Python
Este proyecto implementa una aplicación de cliente-servidor en Python que permite realizar operaciones sobre archivos de texto. La comunicación entre el cliente y el servidor se realiza a través de sockets TCP/IP.

## Tipo de Conexión Cliente-Servidor
El proyecto utiliza una conexión de sockets TCP/IP para la comunicación entre el cliente y el servidor. Esto garantiza una comunicación confiable y orientada a la conexión, lo que es adecuado para aplicaciones donde se necesita transferir datos de manera segura y confiable.

## Funcionalidades
El servidor proporciona las siguientes funcionalidades:
- Filtrado de Palíndromos: El servidor puede filtrar los palíndromos presentes en un archivo de texto.
- Conteo de Vocales: El servidor cuenta el número total de vocales presentes en el archivo.
- Operaciones Específicas de la Clase Kata: El servidor utiliza métodos de la clase Kata para realizar operaciones como eliminar vocales de una cadena, añadir caracteres después de ciertos caracteres específicos, etc.

## Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:
- servcli: Contiene los archivos de código fuente del cliente ('cli.py') y el servidor ('serv.py'), así como el módulo 'Kata.py' que proporciona las funcionalidades específicas.
- tests: Contiene los archivos de prueba ('test_kata.py') para probar las funcionalidades de la clase 'Kata'.

## Ejecución del Servidor
Para ejecutar el servidor, simplemente ejecuta el siguiente comando en una terminal desde el directorio principal del proyecto:
    '''bash
    python3 servcli/serv.py <direccion_ip> <puerto>
    '''
Por ejemplo:
    '''bash
    python3 servcli/serv.py 127.0.0.1 5111
    '''

## Ejecución del Cliente
Para ejecutar el cliente y realizar operaciones sobre un archivo de texto, utiliza el siguiente comando en una terminal desde el directorio principal del proyecto:
    '''bash
    python3 servcli/cli.py <direccion_ip> <puerto> <archivo>
    '''
Por ejemplo:
    '''bash
    python3 servcli/cli.py 127.0.0.1 5111 fichero.txt
    '''

### Ejemplo de contenido de prueba
    ``bash
    Palabras palíndromas: radar, nivel, ana
    Palabras con vocales: murciélago, agua, hola
    Palabras que comienzan con 'A': Amanda, amor, araña
    Palabras con más de 7 caracteres: desarrollo, programación, pythonista
    Cadenas con mezcla de mayúsculas y minúsculas: eJEmPlO, cODigO, Algoritmo
    Números para convertir a romano:
    2021
    1094
    47
    ```

## Pruebas
Para ejecutar las pruebas unitarias, primero asegúrate de tener instalado pytest. Luego, ejecuta el siguiente comando en una terminal desde el directorio principal del proyecto:

    ```bash
    pytest
    ```
Esto ejecutará las pruebas definidas en el archivo 'test_kata.py' y mostrará los resultados en la terminal.
