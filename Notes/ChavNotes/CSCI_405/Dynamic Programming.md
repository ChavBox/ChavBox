	A general algorithm design technique.
	"Programming": refers to building up a table of solutions (tabular method)
	optimization problems: maximize value of solution givs an optimal solution 
	in terms of solutions to smaller problems. 

### Four Main Steps
1. structure of optima
2. recursive formula for value
3. compute optimal value
4. solve the problem

### Rod Cutting Example
	Working in steel mill with big metal rods, various customers want different
	integer length cuts of rod. 


Input: 
- Length of rod (n)
- table of prices
- $p_i$ for $i = 1, 2, ... , n$
Output:
- Maximum revenue possible for any choice of cuts

#### Recursive Top Down Solution
```
cutRod(p, n){
if n == 0:
	return 0
q = -inf
for i = 1..n
	q = max(q, p[i] + cutRod(p, n-1))
return q
}
```

#### Dynamic Programming Solution
- avoids repeat sub-problems
- every time we first solve a problem, store it in a table
	- table stores optimal values
- trade-off time for memory
- convert exponential to polynomial 

__Top Down with Memoization (remember past compute)__
```
memoizedCutRod(p, n){
	init r[0..n]
	for i = 0..n:
		r[i] = -inf
	return memoizedCutRodAux(p, n, r)
}

memoizedCutRodAux(p, n, r){
	if r[n] >= 0:
		return r[n]
	if n == 0:
		return 0
	q = -inf
	for i = 1..n
		q = max(q, p[i] + cutRod(p, n-1))
	r[n] = q
	return q
}
```

__Bottom Up__: Construct big problems from small
$$r[0] = 0$$
$$r[1] = max(p[1], r[0])$$
$$r[2] = max(p[1] + r[1], p[2] +r[0])$$
$$r[3] = max(p[1] + r[2], p[2] + r[1], p[3] + r[0]) $$
```
bottomUpCutRod(p, n){
	init r[0..n]
	r[0] = 0
	for j = i..n        //(size j problem)
		q = -inf
		for i = 1..j
			q = max(q, p[i] + r[j-i])
		r[j] = q
		return r[n]
}
```


### Matrix Multiply
```
Matrix-Chain-Order(p, n){
	init m[1:n, 1:n], s[1:(n-1), 2:n]
	for i = 1..n
		m[i,i] = 0
	for l = 2..n                  // Chain Length: l
		for i = 1..(n-l+1)        // Starting point: i
			j = i+l-1
			m[j] = inf
			for k = i..(j-1)
				q = m[i,j] + m[k+1, j] + p[i-1]*p[k]*p[j]
				if q < m[i, j]
					m[i,j] = q    // Remember cost
					s[i,j] = k    // Remember split
}
```


## Optimal Substructure

```
c[i,j] = length of LCS of X_i + Y_j

		   /          0                 if i = 0 or j = 0
c[i, j] = {      1 + c[i-1, j-1]        if x_i = y_j and i,j > 0
           \   c[i-1, j], c[i, j-1]     if x_i != y_j and i,j > 0



```

X = atom      Y = ant        Z = at

### Dynamic Wrap-up

optimal substructure:
- can recursively compute optimal value
- requires making choice (give max value)
- showing solutions to subproblems must also be optimal
	1. suppose subproblem is not optimal
	2. cut it out
	3. paste in what you think is optimal solution
	4. show you get a better solution overall

#### Number of subproblems:
- rods: cuts 1, 2, ..., n
- LCS: LCS of $(X_{m-1}, Y) or (X, Y_{n-1})$
	- two choices
	- one choice of endpoints are equal
	- overall cost depends on both

#### To solve:
1) bottom-up:
	- not recursive
	- start from base case
2) memoization:
	-  recursive
	- store in extra array

