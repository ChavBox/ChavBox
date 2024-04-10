What is a process?
- Something being executed or needs resources

#### Required Components to Schedule Jobs
- The program file (exe) aka the 'text' section
- the activity currently executing, which includes the value of the program counter, and the values of the registers
- The memory image
	- text, data, heap, stack
		- heap: dynamically allocated
		- stack: temporary data

Process States:
- New: being created
- Running: being executed
- Waiting: for some event to occur
- Ready: process is waiting to be assigned a processor
- Terminated: finished executing

Transitions:
- Ready -> running
	- The OS determines which process goes next

### Process Control Block (PCB)
	A repository for information aboutr processes
- State
- Program Counter
- CPU Registers
- CPU Scheduling Info
- Memory Management Info
- Accounting Info
- I/O Status

If a process has an interrupt, the OS saves the status of the process into it's PCB and then choose a waiting process and load it's PCB, and resume execution. 

PCB's stored in __Ready Queue__
