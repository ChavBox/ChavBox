### Grading Breakdown
	HW + Essays:    60% 
	Quizzes:        20%
	Final:          15%
	Participation:   5%

Office hours: Thursday 4pm

Book: Fourth Edition

Assignment 1: Read Syllabus

## 4/2: Chapter 9 - Medians and Order Stats

$\text{i}^{th}$  order statistic: $\text{i}^{th}$  smallest element from set of n
Example
- i = 1: minimum
- i = n: maximum 
- median: halfway point ... 
	- if n odd $i = \frac{n+1}{2}$ 
	- if n even $i = \frac{n}{2}$ 
- Percentile:
	- 35% $i = \lfloor 0.35n \rfloor$

##### Selection Problem
- Input A set of n distinct numbers $1 \leq i \leq n$ 
- Output: $\text{i}^{th}$ order statistic

Simple Solution: 
- sort array O(n log n)

Min/Max? Loop through and keep track
- O(1) or O(n)

Select ith smallest in linear time
book shows 2 ways (we will look at randomized)

```
A: array
n: array size
p: min of current range
r: max of current range
i: ith smalest element?
	A[1, 4, 6, 9, 13, 15, 18, 23]
	i = 4 
	ith smallest = 9
	
q: index of pivot
k: size of chunk we're looking at

Start:
Randomized-Select(A, 1, n, i)

Randomized-Select(A, p, r, i){
	if p == r
		return A[p]
	q = Randomized-Partition(A, p, r) [same algo as quicksort for refersher]
	k = q-p + 1
	if i == k
		return A[q]
	else if i < k
		return Randomized-Select(A, p, q-1, i)
	else
		return Randomized-Select(A, q+1, r, i-k)
```
Worst Case: $O(n^2)$ 
Average Case: T(n) time to solve random var.
- Goal: upperbound $E[T(n)] \leq O(n)$ 
- Randomized-Partition picks any pivot with equal probability 
- $A[1..q]$ has size k with probability $\frac{1}{n}$ $\forall$ $1 \leq k \leq n$ 
- $X_k = I$ {subarray has k elements} = {1 if subarray size k} {0 otherwise}
- When $X_k = 1$ then subarrays 
	- $A[1..q-1]$ size k -1
	- $A[q+1..n]$ size n-k
- $T(n) \leq [\Sigma^{n}_{k=1} X_k ** T(max(k-1, n-k))] + O(n)$ 
- $E[T(n)] \leq \frac{1}{n} \Sigma^n_{k-1} E[T(max(k-1, n-k))] + O(n) \leq \frac{2}{n} \Sigma_{k = \lfloor \frac{n}{2} \rfloor}^{n-1} E[T(k)] + O(n)$
- $E[T(n)] = f(n) \leq \frac{2}{n} \Sigma^{n-1}_{{k = \lfloor \frac{n}{2} \rfloor}} f(k) + O(n)$
- Can use substitution to get $f(n) \leq c * n$
- $E[T(n)] \leq O(n)$
