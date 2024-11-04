import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    print("Servidor escuchando en el puerto 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada de {client_address}")
        message = client_socket.recv(1024).decode()
        print(f"Mensaje recibido: {message}")
        client_socket.send("Mensaje recibido".encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
