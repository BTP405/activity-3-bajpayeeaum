# server.py
import socket
import pickle

def save_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def main():
    host = '127.0.0.1'
    port = 12352
    buffer_size = 4096

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening at", (host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connected to", client_address)

        try:
            data = client_socket.recv(buffer_size)
            file_data = pickle.loads(data)

            filename = input("Enter the filename to save the received file: ")
            save_file(file_data, filename)
            print("File saved successfully as", filename)
        except Exception as e:
            print("Error:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()

