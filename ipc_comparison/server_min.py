import socket
import struct
import os

if os.path.exists('./some_filename.sock'):
    os.remove('./some_filename.sock')

serversocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
serversocket.bind('./some_filename.sock')
serversocket.listen()
connection, address = serversocket.accept()

x_from_client = connection.recv(8)
x_from_client = struct.unpack('<q', x_from_client)[0]
y_from_client = connection.recv(8)
y_from_client = struct.unpack('<q', y_from_client)[0]

result = x_from_client + y_from_client
result = struct.pack('<q', result)
connection.send(result)

connection.close()
