import socket
import struct

clientsocket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
clientsocket.connect('./some_filename.sock')

x = struct.pack('<q', 7)
clientsocket.send(x)
y = struct.pack('<q', 10)
clientsocket.send(y)

result_from_server = clientsocket.recv(8)
result_from_server = struct.unpack('<q', result_from_server)[0]

clientsocket.close()
