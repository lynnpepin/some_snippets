"""
This is the code from `example_socket_client.ipynb`, exported without minimal
documentation. This is the minimal socket programming client example!
"""

import socket
import struct

# 1. Set up the socket and connect
ADDRESS_FAMILY = socket.AF_UNIX
SOCKET_TYPE = socket.SOCK_STREAM
ADDRESS = './some_filename.sock'

print("Waiting to connect to server...")
clientsocket = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
clientsocket.connect(ADDRESS)
print("... Connected!")

# 2. Send two integers
x = struct.pack('<q', 7)
print(f"Sending {x}")
clientsocket.send(x)
y = struct.pack('<q', 10)
print(f"Sending {y}")
clientsocket.send(y)

# 3. Receive the sum
result_from_server = clientsocket.recv(8)
print(f"Received {result_from_server}")
result_from_server = struct.unpack('<q', result_from_server)[0]
print(f"Result formatted as {result_from_server}")

# 5. All done! Close the connection
clientsocket.close()
print("All done!")
