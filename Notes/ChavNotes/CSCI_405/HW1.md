TODO

**Question 1**
- 1.2 show T(n) = 1.5^n
- Analyze performance of 1.3 and 1.4

1. Greedy Counter Example
pick 4, set 3&5 unavailable, pick 2 set 1 unavailable, pick 6 total = 27
optimal: 39 (1, 3, 5)
t1 = 1
t2 = 4
t3 = 19
t4 = 20
t5 = 19
t6 = 3

S1: 1
S2: 2(4)
S3: 3, 1 (20)
S4: 4, 2(24)
S5: 5, 3, 1 (39)
S6: 5, 3, 1 (39)

S contains value, and path to value
S1 = 1:(1)
S2=4:(2)
S3=20(3, 1)
S4=

2. Even/Odd counterexample
t1: 35
t2: 4
t3: 2
t4: 40

even gives 44
odd gives 37
optimal gives 75

3. Dynamic Solution
```
v_i = value of plot i
S[1..n] = array of optimal solutions
S[i].v = optimal value for i tracts
S[i].p = optimal tracts to harvest

Bottom-up-Truffles(n){
	S[1] = (v_1, {1})
	S[2] = v_1 > v_2 ? (v_1, {1}):(v_2, {2})
	for i = 3..n
		profit = v_i + S[i-2].v
		if value > S[i-1].v
			S[i] = (profit, {S[i-2].p U i})
		else
			S[i] = S[i-1]
	return S[n].p
}

Bottom up idea:
if n = 1 optimal is trivial
maybe save value of n = 1
then to pick or not to pick:
	if n = 2, max between S[1] and v_2
	if n = 3, max between S[2] and v_3 + S[1]
	if n = 4, max between S[3] and v_4 + S[2]
	if n = 5, max between S[4] and 
	at n = n, max between S[n-1] and v_n + S[n-2]

S[n] = max(S[n-1], v_n + S[n-2])

How to know if you take or not?


```