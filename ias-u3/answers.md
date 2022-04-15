# IaS - Exercise sheet 3

## Task 1 - TCP Chat
The idea is to have a driver code (*tcp_chat_launcher.py*) that allows to start the application as a server or client, depending on the number of arguments given. For the server, only the port number is needed, for the client also the server's ip address is needed.

In the tcp_chat package ([TestPyPi](https://test.pypi.org/project/tcp-chat-tobi-ruben/)) we have two methods, one for initializing a server peer, which listens for a client initially, and the other for the client, which connects to the listening peer.
If the *launch_client* method doesn't receive the correct parameters and the socket, trying to connect to the server, throws an error, it would be catched and a server would be launched instead.
Once the connection is established the *run_chat* method is responsible for updating sockets (with `select()`), request data from socket and check if connection is still there (otherwise close connection), receive data and send data if something is typed in the standard input.

To close the connection, enter `:q` as a message.

## Task 2 - UDP Chat

