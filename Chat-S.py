import socket

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()

print(f"Listening for connections on {IP}:{PORT}...")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

while True:
    message = client_socket.recv(1024).decode("utf-8")
    if message.lower() == "quit":
        print("Client has closed the connection.")
        break
    print(f"Received message: {message}")

    server_message = input("Enter your message (or type 'QUIT' to close connection): ")
    client_socket.send(server_message.encode("utf-8"))
    if server_message.lower() == "quit":
        print("Server has closed the connection.")
        break

client_socket.close()
