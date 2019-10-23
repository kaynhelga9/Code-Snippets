import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full += msg

        if(len(full)-HEADERSIZE == msglen):
            print('full msg recv')
            print(full[HEADERSIZE:])

            d = pickle.loads(full[HEADERSIZE:])
            print(d)
            
            new_msg = True
            full = b''

print(full)