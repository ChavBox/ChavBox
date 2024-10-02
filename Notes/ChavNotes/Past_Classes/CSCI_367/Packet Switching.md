This is the dominant/relavant way of using internet.
- End-to-end or (host-to-host) communications split into data chunks or ***packets***.
- Each packet uses full link bandwidth.
- Network users share resources.
	- Resources used as needed (no reservation).
	- Aggregate demand may exceed available resources.
	- Congestion may occur.
		- Wait for resources to become available.
		- If too much congestion, packets may be lost.
- Packets move one hop at a time
	- Store and forwards
	- Nodes wait to recieve entire packet before forwarding it

### Statistical Multiplexing
- Packets arrive with no fixed timing pattern
- Bandwidth share on demand
- Different from FDM/TDM, for which resource are guaranteed for entire "call time".

### A router
Responsibilities:
- Forwarding (aka switching):
	- local action: move arriving packets from router's input link to appropriate router output link
	- smaller scale than routing
	- router has an internal table to help with connecting header value with output link
- Routing:
	- global action: determine source-destination paths taken by backets
	- how to best send packages along the correct routes
	- like using a map to figure out how to get from point A to point B
	- routing algorithms

Packet Transmission Delay: takes L/R seconds to transmit (push out) L-bit packet into link at R bps
- Packet delay: packets queue in router buffers, waiting in turn for transmission
- Packet loss: router memory to hold queued packest fills up, router discards newly received packet. 
Store and Forward: entire packet must arrive at router before it can be transmitted on next link

#### Delays
D_processing (proc): nodal processing
- check bit errors
- determine output link
- typically < microseconds
D<sub>queue</sub>: queuing delay
- time waiting at output link for transmission
- depends on congestion level of router
D<sub>transmission</sub> (trans):
- L: packet length (bits)
- R: link transmission rate (bps)
- d<sub>trans</sub> = L/R
D<sub>propagation</sub> (prop):
- d: length of physical link
- s: propagation speed (~2x10<sup>8</sup> m/s)
- d<sub>prop</sub> = d/s

Example:
NYC to London (5500km)
prop speed ~200,000km/s

15Mbps link bandwidth
1500-byte packet (1 byte = 8 bits)

prop = 5500/200,000 = 27.5 ms
trans = 8 * 1500/15E6 = 0.8 ms

total delay ~ 28.3ms
___
Calculating traffic intensity:

a: average packet arrival rate
L: packet length (bits)
R: link bandwidth (bit transmission rate)

(L * a)/R

Throughput: rate (bits/time unit) at which bits are being sent from sender to receiver)
- instantaneous: rate at given point in time
- average: rate over longer period of time
- bottleneck link: link on end-end path that constrains end-end throughput
- speed is restricted by the slowest link