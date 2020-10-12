import socket
import struct

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(localhost, 12666))
serversocket.listen(5)
(clientsocket, address) = serversocket.accept()
    
