# Quote Of TheDay
Quote of The Day Program. Really simple, non-formated results and console program. This program is inpired in the Quote of The Day Protocol, but, in this case the program doesn't make usage of any protocol, just some harcoded quotes in a database table. The purpose of this program is to test some basic Python language basic concepts.

## What is a Quote of The Day Program?
As defined in [Gokberk Yaltirakli - Quote of the Day (QOTD) Protocol](https://www.gkbrk.com/wiki/qotd_protocol/) a Quote of the Day is: 
> (...) a simple protocol that is used to deliver daily quotes. Although its usage is almost nonexistent these days, there are still a few public servers. The protocol is defined by RFC865. According to the RFC, a QOTD server is run on port 17 for TCP and UDP connections. It is an excellent protocol to learn the socket API and to write your first server.

## Protocol Details 
The content of this section is owned and is published on [Gokberk Yaltirakli - Quote of the Day (QOTD) Protocol](https://www.gkbrk.com/wiki/qotd_protocol/). 

>The RFC is quite short, actually it is just half a page. Therefore, it is highly recommended to read it. But the protocol details are also written below in an easy-to-understand manner.
> ### Recommendations
> The RFC recommends that;
> * The quotes should be limited to the ASCII printable characters, spaces and newlines.
> * They should be less than 512 characters.

> Since the protocol is only used to send quotes to terminals, these aren’t hard requirements. But a server should still follow these recommendations in order to be compatible with the other servers and clients.
> Despite the name being Quote of the Day, a server does not have to serve daily quotes. It can change the quote at any interval or send random quotes at each connection.

> ### TCP Connections

> When a QOTD server gets a connection, it sends a quote and closes the connection, discarding any received data. Basically, a server should do the following

> Listen to connections on port 17.
> 1. Accept a connection.
> 2. Choose a random quote.
> 3. Send the quote to the client.
> 4. Close the connection.

> ### UDP Connections

> A UDP server is a bit different from a TCP one. Since UDP has no concept of connections, a server just sends the quote after getting a UDP datagram.

> * Listen to UDP datagrams on port 17.
> * When you get a UDP packet:
>    * Discard any data in the packet.
>    * Send a UDP datagram containing the quote back to the client.

### UDP Connections
The content of this section is owned and is published on [Gokberk Yaltirakli - Quote of the Day (QOTD) Protocol](https://www.gkbrk.com/wiki/qotd_protocol/). 
> Despite being almost extinct, the following servers have been reported to work.
> | Server Address	| TCP Port	| UDP Port |
> | -- | --- | --- |
> |djxmmx.net	| 17	| 17 |
> |alpha.mike-r.com	| 17	| 17 |
> |cygnus-x.net	| 17	| 17 |

## Code Examples in Pyhton
The content of this section is owned and is published on [Gokberk Yaltirakli - Quote of the Day (QOTD) Protocol](https://www.gkbrk.com/wiki/qotd_protocol/). 
> Since the protocol is very simple and completely one-way, it is easy to write your own QOTD server and QOTD client.
>Below is the code for a simple, single-threaded QOTD server written in Python. On each connection, it picks a random quote from the quotes list and sends it to the client. It should be an easy exercise to read the quotes from a file or a database.
### QOTD Server
```
>import socket
import random

quotes = [
    "Never do today what you can do tomorrow",
    "Nobody lies on the internet",
    "The cake is a lie"
]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 17)) # Bind to port 17
server.listen(5)

while True:
    sock, addr = server.accept()
    quote = random.choice(quotes)
    sock.send(f"{quote}\n")
    sock.close()
```
# QOTD Client
```
import socket

addr = ("example.com", 17) # Change server address

conn = socket.create_connection(addr)
quote = conn.recv(4096) # Read up to 4096 bytes

print(quote.decode("utf-8"))
```

 ## Technologies
 * [Python](https://www.python.org);
 * [MySQL Databse](https://www.mysql.com);
 
 
