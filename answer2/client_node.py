import socket
import pickle

def send_task(task, args, worker_address):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(worker_address)
        data = pickle.dumps((task, args))
        client_socket.sendall(data)
        response = receive_complete_message(client_socket)
        return pickle.loads(response)
    except socket.error as e:
        print(f"Socket error: {e}")
        return None
    except pickle.PickleError as e:
        print(f"Pickling error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if client_socket:
            client_socket.close()

def receive_complete_message(sock):
    data = b''
    while True:
        part = sock.recv(4096)
        data += part
        if len(part) < 4096:  # End of message
            break
    return data

# Example usage:
if __name__ == "__main__":
    task = some_function
    args = (arg1, arg2)  # Arguments for the task
    worker_address = ('localhost', 12345)  # Address of the worker node
    result = send_task(task, args, worker_address)
    print("Result:", result)

