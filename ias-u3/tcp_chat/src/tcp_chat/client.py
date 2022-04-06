# code for client goes here
''' This module provides the functionality to listen for strings received on a tcp port and print it to CLI.

Requirements to module:
- Two peers can communicate directly with each other (i.e. without an intermediate
server, peer-to-peer respectively).

- Hint: With server we mean a central process that manages and sometimes forwards mes-
sages. A listener-”server” and a requesting ”client” is still required to establish communi-
cation.

- The IP address and port of the communication partner are passed as command line
arguments.

- Chat messages are plain UTF-8 strings (default strings).

- For chat-message input (and output), use CLI (standard IO).

- Fast message display (own and received):
To display messages immediately, use select() for C, for Python3 and for C++.
This call can be used with sockets and CLI In-/Output.

- Do NOT use multiprocessing, asyncio or something alike. Such methods remove any
guaranty of ordered input/output (order preservation).'''

import socket
from threading import Thread

class Client:

