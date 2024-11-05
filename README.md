# Proyecto de Comunicación entre Contenedores Docker
Este proyecto implementa una comunicación entre dos contenedores Docker utilizando sockets. Un contenedor actúa como servidor y el otro como cliente. Ambos se comunican a través de una red privada de Docker, lo que permite un canal de comunicación directo y aislado.

### Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos instalados en tu máquina:

Docker: Docker es necesario para crear y administrar contenedores.

## Instrucciones de instalación de Docker
Docker Compose: Docker Compose es una herramienta para definir y ejecutar aplicaciones de múltiples contenedores Docker.

Instrucciones de instalación de Docker Compose
Clonar el Repositorio
Para comenzar, clona este repositorio en tu máquina local utilizando Git:

```bash
git clone https://github.com/sarabarona/Integraci-n-continua-Socket.git
cd mi_servicio_socket 
```
Descripción del Proyecto
Este proyecto consiste en dos contenedores Docker que se comunican entre sí a través de sockets. El contenedor servidor escucha en un puerto determinado (por ejemplo, el puerto 5000) y el contenedor cliente se conecta al servidor para recibir un mensaje.

El servicio de comunicación se ejecuta utilizando un archivo docker-compose.yml que orquesta ambos contenedores.

Instrucciones de Ejecución
Paso 1: Construir y levantar los contenedores
Una vez clonado el repositorio, ejecuta el siguiente comando para construir las imágenes de Docker y levantar ambos contenedores utilizando Docker Compose:

``` bash
docker-compose up --build
```
Este comando:

Construirá las imágenes de Docker para el servidor y el cliente.
Levantará los contenedores y los conectará a través de una red interna creada por Docker Compose.
Paso 2: Verificar la Ejecución
Después de ejecutar docker-compose up --build, los contenedores deberían empezar a ejecutarse. El servidor estará esperando conexiones en el puerto 5000, y el cliente intentará conectarse a él.

Para verificar que los contenedores están funcionando correctamente, puedes ver los logs de los contenedores con el siguiente comando:

``` bash

docker-compose logs
``` 

Deberías ver en los logs algo similar a esto:

El servidor mostrando que está esperando conexiones:


Esperando conexiones...
El cliente mostrando el mensaje recibido del servidor:

``` yaml
Mensaje recibido: Hola desde el servidor!
```

Paso 3: Detener los contenedores
Para detener y eliminar los contenedores, redes y volúmenes creados por Docker Compose, ejecuta:

``` bash
docker-compose down
```
Este comando detendrá y eliminará todos los recursos asociados al proyecto.

Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:

``` bash
/mi_servicio_socket
    - Dockerfile
    - server.py
    - Dockerfile
    - client.py
    -docker-compose.yml
    -README.md
  ```
/servidor_socket: Contiene los archivos necesarios para el contenedor servidor (el script server.py y su Dockerfile).
/cliente_socket: Contiene los archivos necesarios para el contenedor cliente (el script client.py y su Dockerfile).
docker-compose.yml: El archivo que define la orquestación de contenedores y redes.
README.md: Este archivo de documentación.
Detalles Técnicos
server.py (Servidor)
Este archivo contiene el código del servidor que escucha en el puerto 5000, esperando una conexión de un cliente. Cuando recibe una conexión, le envía un mensaje.

client.py (Cliente)
El archivo client.py contiene el código del cliente, que se conecta al servidor y recibe el mensaje enviado por él.

docker-compose.yml
Este archivo define los servicios de Docker Compose para orquestar los dos contenedores (servidor y cliente), asegurando que se comuniquen entre sí a través de una red interna de Docker.

Dockerfiles
Cada contenedor (servidor y cliente) tiene su propio Dockerfile para definir cómo se construye la imagen de Docker. Ambos archivos utilizan la imagen base de python:3.9-slim y copian los archivos necesarios para ejecutar el servidor y el cliente.

Contribuciones
Si deseas contribuir a este proyecto, puedes realizar un fork del repositorio, crear una nueva rama, y hacer tus cambios. Luego, puedes abrir un pull request con una descripción detallada de lo que has hecho.

Contacto
Si tienes alguna duda o sugerencia sobre el proyecto, no dudes en abrir un issue en el repositorio.

¡Gracias por usar este proyecto! 😄

