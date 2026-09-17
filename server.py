import socket

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            client_socket.send(f"Echo: {data.decode()}".encode())

        client_socket.close()
        print(f"Connection with {client_address} closed.")

start_server()
# Save client output to a file
python client.py > output.txt 2>&1

# Push everything to GitHub
git add server.py client.py output.txt
git commit -m "Add TCP client/server with output"
git push