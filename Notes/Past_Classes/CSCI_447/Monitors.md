- Provide a more object-oriented, abstract style approach to mutex and 
   synchronization
- More structure than a semaphore
- A data abstraction mechanism
- Can be implemented multiple ways
- Access to monitor variables is only through interface
- Mutual exclusion of all monitor procedures is implicit (procedures in the same monitor cannot be executed concurrently)
- Conditions synchrnozation...
- Active processes (threads running concurrently) interact by calling procedures in the same monitor.
- The monitors are referred to as passive.
- A monitor is used to group together the representation and implementation of a shared resource.
- In different languages, they are created in different ways. 

__Active processes__ interact by calling procedures in the same monitor

```
monitor mName{

  queue mEntryQueue
  queue cvQueue 
  cond cv      // static condition variable
  
  empty(cv){
	// return true if empty
  }
  
  wait(cv){
    // a process blocks; it's ID is placed at rear of cv queue
  }
  
  signal(cv){
  
  }
  ...
}
```

### How monitors solve problems
	A monitor is called by an external process
	
	A proceedure is active if some process is executing a statement in the 
	monitor
	
	At most one instance of any one of a monitor's procedure may be active at 
	the same time.
	
	A single monitor can coordinate multiple processes, unlike a semaphore.

- Monitors will decide which process can execute a procedure via a queue.
- A condition variable is used to delay a process that cannot safely continue until the monitor's state satisfies some Boolean condition.
- wait ~ (semaphore decrement)
- signal ~ (semaphore increment)

__Signal__:
- scenario 1.1
	- T1:
		- p1: signal
		- p2: wait
	- T2: 
		- p1: wait
		- p2: goes
	- T3: 
		- p1: goes
		- p2: done
- scenario 2:
	- T1:
		- p1: signal
		- p2: wait
	- T2:
		- p1: goes
		- p2: wait
	- T3:
		- p1: done
		- p2: goes

If I signal, who goes next: me or someone else?

__Signal and Continue (SC):__ the signaler (process that called signal) contines, and the signaled (process that is awakened) executes at some later time.

__Signal and Wait (SW):__ the signaler waits until some later time and the signaled process executes immediately.

##### Process monitor call:
- are there other processes currently executing in monitor?
- are there other processes currently waiting to execute?
- when a processes issues:
	- signal: 
		- (SC): the awakened process goes to tail of entry queue
		- (SW):  
	- wait: it goes to the tail of the cv queue

