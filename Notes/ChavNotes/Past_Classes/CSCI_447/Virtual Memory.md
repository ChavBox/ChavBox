### Virtual Addresses
The address generated by a CPU is called a <u>logical</u> address, and most often referred to as  <u>virtual address</u>.

# MMU
	Memory Management Unit: responsible for ampping between a virtual address and physical one.

T/F: In order for a process to be executed, it must be "in" memory. | False
- Not all processes (PCB's) can fit into L1 cache, L2 cache, memory, etc at the same time

### Memory Protection
Cpu (logical address) ->  (< limit register) -> 
logical address + relocation register -> 
physical address in memory

Contiguous memory allocation is assumed here, but is not always used. 

#### Segmentation
- Logical Address is made of two parts (tuple) \<segment num, offset> \<S, D>
- A segment table holds all of the segment IDs and their limits
- Segment number is an index into the segment table
- External fragmentation is when memory is fragmented in between segments, so there aren't large enough holes
	- One solution is to unfragment memory
- Internal fragmentation is when there is bad usage of individual rows within a certain frame/range of addresses
- Compaction is merging the existing holes into one large hole
#### Paging
- Physical memory is broken into frames, or chunks. 
- The logical memory space is broken into blocks of the same size called pages.
- Each address generated has a p (offset/index) into a page table
- The base address at a specific index in the page table identifies the frame where the page is located in memory
- The d, or offset in combination with the frame, identifies where in a frame the exact requested address is located. 
- Size of page == size of frame
- Page sizes come in powers of 2
- Size of logical address space: $2^m$
- Size of page: $2^n$
- Use the m-n highest bits of logical addresses to index into page table
- Map to frame in physical memory
- The n lower bits of the logical addres designate the index into the frame


## Page Table

| frame? | invalid-bit |     |
| :----: | :---------: | :-: |
|        |      0      |     |

#### Segment Table
- Two columns - base and limit, the index in the table refers to which segment
- P is the page (index in the table)
- D is the offset for the frame
##### Two important ramifications
- The logical address space is totally seperate from the physical address space the datda page can residue in any frame
- A process can have a high (32 bit for example) logical address space, even though less than $2^{32}$ bytes are available.

#### Translation Look-aside Buffer TLB
	high speed associative memory (register speed)
- TLB has a page and a frame column

Two processes may share a page table when they are the same executable

#### Inverted Page Table
	a single page table regardless of how many processes there are
- three tuple (pid, p, d) ?? (2-tuple: pid, p)
	- pid: process ID
	- p: index into table
	- d: offset into frame
- when searching for a <pid, p> you return the index of that row in the page table
- Size = as many frames you have in physical memory

# Virtual Memory
Why?
- Program is too large for physical memory
- We don't want infrequently used error handling code to occupy physical memory
- Data structs are often declared to be large, but not filled
- Unused Routines
- Different portions of a program are used at different times

Goal: Execute a program that is only partially in memory
Benifits:
- Not hogging main memory space
- Less I/O required to swap user programs
## HOW?
Just before a page is needed, the OS will swap it into the Physical Memory from the Secondary Storage Device (Hard Drive/SSD)

- Valid/invalid bit also refers to if the frame is in physical memory
- If a requested address is invalid, the OS traps the address and throws a page fault
	- If the requested addres is in the process's logical address space, the OS terminates the process

### Memory Speed
Miliseconds (HD/Memory)
Microseconds (Cache/Register)
Nanoseconds (ALU)
# Swapping from HD to Physical Memory
#### Effective access time
	2 processes A, B
- Probability of A to page <u>fault</u> (p) = 0.4
- Probability of B to page <u>fault</u> (p) = 0.3 (Probability to page hit 1-p)
- Time cost of page fault (fault): 5 miliseconds
- Time cost of memroy access (ma): 300 nanoseconds
- How much more is the effective access time of process A vs process B?
### Effective Access Time = $(1-p)ma + p(fault)$ 

## [[Page Replacement]]