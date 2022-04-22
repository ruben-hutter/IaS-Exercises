# Task 1 - Routing - Are We There Yet?! AWTY?! ...
## Basic Setup

**Peer**:
We implemented for the basic setup a *peer* and a *control* node.
The *peer* implementation is divided in multiple files, located in the *peer* folder. There is a *protocol* that defines different message types that are correctly managed by the peer, *routing* is responsible to manage the routing table and to save the ip addresses of the neighbour nodes, *sender* establishes a new connection with the correct receiver node and sends the desired message to it, and *peer* is the "main programm" that listens to messages and parse them correctly.