import socket
import sys

def start_server(port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_socket.bind(('0.0.0.0', port))
    
    # Start listening for connections
    server_socket.listen(1)
    print(f"Server started, listening on port {port}...")
    
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")
    
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        
        print(f"Client: {data}")
        
        # If the client sends "terminate", close the connection
        if data.strip().lower() == "terminate":
            print("Client has terminated the connection.")
            break
    
    # Close the sockets
    client_socket.close()
    server_socket.close()
    print("Server has shut down.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python my_server_app.py <port>")
        sys.exit(1)
    
    port = int(sys.argv[1])
    start_server(port)
