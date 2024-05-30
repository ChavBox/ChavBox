Multiple Processes, MMU/Memory Map, Physical Memory

If there are two processes, should
- each process be allocated 1/2 of the available frame?
	- pro: easy
	- con: only works if every process have the same memory requirements
- frames be allocated on an as-needed basis?
	- pro: more space is reserved for incoming processes
	- con: slower

Why is there a minimum number of frames that should be reserved for a process?
- A frame needs to be at least as large as the smallest OP-code in a processes instructions
- The minimum number of frames per process is defined by the architecture
- The __maximum__ number of frames possible for a process is the number of frames in memory.
###### As the # of frames allocated to each process decreases, <u>Overall page fault</u> increases.
###### When a page fault occurs, a process's instruction is restarted after the swap in, and the restarted instruction might need more pages than just the one that was brought in.

### Early days: Equal allocation
	for n processes, reserve m/n frames for each process (with any non-int remainder left over for a pool of processes)

### Proportional allocation
	Allocate frames based on a process's size
__If process $p_i$ needs $s_i$ amount of virtual memory:__

	
What is the size of needed space for all n processes?
-  $S=\Sigma^n_{i=0} S_i$ 
How many frames, $a_i$, should be allocated to a process?
- Conceptually: if the total amount of available frames is $m$, dole out for a process $i$ the amount of available frames that is equal to the ratio of the size of process $i$ to S.
- Concretely: $a_i = (s_i/S)*m$ 
Ex:
- $10_x$
- $25_y$
- $35z$
- $m = 100$
- $S = 70: (10+25+35)$
- $a_{10} = \frac{100}{70}$
- $a_{25} = \frac{250}{70}$
- $a_{35} = \frac{350}{70}$

### Thrashing
	Because processes come and go with various priorities, if a low prio process is allocated too few frames, suspend the process and evict all pages needed by the instructions of the process

Thrashing: when the CPU spends more time paging than executing (running) code

What causes thrashing?:
- If a process enters a "new" phase of execution, and needs more frames, which are taken away from other processes

As CPU utilization increases in respoinse to more processes being allowed "in", 

__How could we prevent (or minimize) thrashing?__
### Working Set Model
	Consider what pages a process has needed in the recent past, as an indicator of the pages it will need in the future. (Size is the most important property)

If $\Delta$ = 5, the working set at t = x are the past $\Delta$ frames needed.
- If only frame 2 & 3 are used in 5 requests, the working set would only be those two frames, not 5 unique frames. 
- Pages in the working set are considered active pages
- The working set is an approximation of a program's locality
- Accuracy of the working set depends on the selection of $\Delta$

If $\Delta$ is too small, important frames could be removed from physical memory when it is still needed soon.

If $\Delta$ is too large, the programs a long time ago may no longer be in memory and a large working set would take up unnecessary memory.

If Working Set (WS) Size (WSS) of process $i$ is $WSS_i$, then what is the total demand of the most active frames for n processes?
- $D = \Sigma_{i=1}^n WSS_i$ (demand of the most active frames)
- __If D is larger than the number of available frames thrasing will occur.
- If WSS is small, there will be many page faults
- If WSS is large, there will be few pages faults

Modern Computer System $\Delta = 5,000$ <-> $15,000$ 
