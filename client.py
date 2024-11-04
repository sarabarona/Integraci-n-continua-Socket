import socket
import time

# Configuración del cliente
HOST = 'server'  # Nombre del servicio del servidor en Docker Compose
PORT = 8080

# Esperar unos segundos para asegurarse de que el servidor esté listo
time.sleep(5)

try:
    # Crear el socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = "Hola desde el cliente"
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Recibido: {data.decode()}")

    client_socket.close()
except Exception as e:
    print(f"Error: {e}")
