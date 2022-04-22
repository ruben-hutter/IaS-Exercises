# Task 1 - Routing - Are We There Yet?! AWTY?! ...
## Basic Setup

We implemented for the basic setup a *peer* and a *control* node.
**Peer**:
The *peer* implementation is divided in multiple files, located in the *peer* folder. There is a *protocol* that defines different message types that are correctly managed by the peer, *routing* is responsible to manage the routing table and to save the ip addresses of the neighbour nodes, *sender* establishes a new connection with the correct receiver node and sends the desired message to it, and *peer* is the "main programm" that listens to messages and parse them correctly.

**Control**:
The *control* is similarly implemented, also in his folder. There is again a *protocol* for the possible messages that are managed, *commands* defines the possible commands to enter in the *cli*, that is the "main programm", were you can enter the different commands, started by *control*.