# server.py
import socket
import pickle

def save_file(data, filename):
    """
    Save the received file data to the specified file.

    Parameters:
    - data (bytes): The content of the file to be saved.
    - filename (str): The name of the file to save the data into.
    """
    with open(filename, 'wb') as f:
        f.write(data)

def main():
    """
    Main function to start the server, listen for connections, and save received files.

    It binds the server to a specific host and port, listens for incoming connections,
    receives pickled data from clients, prompts the user for the filename to save the received
    file, saves the file, and handles any potential errors.
    """
    host = '127.0.0.1'
    port = 12352
    buffer_size = 4096

    # Create a server socket, bind it to the specified host and port, and start listening
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening at", (host, port))

    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print("Connected to", client_address)

        try:
            # Receive data from the client
            data = client_socket.recv(buffer_size)
            # Unpickle the received data
            file_data = pickle.loads(data)

            # Prompt the user to enter the filename to save the received file
            filename = input("Enter the filename to save the received file: ")
            # Save the received file data
            save_file(file_data, filename)
            print("File saved successfully as", filename)
        except Exception as e:
            # Handle any exceptions that occur during the process
            print("Error:", e)
        finally:
            # Close the client socket
            client_socket.close()

if __name__ == "__main__":
    main()
