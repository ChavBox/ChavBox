# Disk Scheduling
	Very important because since an HD is mechanical, it is very slow compared to ALU/registers

Cylinders on the disk are like rings, and are indexed starting from outside of disk going inwards, outer cylinder is #0, and the inner most is the max # of cylinders. 

We want to <u>minimize</u> the number of times the arms of the disk have to <u>stop their movement and go in the opposite direction.</u>

## Scheduling Algorithms
##### FCFS
	Retrieve the data in the order it is asked for
##### SSTF
	 Select the request with the shortest seek time from the current position
##### SCAN
	Full back and forth, reading during both swings
##### C-SCAN
	Full back and forth, reads on during one swing (C = circular)
##### LOOK 
	Proceed in direction at start, go to "maximum" request in that direction, then reverse, and perform reads as continuing towards maximum "other" direction.

# Example Questions
1. Assume the following page requests by process $i$ left to right \[Answers TBD]:
43   78   32 |  32   43 |  32   12   34 |  78   65   43   78 |  32   78 |
           $t_1$              $t_2$                    $t_3$                            $t_4$              $t_5$
Which of the following statements are true?
A \[True]. If a$t $t1$ the $\Delta$ for $i$'s working set is 3, then 32 is always in $i$'s working set up until time $t_2$
B \[False]. If at $t1$ the $\Delta$ for $i$'s working set is 2, then 32 is always in $i$'s working set up until t_3 
C \[True]. If at $t1$ the $\Delta$ for $i$'s working set is 4, then 32 or 78 is always in $i$'s working set up until $t_4$ 
D \[True]. If at $t1$ the $\Delta$ for $i$'s working set is 3, then 32 or 78 is always in $i$'s working set up until $t_4$ 
E \[True]. If at $t2$ the $\Delta$ for $i$'s working set is 5, then 78 appears most often in $i$'s working set up until $t_4$ 
F . If at $t2$ the $\Delta$ for $i$'s working set is 5 then 78 appears most often in $i$'s working set up until $t_5$

