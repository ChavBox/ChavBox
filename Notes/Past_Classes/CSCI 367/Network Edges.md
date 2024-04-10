### Application Layer
__Apps__
	- social networking
	- web
	- text msg
	- e-mail
	- multi-user network games
	- streaming stored video
	- P2P file sharing
	- voice over IP
	- real-time video conferencing
	- Internet search
	- remote login
__Communication models__
- Client-server model:
	- Server
		- always-on host
		- permanent IP address
		- often in data centers, for scaling
	- Clients:
		- contact
- P2P model:
	- no always-on server
	- arbitrary end systems directly communicate
	- peers request service in return to other peers

- Process: program running within a host
	- within same host, two processes communicate using inter-proces communication (defined by OS)
	- processes in different hosts communicate by exchanging messages
	- client process: process that initiates communication
	- server process: process that waits to be contacted
__Sockets__
- Process sends/recieves messages to/from its socket
- socket analogous to dor
	- sending process shoves message out door
	- sending process relies on transport infrastructure on other side of door to deliver message to socket at receiving process
	- two sockets involved: one on each side
- To receive messages, process must have identifier
- Host device has unique 32-bit IP address
- Q: does IP address of host on which process runs suffice for identifying the process? 
	- A: no, many processes can be running on the same host
- identifier includes both IP address and port numbers associated with process on host
- example port numbers:
	- HTTP server: 80
	- mail server: 25
- to send HTTP message to cs.wwu.edu web server:
	- IP address: 128.119.245.12
	- port number: 80

__What's underneath it?__
TCP service:
- reliable transport between sending and receiving process
- flow control: sender won't cverwhelm receiver
- congestion control: throttle sender when network overloaded
- connection-oriented: setup required between client and server processes
UDP service:
- unreliable data transfer between sending and receiving process
- does not provide: reliability, flow control, gongestion control, timing, throughput guarantee, security, or connection setup

UDP and TCP have:
- no encryption
- cleartext passwords sent into socket

Transport Layer Security (TLS)
- provides encrypted TCP connections
- data integrity

### Protocols
- HTTP
- E-mail, SMTP, IMAP
### Application protocol: HTTP
__HTTP__: hypertext transfer protocol
- web application-layer protocol
- client/server model:
	- client: browser that requests, receives, and "displays" web objects
	- server: web server sens objects in responce to requests
- HTTP client initaites TCP connection to HTTP server
- HTTP server at host waiting for TCP connection, "accepts" connection, notifying client
- HTTP client sends HTTP request message into TCP connection

__Non-persistent HTTP__ 
- RTT: time for a small packet to travel from client to server and back
- HTTP response time:
	- one TRR to initiate TCP connection
	- one RTT for HTTP request an first few bytes of HTTP responce to return
	- object/file transmission time
	- 2RTT + file transmission time
- Issues:
	- requires 2 RTTs per object
	- OS overhead for each TCP connection
	- browsers often open multiple parallel lTCP connections to fetch referenced objects in parallel
__Persistent HTTP__ 
- Server leaves connection open after sending response
- subsquent HTTP messages between same client/server sent over open connection
- client sends requests as soon as it encounters a referenced object
- as little as one RTT for all the referenced objects (cutting responce time in half)
- two types of HTTP messages: request, responce
	- Request:
		- ASCII (human-readabl format)
		- request line(GET, POST, HEAD commands)
		- POST method:
			- web page often includes form input
			- user input sent from client to server in entity body of HTTP POST request message
		- HEAD method:
			- request headers (only) that would be returned if specified URL were requested with an HTTP GET method
		- GET method (for sending data to server):
			- include user data in URL field of HTTP GET request message (following a '?')
		- PUT method:
			- uploads new file (object to server)
			- completely replaces file that exists at specified URL with content in entity body of POST HTTP request message
	- Responce:
		- status line(protocol status code status phase)
		- status code appears in 1st line in server-to-client responce message
		- example codes:
			- 200 OK
				- request success
			- 404 Not Found
				- requested document not found on this server
