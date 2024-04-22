	basic unit of CPU utilization

Benefits:
- Responsiveness
- Resource Scaling
- Economy
- Scalability

Challenges:
- Identifying tasks
- Balance
- Data splitting
- Data dependency 

### Parallel Execution
	Multiple CPU's or cores so that more than one process can do work in the 
	same instance

### Concurrent Execution
	Permits multiple tasks to be making progress at any one time. 
	(concurrent execution on a single core computer is possible)

#### Many to One
	Multiple threads mapped to a single kernel thread that controls them

Con:
- If any of the threads block the the entire process will.
#### One to Many
	Multiple threads with each thread being mapped to a unique kernel thread

### Many to Many
	Many user threads are mapped to a smaller or equal number of kernel threads

Pro/Con:
- At the user level, multiple threads are created, and it is up to the OS to schedule/orchestrate/map each of them to a kernel thread. 


Number of histories with threads that have same # of instructions
m = number of threads
n = number of instructions
# $\frac{(mn)!}{(n!)^m}$ 

### Concurrency vs Parallel
- On a single CPU concurrency is possible but parallel is not

### Thread Cancelation

Asynchronous Cancellation:
- A thread immediately terminates the target thread.
- Potentiolly Problematic:
	- Thread 1 is target for termination, and it is in the process of writing to the buffer.
Deferred Cancellation:
- The target thread periodically "checks in" to find out if it should be terminated; if so, it does so in an oderly fashion. 
- A flag is set if a given thread is writing to a buffer, to prevent from being killed while it is writing. 


### Synchronization

Entry Section: Implement rules to monitor critical section so that it is performed atomically. s
Critical Region:
- A region of code for which acces is controlled and/or coordinated by multiple processes.

Exit Section: we want to write code which informs "others"

A solution to the critical section problem must satisfy 3 criteria
1. Mutual exclusion
	- if a process is executing its critical section, no other process can be executing its critical section
2. Progress
	- If no process is executing and some process wants to enter its critical section, then only the processes NOT executing code in their other sections can decide who enters
3. Bounded Waiting: 
	- There must be a limit on the number of times that ANOTHER  process is allowed to enter its critical seciton after a processs has made a request to enter its critical section.


__Peterson's Solution:__
```
do{
	flag[i] = true;
	turn = j;
	while (flag[j] && turn == j) {};
	//CRITICAL SECTION
	flag[i] = false
	//other stuff (non-critical)
} while (true);
```

### Mutex
Mutual exclusion: allows the app programmer to solvre a critical section problem

```
do{
	//aquire lock
	//CRITICAL SECTION
	// release lock
	// other stuff (remainder)
} while (true);


acquire(){
	while(!available){};
	available = false;
}

release(){}
```

### Semaphores
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

x`