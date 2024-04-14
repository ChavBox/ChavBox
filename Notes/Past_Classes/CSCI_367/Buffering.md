### Output port queuing
- Buffering required when datagrams arrive from fabric faster than link transmission rate. Drop policy: which datagrams to drop if no free buffers?
- Scheduling discipline chooses among queued datagrams for transmission, no priority, net neutrailty
	- tail drop: drop arriving packets
	- priority drop:

Rule of thumb: average buffering equal to "typical RTT" times link capacity C
- C = 10 Gbps link: 2.5G bit buffer
More recent recommendation: with N flows, buffering equal to RTT/C\*sqrt(N)
#### Too much buffering can increase delays (particularly in home routers)
- long RTTs: por performance for real-time apps, sluggish TCP responce
- recall delay-based congestion control: "keep bottleneck link just full enough (busy) but no fuller"

#### Packet Scheduling
Priority Scheduling:
- Arriving traffic classified, queued by class
	- any header fields can be used for classification

Round Robin:
- Arriving traffic classified, queued by class
	- any header fields can be used for classification
- server cyclically, repeatedly scans class queues, sending one complete packet from each class (if available) in turn. 