# 🌐 DistributedDevHub

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![C](https://img.shields.io/badge/language-C-lightblue)
![Sockets](https://img.shields.io/badge/Networking-Sockets-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**Colección de proyectos y recursos sobre desarrollo de aplicaciones distribuidas**  
Este repositorio aborda temas clave como **comunicación entre procesos (IPC)** usando pipes, fifos, sockets (TCP/UDP), y metodologías de desarrollo como **TDD (Test-Driven Development)** para garantizar software de calidad.

![2929337_drawreese2news_mario-pipe-gif](https://github.com/martacanirome4/DistributedDevHub/assets/50625677/0092e526-d3b2-46ed-a23f-612b12fafdc1)

---

## 📦 Contenido

- **🧪 TDD (Test-Driven Development)**: Proyectos guiados por pruebas, como la **Kata de Bolos**, aplicando buenas prácticas desde el inicio.
- **🔧 Pipes y FIFOs**: Comunicación entre procesos en sistemas Unix mediante **pipes anónimos** y **fifos** (pipes con nombre).
- **🌐 Sockets**: Ejemplos de comunicación cliente-servidor en red usando **sockets UDS (Unix Domain Sockets)**, **TCP/IP** y **UDP**.

---

## 🗂️ Estructura del Repositorio

- `/practicas/` - Carpetas organizadas por tipo de proyecto (cada una con README específico)
- `/apuntes/` - Recursos teóricos y apuntes técnicos sobre IPC, redes, y TDD

---

## 📋 Lista de Proyectos

1. 🎯 Kata de TDD de Bolos
2. 🔌 Cliente-Servidor mediante pipes
3. 🔌 Cliente-Servidor mediante FIFOs
4. 🔌 Cliente-Servidor mediante sockets UDS (Unix Domain Sockets)
5. 🌍 Cliente-Servidor mediante sockets UDP de Internet
6. 🌍 Cliente-Servidor mediante sockets TCP de Internet
7. 💬 Cliente-Servidor de mensajería mediante sockets TCP de Internet

---

## 📓 Información Complementaria

### 🔄 Comunicación entre Procesos (IPC)
- **Pipes/FIFOs**: Usados para pasar datos entre procesos relacionados (pipes) o no relacionados (fifos), en sistemas tipo Unix.
- **Sockets**: Permiten la comunicación a través de la red, ya sea local (**UDS**) o global (**TCP/UDP**).

### 🌐 TCP vs UDP
- **TCP**: Protocolo orientado a conexión, garantiza entrega de datos. Ideal para aplicaciones donde la fiabilidad importa.
- **UDP**: Protocolo sin conexión, rápido y ligero. Perfecto para aplicaciones en tiempo real (ej. juegos, streaming).

### 🧪 TDD - Desarrollo Guiado por Pruebas
- Escribe primero las pruebas, luego el código → permite detectar errores temprano y mejora la arquitectura del software.

> "Primero falla la prueba, luego escribe el código para pasarla, y finalmente refactoriza. Repite." – Ciclo TDD

---

## 🏋️ Diagrama: Pila de Protocolos TCP/IP vs OSI

| Capa OSI              | Capa TCP/IP         | Ejemplos de Protocolos           |
|----------------------|---------------------|----------------------------------|
| 7. Aplicación        | Aplicación          | HTTP, FTP, SSH, DNS              |
| 6. Presentación      | —                  | SSL/TLS                          |
| 5. Sesión            | —                  | NetBIOS, RPC                     |
| 4. Transporte         | Transporte          | TCP, UDP                         |
| 3. Red                | Internet            | IP, ICMP                         |
| 2. Enlace de Datos    | Acceso a Red        | Ethernet, Wi-Fi, ARP             |
| 1. Física            | Acceso a Red        | Cables, conectores, señales      |

> El modelo **TCP/IP** es el usado en redes modernas. El modelo **OSI** es más teórico pero ayuda a entender la separación de funciones.

---

## 🎯 Objetivo del Repositorio

Este repositorio busca consolidar prácticas esenciales en sistemas distribuidos y redes, desarrollando aplicaciones robustas con **técnicas reales de la industria** y fomentando el aprendizaje práctico con recursos teóricos.

---

## 👩‍💻 Autoría

Marta Canino Romero  
[@martacanirome4](https://github.com/martacanirome4)  
GitHub 2023

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=martacanirome4&show_icons=true&theme=radical)

---

## 📅 Licencia

MIT License – Libre uso con atribución  
[Ver licencia](https://opensource.org/licenses/MIT)

---

## 💬 Extra Flow Ideas

- 📊 Benchmark de rendimiento TCP vs UDP
- 📹 GIFs o demos de mensajes cruzados cliente-servidor
- 🧵 Gráfico visual del flujo de datos entre procesos
- 🌍 Mini entorno virtual de pruebas con Docker Compose
