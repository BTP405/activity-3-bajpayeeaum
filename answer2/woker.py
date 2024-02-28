import socket
import pickle

def run_worker(port):
    """
    Run a worker node that listens for tasks, executes them, and sends back the results.

    Parameters:
    - port (int): The port on which the worker node listens for incoming connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print("Worker node is listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connected to", client_address)

        try:
            data = client_socket.recv(4096)
            task, args = pickle.loads(data)
            result = task(*args)
            response_data = pickle.dumps(result)
            client_socket.sendall(response_data)
        except socket.error as e:
            print(f"Socket error: {e}")
        except pickle.PickleError as e:
            print(f"Pickling error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

# Example function that worker node can execute
def some_function(arg1, arg2):
    """
    An example function that can be executed by the worker node.

    Parameters:
    - arg1: First argument.
    - arg2: Second argument.

    Returns:
    - The sum of arg1 and arg2.
    """
    return arg1 + arg2

if __name__ == "__main__":
    run_worker(12345)

