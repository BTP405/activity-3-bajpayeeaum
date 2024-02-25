# client.py
import socket
import pickle

def load_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def main():
    host = '127.0.0.1'
    port = 12352
    buffer_size = 4096

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        file_path = input("Enter the path of the file to send: ")
        file_data = load_file(file_path)
        pickled_data = pickle.dumps(file_data)

        client_socket.sendall(pickled_data)
        print("File sent successfully")
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
