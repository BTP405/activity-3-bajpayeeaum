# client.py
import socket
import pickle

def load_file(filename):
    """
    Load file from the specified path.

    Parameters:
    - filename (str): The path of the file to be loaded.

    Returns:
    - bytes: The content of the file as bytes.
    """
    with open(filename, 'rb') as f:
        return f.read()

def main():
    """
    Main function to establish a connection to the server and send a file.

    It prompts the user to enter the path of the file to be sent,
    loads the file, pickles the data, sends it over the network,
    and handles any potential errors.
    """
    host = '127.0.0.1'
    port = 12352
    buffer_size = 4096

    # Create a client socket and establish a connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        # Prompt the user to enter the path of the file to send
        file_path = input("Enter the path of the file to send: ")
        # Load the file data
        file_data = load_file(file_path)
        # Serialize the data using pickle
        pickled_data = pickle.dumps(file_data)

        # Send the serialized data over the network
        client_socket.sendall(pickled_data)
        print("File sent successfully")
    except Exception as e:
        # Handle any exceptions that occur during the process
        print("Error:", e)
    finally:
        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    main()
