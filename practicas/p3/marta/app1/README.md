# Aplicación Cliente-Servidor de Ficheros con FIFOs en Python

Este programa implementa una aplicación Cliente-Servidor en Python utilizando FIFOs para la comunicación entre procesos. El cliente se conecta al servidor y le envía la ruta completa de un fichero. El servidor responde con los contenidos del fichero solicitado, o un mensaje de error si no pudo proporcionarlos. El cliente muestra la respuesta recibida por el servidor en su salida estándar.

## Requisitos
- Python 3.11

## Instalación
1. Clone o descargue el repositorio en su máquina local.
2. Asegúrese de tener el directorio `/tmp` creado en su sistema.
3. Ejecute el script del servidor (`serv3.py`) en una terminal.
```bash
python3 serv3.py
```
4. Ejecute el script del cliente (cli3.py) en otra terminal, proporcionando la ruta completa del archivo como argumento.
```bash
python3 cli3.py /ruta/completa/del/archivo.txt
```