import socket
import json
import memcached
import shlex

cache = memcached.Memcached()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))
s.listen(1)

try:
    while True:

        print('Waiting for client...')
        conn, addr = s.accept()
        print('Connected:', addr)

        with conn:

            while True:
                cmd = b''
                # get one command
                while True:
                    data = conn.recv(1) # read single char until you get '\n'
                    # read until '\n'
                    if not data or data == b'\n':
                        break
                    cmd += data

                cmd = cmd.decode('utf-8')

                print('cmd:', cmd)

                if cmd.lower() == 'quit':
                    break

                args = shlex.split(cmd)

                if args[0] == 'set':
                    cache.set(args[1], args[2], int(args[3]))
                elif args[0] == 'add':
                    cache.add(args[1], args[2], int(args[3]))
                elif args[0] == 'get':
                    cache.get(args[1])
                elif args[0] == 'append':
                    cache.append(args[1], args[2], int(args[3]))
                elif args[0] == 'replace':
                    cache.replace(args[1], args[2], int(args[3]))
                elif args[0] == 'prepend':
                    cache.prepend(args[1], args[2], int(args[3]))        
                else:
                    print('ERROR')    
finally:
    s.close()                

