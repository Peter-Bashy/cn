import socket

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    messages = ["Hello!", "How are you?", "Goodbye!"]

    for msg in messages:
        client_socket.send(msg.encode())
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode()}")

    client_socket.close()

start_client()