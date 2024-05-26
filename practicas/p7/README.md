# Proyecto de Chat Cliente-Servidor

Este proyecto implementa un chat cliente-servidor utilizando sockets en Python. Permite a múltiples clientes conectarse al servidor simultáneamente y comunicarse entre ellos en tiempo real.

## Estructura del Proyecto

p7/
├── app1/
│   ├── serv7.py
│   ├── cli7.py
│   └── MAKEFILE
├── ARCHITECTURE
├── INSTALL
└── README.md

## Funcionalidades

- Comunicación en Tiempo Real: Los clientes pueden enviar mensajes al servidor, y estos mensajes serán retransmitidos a todos los otros clientes conectados en tiempo real.
- Gestión de Usuarios: Los clientes pueden elegir un nombre de usuario al iniciar sesión en el chat, lo que les permite identificarse y comunicarse de manera personalizada.
- Salir del Chat de Forma Segura: Los clientes pueden salir del chat de forma segura escribiendo "exit" en el chat. Esto cierra la conexión con el servidor de manera ordenada y permite que el cliente termine su sesión adecuadamente.
- Gestión Concurrente de Conexiones: El servidor puede manejar múltiples conexiones de clientes de manera concurrente utilizando hilos, lo que garantiza un rendimiento óptimo incluso cuando hay muchos usuarios conectados simultáneamente.

## Archivos Adicionales

- ARCHITECTURE: Este archivo proporciona una descripción detallada de la arquitectura del proyecto, incluyendo los componentes principales y cómo interactúan entre sí. Este archivo también proporciona un MANUAL DE USUARIO con información detallada sobre cómo utilizar el software una vez que está instalado.
- INSTALL: Contiene instrucciones detalladas sobre cómo instalar y configurar el chat cliente-servidor en tu máquina local.
- MAKEFILE: Un archivo de makefile que puede ser utilizado para automatizar tareas comunes de compilación y ejecución del proyecto.

## Requisitos Previos
- Python 3.x: Asegúrate de tener instalado Python 3.x en tu sistema antes de ejecutar el chat cliente-servidor.

## Instalación y Uso

1. Clona el Repositorio: Clona este repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone http://git.eps.ceu.es/ped/ped7
```

2. Navegar al Directorio: Navega al directorio p7/app1 del proyecto en tu terminal.

3. Ejecutar el Servidor: Inicia el servidor ejecutando uno de los siguientes comandos:

```bash
make serv
```

```bash
python3 serv7.py
```

4. Ejecutar el Cliente: Abre otra terminal y navega al mismo directorio p7/app1. Luego, inicia el cliente ejecutando uno de los siguientes comandos:

```bash
make cli
```
s
```bash
python3 cli7.py
```

5. Ingresar Nombre de Usuario: Cuando se te solicite, ingresa un nombre de usuario único para identificarte en el chat.

6. ¡Comenzar a Chatear!: Una vez conectado, puedes comenzar a enviar y recibir mensajes en el chat. Para salir del chat, simplemente escribe "exit" y presiona Enter.

7. Detener el Servidor: Para detener el servidor, simplemente presiona Ctrl + C en la terminal donde se está ejecutando el script 'serv7.py'.
