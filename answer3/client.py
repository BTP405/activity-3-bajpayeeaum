import socket
import threading
import pickle

class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.sendall(pickle.dumps(username))

    def receive_messages(self):
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
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        send_thread = threading.Thread(target=self.send_message)
        send_thread.start()

if __name__ == "__main__":
    username = input("Enter your username: ")
    client = ChatClient('localhost', 5555, username)
    client.start()

