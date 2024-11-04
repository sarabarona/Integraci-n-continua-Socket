import socket

# Configuración del servidor
HOST = '0.0.0.0'  # Escuchar en todas las interfaces de red
PORT = 8080

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexión aceptada de {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recibido: {data.decode()}")
            conn.sendall(b"Hola desde el servidor")
