import socket

IP = "127.0.0.1"
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

while True:
    message = input("Enter your message (or type 'QUIT' to close connection): ")
    client_socket.send(message.encode("utf-8"))
    if message.lower() == "quit":
        print("Client has closed the connection.")
        break

    response = client_socket.recv(1024).decode("utf-8")
    if response.lower() == "quit":
        print("Server has closed the connection.")
        break
    print(f"Server response: {response}")

client_socket.close()
