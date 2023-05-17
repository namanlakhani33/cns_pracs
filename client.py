

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        
        mssg = input("Enter message : ") 
        s.sendall(bytes(mssg , encoding = "utf-8"))
        if mssg.upper() == "QUIT":
            break
        data = s.recv(16)

        print(f"Received {data!r}")

    s.close()