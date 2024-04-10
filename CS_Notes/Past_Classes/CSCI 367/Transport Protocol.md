TCP: Transmission control protocol
- reliable, in-order delivery
- congestion control
- flow control
- connection setup
UDP: User datagram protocol
- unreliable, unordered delivery
- only cares about destination port number
- no-frills extension of "best-effort" IP

Services not available:
- Delay guarantees
- Bandwidth guarantees


### Multiplexing/Demultiplexing

Multiplexing as sender:
- handle data from multiple sockets, add transport header (later used for demultiplexing)
Demultiplexing as receiver:
- use header info to deliver received segments to correct socket

__How demultiplexing works__
- Host receives IP datagrams
	- each datagram carries one transport-layer segment
	- each segment has source, destination port number
- Host uses IP addresses and port numbers to direct segment to appropriate socket

Connection-less demultiplexing
- when creating datagram to send into UDP socket, must specify
	- destination IP address
	- destination port #
- demux: receiver only destination IP and port to direct segment to appropriate socket

Conncetion-oriented demultiplexing
- TCP socket identified by 4-tuple:
	- source IP address
	- source port number
	- dest IP address
	- dest port Number
- dmux: receiver uses *all four values (4-tuple)* to direct segment to appropriate socket