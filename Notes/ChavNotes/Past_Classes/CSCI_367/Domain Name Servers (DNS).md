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
				- value is name of SMTP mail server associated with name]
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
