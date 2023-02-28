"""
This is the code from `example_socket_server.ipynb`, exported without minimal
documentation. This is the minimal socket programming server example!
"""

import socket
import struct
import os

# 1. Set up the socket and listen
ADDRESS_FAMILY = socket.AF_UNIX
SOCKET_TYPE = socket.SOCK_STREAM
ADDRESS = './some_filename.sock'

if os.path.exists(ADDRESS):
    os.remove(ADDRESS)

serversocket = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
serversocket.bind(ADDRESS)
serversocket.listen()

# 2. Accept the connection when the client connects.
# This line will wait until that happens...
print("Waiting for client to connect...")
connection, address = serversocket.accept()
print("... Connected!")

# 3. Receive bytes from the client and unpack to integers
x_from_client = connection.recv(8)
print(f"Received {x_from_client}")
y_from_client = connection.recv(8)
print(f"Received {y_from_client}")

x_from_client = struct.unpack('<q', x_from_client)
y_from_client = struct.unpack('<q', y_from_client)
print(f"Unpacked as {x_from_client}")
print(f"Unpacked as {y_from_client}")

# 4. Calculate the sum and return the result to the client
result = x_from_client[0] + y_from_client[0]
print(f"Packing as {result}")
result = struct.pack('<q', result)
print(f"Sending {result}")
connection.send(result)

# 5. All done! Close the connection
connection.close()
print("All done!")
