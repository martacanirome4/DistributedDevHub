# Proyecto de Comunicación con Sockets UNIX
Este proyecto consiste en dos scripts, uno para el servidor ('serv4.py') y otro para el cliente ('cli4.py'), 
que se comunican a través de sockets UNIX. El servidor envía la fecha y hora actual al cliente cuando recibe una solicitud.

## Requisitos Previos
- Python 3.x
- Sistema operativo basado en UNIX (Linux, macOS)

## Estructura del Proyecto
ped7/
└── p4/
    └── yolanda/
        └── app2/
            ├── serv4.py
            ├── cli4.py
            ├── MAKEFILE
            └── README.mds

## Instrucciones para Ejecutar el Proyecto

1. Clonar el Repositorio
Clona este repositorio en tu máquina local:
    ```bash
    git clone http://git.eps.ceu.es/ped/ped7
    ```
2. Ejecutar el Servidor
Primero, inicia el servidor. Abre una terminal y ejecuta:
    ```bash
    make serv
    ```
ó
    ```bash
    python3 serv4.py
    ```
Verás la salida indicando que el servidor está esperando solicitudes:
    ```bash
    - Servidor -
    Esperando solicitud...
    ```
3. Ejecutar el Cliente
En otra terminal, ejecuta el cliente para solicitar la fecha y hora al servidor:
    ```bash
    make cli
    ```
ó
    ```bash
    python3 cli4.py
    ```
La salida del cliente debería mostrar la fecha y hora recibida del servidor:
    ```bash
    - Cliente -
    2024-05-26 14:52:35
    ```


