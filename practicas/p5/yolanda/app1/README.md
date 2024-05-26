# Proyecto de Comunciación de Sockets UDP
 
 Este proyecto consiste en dos scripts, uno para el servidor ('serv5.py') y otro para el cliente ('cli5.py)', que se comunican a través de sockets UDP. El cliente envía una solicitud con el nombre de un archivo al servidor, y el servidor responde con el contenido del archivo si existe, o con un mensaje de error si no se encuentra el archivo.

## Estructura del Proyecto
ped7/
└── p5/
    └── yolanda/
        └── app1/
            ├── serv5.py
            ├── cli5.py
            ├── MAKEFILE
            └── README.md

## Requisitos Previos

- Python 3.x
- Sistema operativo con soporte para sockets (Linux, macOS, Windows)

## Instrucciones para Ejecutar el Proyecto

1. Clonar el Repositorio
Clona este repositorio en tu máquina local:
    ```bash
    git clone http://git.eps.ceu.es/ped/ped7
    cd ped7/p5/yolanda/app1
    ```

2. Crear un Archivo de Prueba
Para probar el servidor y el cliente, crea un archivo de texto llamado fichero.txt en el mismo directorio:
    ```bash
    echo "Este es un archivo de prueba." > fichero.txt
    ```

3. Ejecutar el Servidor
Primero, inicia el servidor. Abre una terminal y ejecuta uno de los siguientes comandos:
    ```bash
    make serv
    ```
ó
    ```bash
    python3 serv5.py
    ```
Verás la salida indicando que el servidor está esperando peticiones:
    ```bash
    Servidor esperando peticiones
    ```

4. Ejecutar el Cliente
En otra terminal, ejecuta el cliente para solicitar el contenido del archivo al servidor:
    ```bash
    make cli
    ```
ó
    ```bash
    python3 cli5.py
    ```
La salida del cliente debería mostrar el contenido del archivo recibido del servidor:
    ```bash
    Cliente
    Respuesta Servidor: Este es un archivo de prueba.
    ```
