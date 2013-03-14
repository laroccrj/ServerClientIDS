ServerClientIDS
===============

A simple script to have collaboration between IDSs on different machines

This script is being made for a competition. There is not much error checking because we will need to copy this off a piece of paper onto a computer during the competition.

How it works:

Clients connect to the server with the password the server was initialized with.
Clients then bind to a port and act as a honey pot.
When someone tries to connect to the port, the client sends the ip to the server.
The server then relays the ip to all the clients.
The clients then block that ip with iptables.
