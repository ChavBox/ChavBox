### Definitions
- Host Nodes (hosts):
	- Called End systems.
	- Run apps.
	- Used to be computers, now include TVs, smart-phones, washing machines, etc.
	- bit = 0 or 1
	- bps = bits per second
	- kbps = 1000 bits per second
	- mbps = 1,0000,000 bits per second

- Routers:
	- Forward network packets (information).
	- Make it possible to connect one network to another.
### How do hosts connect to the net?
[[Types of Connections]]

***HTTP/2

Objects are divided into frames, frame transmission is interleaved so one large object doesn't clog entire webpage

***HTTP/3

Adds security, per object error- and congestion-control (more pipelining) over UDP
- more on HTTP/3 in transport layer

Transport Layer:
- communication between processes
- relies on, enhances, network layer services
Network layer:
- comunication between hosts
- actions:
	- 

Household analogy:
- 12 kids in Ann's house sending letters to 12 kids in Bill's house
	- hosts = houses
	- processes = kids
	- app messages = letters in envelopes
	- __transport protocol__ = ann and bill who demux to in-house siblings
	- __network-layer protocol__ = postal service