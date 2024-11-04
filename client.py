import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('server', 8080))
    message = "Hola desde el cliente!"
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Respuesta del servidor: {response}")
    client_socket.close()

if __name__ == "__main__":
    start_client()
