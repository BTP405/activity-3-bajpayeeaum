import socket
import threading
import pickle

class ChatClient:
    """
    A simple chat client that connects to a chat server to send and receive messages.
    """

    def __init__(self, host, port, username):
        """
        Initialize the chat client.

        Parameters:
        - host (str): The host address of the chat server.
        - port (int): The port number of the chat server.
        - username (str): The username of the client.
        """
        self.host = host
        self.port = port
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.sendall(pickle.dumps(username))

    def receive_messages(self):
        """
        Receive messages from the chat server and print them.
        """
        try:
            while True:
                data = self.socket.recv(4096)
                if not data:
                    break
                message = pickle.loads(data)
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
        finally:
            self.socket.close()

    def send_message(self):
        """
        Send messages typed by the user to the chat server.
        """
        try:
            while True:
                message = input()
                data = pickle.dumps(f"{self.username}: {message}")
                self.socket.sendall(data)
        except Exception as e:
            print(f"Error sending message: {e}")
        finally:
            self.socket.close()

    def start(self):
        """
        Start the client by creating and starting threads for sending and receiving messages.
        """
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        send_thread = threading.Thread(target=self.send_message)
        send_thread.start()

if __name__ == "__main__":
    username = input("Enter your username: ")
    client = ChatClient('localhost', 5555, username)
    client.start()


