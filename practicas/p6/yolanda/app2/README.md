# Proyecto de Comunicación Cliente-Servidor con Sockets

## Descripción
Este proyecto demuestra la implementación de un sistema de comunicación cliente-servidor utilizando sockets en Python. El servidor escucha las solicitudes de los clientes y responde con la fecha y hora actuales en un formato legible. La comunicación se realiza utilizando el protocolo TCP/IP.

## Estructura del Proyecto
proyecto-sockets/
├── app2/
│   ├── serv6.py
│   └── cli6.py
└── README.md

## Requisitos Previos
- Python 3.x
- Sistema operativo compatible con sockets (Windows, macOS, Linux)

## Instrucciones para Ejecutar el Proyecto
1. Abre una terminal y ejecuta el servidor:
    ```bash
    python3 serv6.py
    ```
Deberías ver:    
    ```bash
    - Servidor -
    Esperando solicitud...
    ```

4. Ejecutar el Cliente
En otra terminal, ejecuta el cliente:
    ```bash
    python3 cli6.py
    ```
Deberías ver:    
    ```bash
    - Cliente -
    Domingo, 26 Mayo 2024, 12:02:49
    ```

## Notas
- Asegúrate de que ningún otro servicio esté utilizando el puerto 5557 en 127.0.0.1.
- Puedes modificar el puerto y la dirección IP en los archivos de código si es necesario.
- Este ejemplo está diseñado para funcionar en una máquina local. Para ejecutarlo en una red, asegúrate de actualizar las direcciones IP y las configuraciones de firewall adecuadamente.
