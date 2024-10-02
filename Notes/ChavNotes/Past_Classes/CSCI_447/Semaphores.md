	A semaphore is a data structure that permits threads to coordinate among 
	each other and specify which thread(s) wait and which threads execute. 
	Invented by Edsger Dijkstra (for CS applications).
- Serialization: Event A must happen before Event B
- Mutual Exclusion: Events A and B must NOT happen at the same time.
- Concurrent: 

Contains only a single non-negative integer as a datum
The integer can be initialized to any non-negative value, but once declared and set, it is modified only by several methods (there are no direct setter and getter methods)
1. Increment (V)
	- If increment occurs, an <u>already</u> waiting thread is unblocked. (waking)
2. Decrement (P)
	- If decrement would result in the datum being negative, then the thread that issued the decrement will be blocked and will not continue until ANOTHER thread increments the semaphore. 

###### Deadlock
	Two threads locked into spots where semaphores both try to decrement while 
	the semaphore value is already zero. Both threads freeze and cannot proceed.
