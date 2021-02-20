import socket
import json

class Client:

    def __init__(self):
        self.host = 'localhost'
        self.port = 12345
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    """Command handler client-side""" 
    def command(self, cmd):
        print('send: ', cmd)
        cmd = cmd.encode('utf-8') + b'\n'   
        self.socket.sendall(cmd)
    """Run function to prompt for input from the client"""
    def run(self):
        while True:
            cmd = input('cmd: ')    
            self.command(cmd)
            if cmd.lower() == 'quit':
                break
# create new instance of client and set it to run to start server-client communication
newClient = Client()
newClient.run()  
