# Inter-process Communication Comparison
This README.md details the differences between **sockets** and **shared memory** for those wanting to do interprocess communication. This folder also contains a simple server/client program written in a Jupyter notebook, implemented using sockets and explaining each step thoroughly.

List of files:
 * `example_socket_server.ipynb`: Read and run this to understand socket programming! Use alongside the client notebook.
 * `example_client_server.ipynb`: Read and run this to understand socket programming! Use alongside the server notebook.
 * `server.py` and `client.py` summarize the example notebooks with very minimal comments and prionts. The notebooks have a lot of writing, which makes it look complicated, but in reality it uses very few lines of code!
 * `server_min.py` and `client_min.py` have even less clutter, with no `print` statements or comments.
    * The server uses 17 lines of code, and the client uses only 11!

## The gist of it:
"Inter-process communication" (IPC) is used to share data between two processes on the same machine. Unlike single-process computing, it is subject to concurrent-computing issues like [race conditions](https://en.wikipedia.org/wiki/Race_condition), [deadlock](https://en.wikipedia.org/wiki/Deadlock), the [Reader-Writer problem](https://en.wikipedia.org/wiki/Readers%E2%80%93writers_problem), and more.

There are two main forms of IPC: **Sockets** and **shared memory**. Sockets utilize APIs / syscalls to share data in a structured manner. In Python they are blocking by default, which means certain socket functionality like `recv()` will stall until the socket has something to read. This can help avoid concurrent-computing issues. Shared memory, however, reads and writes data inside RAM using file I/O operations. It is much faster, it is a bit easier to understand how to use, but requires the user know how to implement sempahores, lock-files, etc. to solve certain issues.

Sockets are a standard used in every major operating system and supported by most programming languages! They are also commonly used to send data through the internet. Learning to use sockets will pay off, since you will surely need to use them again in the future!

| Sockets | Shared Memory |
| - | - |
| Read and write raw bytes. Use `struct` | Read and write data using `open(...)` to `/dev/shm` |
| Linear read/write and blocking sockets avoids issues | Must be implemented carefully to avoid race conditions and other issues |
| | Faster than sockets, but might be slowed down by synchronization lock objects
| Widely used, should work identically on every platform | Might require rewriting code to run on Windows or MacOS |
| Can be easily rewritten as network sockets with little extra work |  |
| Most popular form of IPC, by far. | Second most popular form of IPC. |
| | In Python 3.8, see `multiprocess.shared_memory` |

The similarities between the two are:

 * Both are popular forms of IPC.
 * Data only exists in RAM.
 * Make it easy for programs in different langauges to "talk".
 * Can be used for parallel processing.

## Technical details of Sockets

> **Note:** The best way to learn will be by doing! Consider checking out the notebook. This is a quick summary that might answer questions you have.
>
> I *highly recommend* the [Sockets in Python: Guide by Gordon McMillan.](https://docs.python.org/3/howto/sockets.html).
> 
> The following resources are also good:
>  * The [Python official socket documentation](https://docs.python.org/3/library/socket.html), especially the "Example" section
>  * The [Python official struct documentation](https://docs.python.org/3/library/struct.html), especially the "Format Strings" and the "Examples" sections
>  * The [Wikipedia article on Berkely sockets](https://en.wikipedia.org/wiki/Berkeley_sockets)

A **socket** is an endpoint for two processes to talk to one another. There are two main kinds of sockets: [Unix Domain Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), which are used in interprocess communication, and [Network Sockets](https://en.wikipedia.org/wiki/Network_socket) (TCP and UDP), on top of which more complicated protocols like HTTP are built. These sockets all operate under the well-known [Berkley Socket](https://en.wikipedia.org/wiki/Berkeley_sockets) (aka POSIX Socket) API, which means that sockets will work almost identically in each different programming language.

### Socket functions
Berkely sockets provide some standard functions to interact with sockets. The functions offered and their parameters will depend on the *address family* and *socket type*.

| Function    | A.K.A. | Server or client? | Description |
| - | - | - |
| `socket()`  | - | Both   | Operating system prepares resources for a socket.
| | | | `socket()` takes two parameters: Address family (or "domain"), socket type, and protocol.
| | | | In Python, the protocol will depend on the socket type, and does not need to be set. 
| `bind()`    | - | Server | Operating system associates socket with an *address* (see below).
| `listen()`  | - | Server | (`SOCK_STREAM` / "TCP") Server prepares to hear a connection on to the socket.
| `connect()` | - | Client | Client connects to existing socket using address.
| `accept()`  | - | Server | (`SOCK_STREAM` / "TCP") Connection is finished, data can now be sent.
| `send()`    | `write()`  | Both | Send bytes to the socket buffer
| `recv()`    | `read()`   | Both | Read (and remove!) bytes from the socket buffer.
| `close()`   | - | Both   | Terminate the connection and clean up resources.

Other standard functions include `gethostbyname()` and `gethostbyaddr()` (for `AF_INET` addresses), `select()` `poll()`, and `getsockopt()` and `setsockopt()` to read/write socket options,

### Socket address families and types
Sockets need *addresses* so that other processes can connect to them. There can be one socket per address.

| Domain | Example address | Details |
| - | - | -
| `AF_INET`  | `('192.168.50.1', 12345)` | IPv4 addresses. Specified by a host (IP or URL) and a port.
| `AF_INET6` | `(address, port, flowinfo, scope_id)` | IPv6 addresses. Read more details at the [IPv6 man page](https://man7.org/linux/man-pages/man7/ipv6.7.html).
| `AF_UNIX`  | `./some_filename.sock` | File descriptor. Does not actually read/write to disk! Used exclusively for interprocess communication.
| | | `AF_UNIX` stream sockets will not overrun -- `send()` will block until data is read from the socket with `recv()`. 

Sockets also have *types* that specify how they work.

| Type             | Details |
| `SOCK_STREAM`    | Reliable, sequenced, connection-oriented. One-to-one communication. | 
| `SOCK_DGRAM`     | Unreliable, connectionless. Many can read, many can write. | 
| `SOCK_SEQPACKET` | Reliable, sequenced, connection-oriented. One-to-many communication. |
| `SOCK_RAW`       | Write raw IP packets. |

The `SOCK_STREAM` is a "stream socket" which operates in a "TCP style". It is connection-oriented and packets are sequenced. This means that only two parties are communicating (i.e. server and client), and packages arrive in the order sent. Data must be read from buffer or they will overflow. **Most of the time, you want `SOCK_STREAM` sockets.**

The `SOCK_DGRAM` is a "datagram socket" which operates in a "UDP style". It is connectionless, meaning anyone can read or write to/from such a socket, and packets are not guaranteed to arrive, nor are they guaranteed to arrive in the order sent.

The `SOCK_SEQPACKET` is a "sequenced packet" which operates in "SCTP style". This is less commonly used (and less documented) than the `SOCK_STREAM` style. This is useful when a server has many clients it wishes to read from on one port. It may not be implemented on all platforms and languages.

The `SOCK_RAW` allows you to write *raw IP packets* with `AF_INET`. May require sudo access.

### Packaging data for sockets
In Python, we are privileged in that we rarely need to consider "data types". Integers can grow to any size without encountering most overflow errors. Floats and ints can interact without pain. We rarely need to do memory management, or think about the individual bytes composing an integer.

This is because each integer and float in Python are actually *objects* that have a lot of special functionality associated with them! Python numbers are kinda *special*. But sockets need to communicate *raw bytes*, so we need to cut that cruft away before sending it over the network.

Basically, **one needs to pack and unpack data when sending it over a socket.** This may be unfamiliar, but luckily, Python provides a module called `struct` to make this much easier. 

In Python, we will use `socket` to perform the connection, and `struct` to pack and unpack data from bytes. Here is an example, [courtesy of Mark Tolonen on StackOverflow](https://stackoverflow.com/questions/50494918/send-array-of-floats-over-a-socket-connection):

```
    >>> import struct
    >>> sample = [0.9,120000,0.85,12.8,0.1,28,16,124565,0.72,3.9]
    >>> data = struct.pack('<10f',*sample)
    >>> print(data)
    b'fff?\x00`\xeaG\x9a\x99Y?\xcd\xccLA\xcd\xcc\xcc=\x00\x00\xe0A\x00\x00\x80A\x80J\xf3G\xecQ8?\x9a\x99y@'
    >>> data = struct.unpack('<10f',data)
    >>> data
    (0.8999999761581421, 120000.0, 0.8500000238418579, 12.800000190734863, 0.10000000149011612, 28.0, 16.0, 124565.0, 0.7200000286102295, 3.9000000953674316)
```

The most important lines are `struct.pack('<10f', *sample)` and `struct.unpack('<10f', sample)`. It prescribes a **format** with `'<10f'`, meaning "Pack these 10 floating-point numbers using little-endian encoding." It produces "data", a 40-byte string.

Then, `struct.unpack` interprets those 40 bytes back into the 10 floating-point numbers. You can see the full details of `struct` format-strings at [the official documentation](https://docs.python.org/3/library/struct.html).

Some things you have to be aware of:
 * **Endianness:** Should the unsigned int "6" be stored as `00000110` or `01100000`? It depends on the computer! 
    * Little-endian is most common, but do not assume! Specify little-endian on both ends.
    * Use `'<'` to specify little-endian.
    * E.g. Per [the docs](https://docs.python.org/3/library/struct.html), we can pack our int as `'<B'`.
 * **Data type:** To understand the [Format Characters](https://docs.python.org/3/library/struct.html#format-characters) and how to use them, you need to [recall/study the primitive datatypes](https://en.wikipedia.org/wiki/C_data_types).
    * Recall the difference between `signed` and `unsigned` integers, between `char`/`int`/`long`/`long long` integers, and `float` vs `float64`.
 * **Integer capacity:** Python uses magic to allow *very large* integers, which can exceed what `struct` can natively pack. You may need to explore alternative representations for huge integers.
    * This is similar to "BigInteger" in Java or `libgmp` in C.
    * A `long long` can only take on values between about +- 9.23 x 10^18. Python 
    * One solution may be to use the built in `hex` function to represent the integer as hexadecimal values, and send in that manner.

If you have a complicated piece of data you want to send over a socket, you can use `pickle`, which will convert a Python object to bytes to send over a socket. **But Pickle is not safe to use in general!** Anyone who can connect to your port can send malicious data. Safely using pickle is outside the scope of this document.


### Control with Sockets versus Shared Memory
See: https://stackoverflow.com/questions/2101671/unix-domain-sockets-vs-shared-memory-mapped-file

Sockets have a great advantage over shared memory, since data is written and read linearly. Synchronization is implicit with blocking-sockets. Sockets will provide a lot of utility when it comes to communicating between programs. Sockets are **more portable**, the skills used in sockets are **more applicable** to other applications, and **synchronization** is implicit in the socket mechanism. One socket is used for communication between **two processes**. Reading-writing data requires working with **raw bytes.**
