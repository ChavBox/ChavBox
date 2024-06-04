Output, to the command line:
- Contents of Inverted Page Table
	- row, pid, p, d, r
		- p: page/frame in memory
		- r: reference bit
		- d: dirty bit
- Number of page faults that involve only reading
- Number of page faults that require writing (to the hard drive) and reading in the page being swapped in
- Total number of page faults
- Total percentage of page faults that require writing (to the HD), and reading in the page being swapped in.
###### Least Recently Used (LRU) Page Replacement
	evict the page in memory that has not been used in the longest period of time
- Keep counter for each page in memory (recording time last used)
- When a page is refreshed, move it to TOP of a stack, the least recently used page would be at the bottom of the stack

#### Implement Inverted Page Table
- There can be at most 64 processes in the page table at any time. 
#### Implement Random Evict
#### Implement Optimized Evict

#### Mem-Sim.o
	integer input n -> n pid's with address request w/ read and/or write
	For testing make my own mem-sim so I can fiddle with stuff
1000 -> array{pid, address, R, W}\[1000]
