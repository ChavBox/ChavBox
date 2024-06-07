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
	- 