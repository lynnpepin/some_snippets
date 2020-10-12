# Inter-process Communication Comparison

These Jupyter notebook compares the two main methods for inter-process communication: **Sockets** and **shared memory.**



Here, we'll set up a very simple synchronous client-server architecture.

## The gist of it:

"Inter-process communication" (IPC) is used to share data between two machines. Unlike single-process computing, it is subject to [race conditions](https://en.wikipedia.org/wiki/Race_condition) and other sorts of issues that appear in parallel-computing and multithreading.

There are two main forms of IPC: **Sockets**, which are easier to architect and are more widely used, and **shared memory** which is faster and easier to read/write data with, but more difficult to architect multiprocessing. A summary of both:


## Comparison

| Sockets | Shared Memory |
| - | - |
| Read and write raw bytes, using `struct` | Read and write data using `open(...)` to `/dev/shm` |
| Linear read/write and blocking sockets avoids issues | Must be implemented carefully to avoid race conditions and other issues |
| | Faster, but might be slowed down by necessary synchronization lock objects
| Widely used, should work identically on every platform | Might require extra code to run on Windows and MacOS |
| Can be extended to network sockets with little extra work |  |
| Most popular form of IPC, by far. | Second most popular form of IPC. |
| | In Python 3.8, see `multiprocess.shared_memory` |

### Both Sockets and Shared Memory:
 * Popular forms of IPC.
 * Data only exists in RAM.
 * Make it easy for programs in different langauges to "talk".
 * Can be used for parallel processing, etc. 


## Technical details of Sockets

> **Note:** The best way to learn will be by doing! Consider checking out the notebook. This is a quick summary that might answer questions you have.
>
> Again, I *highly recommend* the [Sockets in Python: Guide by Gordon McMillan.](https://docs.python.org/3/howto/sockets.html).

A **socket** is an endpoint for two processes to talk to one another. There are two main kinds of sockets: [Unix Domain Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), which are used in interprocess communication, and [Network Sockets](https://en.wikipedia.org/wiki/Network_socket) (TCP and UDP), on top of which more complicated protocols like HTTP are built. These sockets all operate under the well-known [Berkley Socket](https://en.wikipedia.org/wiki/Berkeley_sockets) (aka POSIX Socket) API.

So, a person who knows how to use Network Sockets will know 99% of what they need to know for Domain Sockets! A very useful skill, as they show up in all sorts of networking.


### Packaging data for sockets

There are some difficulties. Mainly, you will send and recieve *raw bytes* over a socket. In Python, we will use `socket` to perform the connection, and `struct` to pack and unpack data from bytes. Here is an example, [courtesy of Mark Tolonen on StackOverflow](https://stackoverflow.com/questions/50494918/send-array-of-floats-over-a-socket-connection):

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

The most important lines are `struct.pack('<10f', *sample)` and `struct.unpack('<10f', sample)`. It prescribes a **format** with `'<10f'`, meaning "Pack these 10 floating-point numbers using little-endian encoding." It produces "data", a 40-byte string. Then, `struct.unpack` interprets the 40 bytes back into 10 floating-point numbers. You can see the full details of `struct` format-strings at [the official documentation](https://docs.python.org/3/library/struct.html).

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

TODO FROM HERE

https://stackoverflow.com/questions/2101671/unix-domain-sockets-vs-shared-memory-mapped-file

Sockets have a great advantage over shared memory, since data is written and read linearly. Synchronization is implicit with blocking-sockets.

### Sockets technical conclusion

Sockets will provide a lot of utility when it comes to communicating between programs. Sockets are **more portable**, the skills used in sockets are **more applicable** to other applications, and **synchronization** is implicit in the socket mechanism. One socket is used for communication between **two processes**. Reading-writing data requires working with **raw bytes.**



## Technical Details of Shared Memory

We should not used Shared Memory unless speed is absolutely critical.

## A note on system design

The reason for writing this guide is to provide some 
