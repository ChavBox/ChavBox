	Metrics of a process that we want to minimize/maximize
	Metrics of a computer's component (CPU for example) that we want to 
	minimize/maximize
### Criteria for scheduling

- CPU utilization: keep cpu busy
- Throughput: number of processes completed in x time
- Turnaround: from the time of submission to time of completion, including waiting
- Waiting time: the time spend in waiting/ready queues, not the I/O queues
- Response time: time from submission to the time when the "first" usable data/output is produced

### Different Approaches:

__Shortest Job First (SJF):__
- the process with the shortest burst time goes first
- advantages: minimizes average wait time
- disadvantages: large burst time process may be high priority but would go last

__Priority Scheduling:__
- Internally Defined Priority
- Externally Defined Priority
- Process with the highest priority goes next

### Preemption
	The ability of an OS to kick something out of a CPU


## Real Time Scheduling

	Time Criticial Processes (all units are ms)
Periodic: occuring at a constant interval, or period (p)
Processing Time: time needed to execute (burst time ,t)
Deadline: time by which a process must finish (d)

$0 \leq t \leq d \leq p$ 

If the above relationship is not met a cpu should not allow a process to execute

The period is the amount of time that a process is allowed to begin and finish executing.

### Rate Monotonic Scheduling (RMS)
	p1: p: 50ms, t: 20ms, d:once each period
	p2: p: 100ms, t: 35ms, d:once each period

CPU Utilization:  $\frac{t}{p}$ 
P1: 0.4
P2: 0.35
P1+P2 = 0.75