__Maintaining user/server state: cookies__ 
Recall: HTTP GET/response interaction is stateless
- no notion of multi-step exchanges of HTTP messages to complete a Web "Transaction"
- cookies are used to remember user data such as authentication, their shopping cart, and other user information
- example:
	- sent http request, get reply with data of webpage
	- fetch ad from AdX.com (or some other third party ad vendor)
	- first party cookie generated from visited website
	- once ads are requested, the ad vendor would store another cookie in your browser
	- multiple cookies from many sources from one webpage visit
### Web caches
Goal: satisfy client requests without involving origin server
- user configures browser to point to a (local) Web cache
- browser sends all HTTP requests to cache
	- _if_ object in cache: cache returns object to client
	- _else_ cache requests object from origin server, caches received object, then returns object to client

Calculating access link utilization, end-end delay with cache:
- suppose cache hit rate of 0.4
- 40% requests served by cache, with low (msec) delay
- 60% requests satisfied at origin
	- rate to browsers over access link
		- 0.6 * 1.5 Mbps = 0.9 Mbps
		- access link utilization = 0.9/1.54 = 0.58 means low (msec) queueing delay at access link
- average end-end delay:
	- 0.6 * (delay from origin servers) + 0.4 * (delay when satisfied at cache) = 0.6(2.01) + 0.4(~msecs) = ~ 1.2 secs

Browser caching: Conditional GET
- Goal: don't send object if browser has up-to-date cached version
	- no object transmission delay (or use of network resources)
- client: specify date of browser-cached copy in HTTP request
	- __If-modified-since: \<date\>__
- server: response contains no object if browser-cached copy is up-to-date:
		- __HTTP/1.0 304 Not Modified__

### DNS: Domain Name System
people: many identifiers:
- SSN, name, passport #, etc
Internet hosts, routers:
- IP address (32 bit) - used for addressing datagrams
- "name", e.g., cs.umass.edu - used by humans
DNS:
- distributed database implemented in hierarchy of many name servers
- application-layer protocol: hosts, DNS servers communicate to resolve names (address/name translation)
	- note: core Internet function, implemented as application-layer protocol
- Services:
	- hostname-to-IP-address translation
	- host aliasing
		- canonical, alias names
	- mail server aliasing
	- load distribution
		- replicated Web servers: many IP addresses correspond to one name
- Humongous distributed database:
	- ~billion records, each sample

DNS: a distributed, hierarchical database

\[Root\] Root DNS Servers:
- \[Top Level Domain]
- .com dns servers
- .org DNS servers
- .edu DNS servers
	- \[Authoritative]
	- yahoo.com DNS servers
	- amazon.com DNS servers
	- pbs.org DNS servers
	- etc

Example:
	client wants IP address for www.amazon.com
	1. client queries root server to find .com DNS server
	2. client queries .com DNS server to get amazon.com DNS server
	3. client queries amazon.com DNS server to get IP address for www.amazon.com

DNS name resolution: 
Iterated query (used in nearly every scenario getting IP address)
- contacted server replies with name of server to contact
- "I don't know this name, but ask this server"
Recursive query
- Puts burden of name resolution on contacted name server
- heavy load at upper levels of hierarchy?

DNS Caching
- once (any) name server learns mapping, it caches mapping, and immediately returns a cached mapping in response to a query
	- caching improves response time
	- cache entries timeout (disappear) after some time (TTL)
	- TLD servers typically cached in local name servers

DNS Records
- DNS: distributed database storing resource records (RR)
	- format: (name, value, type, ttl)
		- types:
			- A
				- name is hostname
				- value is IP address
			- CNAME
				- name is alias name for some "canonical" (the real) name
				- www.ibm.com is really servereast.backup2.ibm.com
				- value is canonical name
			- NS
				- name is domain (e.g. foo.com)
				- value is hostname of authoritative name server for this domain
			- MX
				- value is name of SMTP mail server associated with name