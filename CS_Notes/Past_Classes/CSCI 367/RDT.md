### rdt2.1


### rdt2.2
- same functionality as rdt2.1, using ACKs only
- instead of NAK, receiver sends ACK for last pkt received OK
	- receiver must explicitly include seq # of pkt being ACKed
- duplicate ACK at sender results in same action as NAK

- #### sender: receiver fragments
-->\[wait for call 0 from above]
- rdt_send(data)/sendpkt=make_pkt(0, data, checksum), udt_send(sendpkt)