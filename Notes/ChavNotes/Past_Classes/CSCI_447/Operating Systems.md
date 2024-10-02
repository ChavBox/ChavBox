OS: provides 

An OS is "just another program" or set of programs.
- Source code in linux lives in /usr/include/...

### OS Structure
- Multiprogramming: 
	- goal: increases CPU utilization by ensuring that the CUP hsa always something to execute (code to run)
- Several jobs are kept in memory
- Memory Hierarchy ... not all jobs can be "in" memory at one time...
- Hence the use of a job pool
- Multiple jobs kept in memory does not mean they're all running at the same time
- OS picks one jobs in memory to execute
- When a job is waiting for an I/O operation, the OS switches to another job
### OS Services
- Program Execution
	- load program into memory and run it
- I/O operations
	- send data to screen, send data to speaker, send data to/from a file
- File systems
	- create a file, delete a file, add to a file, etc. 
- Communications
	- via shared memory or via message (packet) passing
- Error Detection

- Resource Allocation
	- Scheduling algorithms
- Accounting
	- Which usr/process uses how much of a specific resource
	- time, space, fair access to a shared resource
- Protection and Security


Paramaters are passed to the OS 
- via registers
- save parameters in block or table (in memory) and pass, via the registers, the __address__ of the block
- pushed onto the stack

### System Calls
- Process Control
- File Management
- Device Management
- Information Management
- Communications
