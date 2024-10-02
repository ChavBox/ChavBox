Assume each page/frame are 100 bytes
Assume the following byte address requests, left to write base 10
0110    1206    0613    0697    1206    1211    0614

- Because OS doesn't know ahead of time order of requests, it cannot reorder them

## FIFO Page Replacement
10   06   06   14   06   11   12

Pages in memory in sequence:

| Time | 1   |     | 2   |     | 3   |     | 4   |     | 5   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | 10  |     | 10  |     | 10  |     | 11  |     | 11  |
|      |     | ->  | 06  | ->  | 06  | ->  | 06  | ->  | 12  |
|      |     |     |     |     | 14  |     | 14  |     | 14  |

1 2 3 4 1 2 5 1 2 3 4 5

| 1   | 1   | 1   | 4   | 4   | 4   | 5   | 5   | 5   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2   | 2   | 2   | 1   | 1   | 1   | 3   | 3   |
|     |     | 3   | 3   | 3   | 2   | 2   | 2   | 4   |
1 2 3 4 1 2 5 1 2 3 4 5

| Mem Request | 1   | 2   | 3   | 4   | 1   | 2   | 5   | 1   | 2   | 3   | 4   | 5   |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fault?      | Y   | Y   | Y   | Y   | N   | N   | Y   | Y   | Y   | Y   | Y   | Y   |
|             | 1   | 1   | 1   | 1   | 1   | 1   | 5   | 5   | 5   | 5   | 4   | 4   |
|             |     | 2   | 2   | 2   | 2   | 2   | 2   | 1   | 1   | 1   | 1   | 1   |
|             |     |     | 3   | 3   | 3   | 3   | 3   | 3   | 2   | 2   | 2   | 5   |
|             |     |     |     | 4   | 4   | 4   | 4   | 4   | 4   | 3   | 3   | 3   |

Faults:
- 3 Frames: 9 page faults
- 4 Frames: 10 page faults

### Copy on Write

	Two processes relying on the same pages in physical memory, (fork causes)
	Goal: 
##### When should the OS create multiple copies vs a single shared copy?
- If a process writes to a physical memory location that is in use by another process, you copy on write, creating a new page in physical memory. 


### Optimal Replacement Approach
- Replace the page that will not be needed for the longest period of time into the future.
##### Implementation Difficulty
	Requires information about the future (impossible) so:
###### Least Recently Used (LRU) Page Replacement
	evict the page in memory that has not been used in the longest period of time
- Keep counter for each page in memory (recording time last used)
- When a page is refreshed, move it to TOP of a stack, the least recently used page would be at the bottom of the stack
How much info/what data structure are needed for LRU?
- Common architecture support provides a single <u>reference bit</u>, set to zero when the page is swapped in, set to 1 once referenced or written to. 
- Retain the reference bit, but also a small (8 bit) <u>history register</u> for each page.
- At regular intervals, "push" the reference bit into the highest-order bit of the history register.
	- Reference bit and history register init to 0
	- At a regular time interval, e.g. t=64 take a snapshot of reference bits
	- Push reference bits onto highest order bit of history register
## Approximation: history register
## Approximation: second chance
- The dirty bit is 1 if a process has written to memory but not the hard drive
- The reference bit signals if the frame has been used


dirty, reference

| Best Choice | Worst Choice |
| :---------: | :----------: |
|    0, 0     |     1, 1     |

Best Evict Choice:
- 0, 0
Worst:
- 1, 1
