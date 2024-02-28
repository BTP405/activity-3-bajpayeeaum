import socket
import pickle

def send_task(task, args, worker_address):
    """
    Send a task along with its arguments to a worker node and receive the result.

    Parameters:
    - task (function): The task function to be executed by the worker.
    - args (tuple): The arguments to be passed to the task function.
    - worker_address (tuple): The address of the worker node (host, port).

    Returns:
    - The result of the task function executed by the worker.
    """
    try:
        # Create a client socket and establish a connection to the worker node
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(worker_address)
        
        # Serialize the task and its arguments using pickle
        data = pickle.dumps((task, args))
        
        # Send the serialized data to the worker node
        client_socket.sendall(data)
        
        # Receive the response from the worker node
        response = receive_complete_message(client_socket)
        
        # Deserialize the response
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
        # Close the client socket
        if client_socket:
            client_socket.close()

def receive_complete_message(sock):
    """
    Receive a complete message from a socket.

    Parameters:
    - sock (socket): The socket to receive the message from.

    Returns:
    - bytes: The complete message received from the socket.
    """
    data = b''
    while True:
        part = sock.recv(4096)
        data += part
        if len(part) < 4096:  # End of message
            break
    return data

# Example usage:
if __name__ == "__main__":
    task = some_function  # Define the task function
    args = (arg1, arg2)   # Arguments for the task
    worker_address = ('localhost', 12345)  # Address of the worker node
    result = send_task(task, args, worker_address)
    print("Result:", result)


