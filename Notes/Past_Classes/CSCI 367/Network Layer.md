## IP: the internet protocol
IP address: 32-bit identifier associated with each host or router interface. 

Interface: either input or the output that allow you to connect to a network. 
connection between host/router and physical link
- router's typically have multiple interfaces
- host typically has one or two interfaces (WiFi or Ethernet)
#### IP Datagam format
                32-bits
+----------------------------------------------+
| ver | head. len | type of service | length        |
| 16-bit identifier | flags | fragment offset        |
| time to live | upper layer | header checksum |
|                        source IP address                     | (32 bit)
|                     destination IP address                 | (32 bit)
|                         options (if any)                         |
|         payload data (variable length, typically  |
|                  a TCP or UDP segment)                  |
\+----------------------------------------------+

Maximum length 64K bytes
Typically 1500 bytes. 

#### IP Addressing
Interfaces are connected with switches or base stations

Subnets
- A device interfaces that can physically reach each other without passing through an intervening router
IP addresses have structure:
- Subnet part: devices in same subnet have common high order bits
- Host part: remaining low order bits

#### IPv6
__Datagram format__
32-bits wide
flow label: identify datagrams in same "flow" (concept of flow not well defined)
priority: identify priority among datagrams in flow

Transition from IPv4 to IPv6
- Tunneling: IPv6 datagram carried as payload in IPv4 datagram among IPv4 routers (packet within a packet)
- tunneling used extensively in other contexts (4G/5G)

If IPv4 network are connecting two IPv6 routers we need to use tunneling with IPv4/IPv6 router to send the IPv6 data over the IPv4 network, and then the other IPv4/IPv6 router can extract the IPv6 datagram.


##### Generalized Forwarding
- Match+action
	- match bits in arriving packet, take action
- OpenFlow: match+action in action
- many haeder fields can determine action
- many action possible: drop/copy/etc.

Flow table abstraction
- flow: defined by header field values
- generalized forwarding: simple packet-handling rules
	- match: pattern values in packet header fields
	- actions: for matched packet: drop, forward, modify, matched packet or send matched packet to controller
	- priority: disambiguate overlapping patterns
	- counters: \#bytes and \#packets
	- 