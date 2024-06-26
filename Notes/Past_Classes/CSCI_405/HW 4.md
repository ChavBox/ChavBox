## Question 1
n remote villages
goal: transportation network (connected undirected graph)
- reach any town from any other town via road or flight
- can build a road between any two towns (straight line path)

Town (i) information:
- location: ($x_i$, $y_i$) (miles)
- Air route cost: $C+md$
	- C = aircraft maintence cost
	- m = cost per mile
	- d = distance between towns
- Road cost: $c + Md$ 
	- c = cost of road maintenance
	- M = cost per mile 
	- d = distance between towns

Minimize cost, connect all towns algorithm:
```

```

For any pair of towns with a direct connection, determine distance where air travel becomes more efficient.

## Question 2
Set of expected travel times connecting town $i$ and $j$ $w(i,j)$ 

Set of expected time of road segment connection wait $t(i)$ for intersection i

Give an efficient algorithm that allows computation of the most efficient route from Bellingham to Portland

## Question 3
Want to buy car, concerned about battery range
- D: distance a car can drive with full charge
- Bellingham = directed graph of road networks + distances between cities. 
- Network can only include cities with charging stations.

**Show how to determine in linear time if a route from Bham to any other city is possible with range D.***

Algorithm to determine the min fuel tank capacity to get from bham to a particular city.


## Question 4

Farmers fields are too quickly inundated from flood
Cows need to get to higher ground that is close.
- $n$ farms
- each containing $c_i$ cows ($i = 1..n$)
- $k$ neighboring farms willing to house the cows
- neighboring farm must be within 2 hour cow-walk
- each neighboring farm ($j = 1..k$) can only accept $p_j$ cows

Polynomial time algorithm:
- Input
	- $c_i$ : number of cows on farm $i$
	- $p_j$ : number of cows neighboring farm $j$ can accept
	- $t_{ij}$ : cow walk times from farm $i$ to $j$






\newpage
\begin{center}
    \section*{Homework 2 Revision}
\end{center}
3. \points{20} There is a new videoconference and social network app named Snoom, wildly popular due to
it’s unique capability to enable chat while the user is asleep by tweaking the advertisements they see while
“mindlessly” scrolling on their phone later to subconsciously imprint those messages in their brain. My mom
and I use it so that I remember to always call. \\ \\
Snoom, like most services these days, runs in the cloud which you can think of as a large collection of
high-end but independent computers. However, their engineers have also invested in datacenter with very
fast networking, i.e. a supercomputer, for certain costly computations. They periodically have to recalculate
their social network’s search index through a series of independent jobs $J_1, . . . , J_n$. To complete job $Ji$, it
must first be preprocessed on the datacenter which requires $d_i$ time there and later $c_i$ time finishing on one
of the cloud machines. \\ \\
There are many more than $n$ cloud computers available, so every job can be finished in parallel, but the
supercomputer can only work on one job at a time, serially. So when a job finishes preprocessing, it can
proceed to the finishing stage regardless of whether there are other jobs finishing as well. Ensuring that all
$n$ jobs complete as quickly as possible is essential so that Snoom’s social network grows as fast as possible
(if you can’t find your friends, how can you invite them to the network?), in line with the company’s goal to
maximize profit (ad revenue). \\

\begin{enumerate}
    \item[a.] \points{8} Devise an optimal polynomial-time scheduling algorithm that determines a schedule for the
                        $n$ jobs on the supercomputer so that the completion time of all the cloud machines is minimal. Hint:
                        Think like the company’s ruthless private equity backers.
    \item[b.] \points{2} Analyze the runtime of your algorithm.
    \item[c.] \points{10} Show that your algorithm returns the optimal solution. Try the “cut-and-paste” method.
\end{enumerate}
