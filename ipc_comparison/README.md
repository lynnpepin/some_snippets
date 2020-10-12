# Inter-process Communication Comparison

These Jupyter notebook compares the two main methods for inter-process communication: **Sockets** and **shared memory.**



Here, we'll set up a very simple synchronous client-server architecture.

## The gist of it:

"Inter-process communication" (IPC) is used to share data between two machines. Unlike single-process computing, it is subject to [race conditions](https://en.wikipedia.org/wiki/Race_condition) and other sorts of issues that appear in parallel-computing and multithreading.

There are two main forms of IPC: **Sockets** which are the most widely-used and understood, and **shared memory** which is faster but more difficult. A summary of both:


## Comparison 

### Sockets:

 * Most common form of IPC.
 * Cross platform and portable -- should work on Windows, Mac, and Linux.
 * Very similar to networking code.
     * Easy to modify code to network between machines.
 * Read and write raw bytes.
    * Make use of Python's `struct`!
    * E.g. A float is 4 or 8 bytes -- need to pack and unpack properly!

I highly recommend [Sockets in Python: Guide by Gordon McMillan.](https://docs.python.org/3/howto/sockets.html).


### Shared Memory:

 * More difficult to use cross-platform.
 * Much faster than sockets.
 * More difficult to code correctly.
 * Simpler to start using: Just read/write files to/from `/dev/shm`
 * (As of Python 3.8) Can use `multiprocessing.shared_memory` for easier usage.

### Both Sockets and Shared Memory:
 * Popular forms of IPC.
 * Data only exists in RAM.
 * Make it easy for programs in different langauges to "talk".
 * Can be used for parallel processing, etc. 


## Technical details

> **Note:** The best way to learn will be by doing! Consider checking out the notebook. This is a quick summary that might answer questions you have.

A **socket** is an endpoint for two processes to talk to one another. There are two main kinds of sockets: [Unix Domain Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), which are used in interprocess communication, and [Network Sockets](https://en.wikipedia.org/wiki/Network_socket) (TCP and UDP), on top of which more complicated protocols like HTTP are built. These sockets all operate under the well-known [Berkley Socket](https://en.wikipedia.org/wiki/Berkeley_sockets) (aka POSIX Socket) API.

So, a person who knows how to use Network Sockets will know 99% of what they need to know for Domain Sockets! A very useful skill, as they show up in all sorts of networking.

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




## A note on system design

The reason for writing this guide is to provide some 
