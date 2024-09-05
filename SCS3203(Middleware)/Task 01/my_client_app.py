import socket
import sys

def start_client(server_ip, server_port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")
    
    while True:
        # Read user input
        message = input("Enter message: ")
        
        # Send the message to the server
        client_socket.sendall(message.encode('utf-8'))
        
        # If the message is "terminate", close the connection
        if message.strip().lower() == "terminate":
            print("Terminating connection...")
            break
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python my_client_app.py <server_ip> <server_port>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
