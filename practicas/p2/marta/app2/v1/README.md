# Programa Cliente-Servidor con Pipes en Python

Este programa implementa una aplicación sencilla Cliente-Servidor en Python utilizando pipes (tuberías) para de Unix la comunicación entre procesos.

El cliente se conecta al servidor mediante una tubería (pipe), y el servidor le contesta con on la fecha y hora actual en el formato estándar internacional.
El cliente muestra la respuesta recibida por el servidor en su salida standard.

Cuando se ejecuta el script desde la terminal, nos convertimos el proceso que está iniciando el programa, por lo que tanto en el proceso padre, que actúa como el cliente. El proceso hijo, que actúa como el servidor, se crea dentro del script.

## Requisitos
- Python 3.11

## Instalación
Para ejecutar la aplicación, simplemente ejecute desde el directorio en la terminal el script de Python `cliserv2.py`.

```bash
python3 cliserv2.py
```

## Uso
El servidor y el cliente se ejecutarán en procesos separados. Una vez que se complete la interacción, los procesos se cerrarán automáticamente.