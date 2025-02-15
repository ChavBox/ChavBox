	Filling out a table of numbers - used in optimization problems
	Looking for a solution to
		-minimize cost
		-maximize value

### 4 Main Steps
1. Structure of optimal solution
2. Recursively define optimal value
3. Compute it bottom up or top down
4. Construct solution

##### Example: Rod Cutting
	Running a factory that produces steel rods, which are cut up. Different length cuts are valued differently.
	Input: length (n) of a rod and table of prices (P_i) for i = 1..n

**2 methods to convert top-down recursive solution into a dynamic programming one**
- Compute Table of $r_i$ 
	- Memoization - Cache value as it is computed
	- Bottom-up - remove recursion by building table from small to big

```
Bottom-up-Cut-Rod(p, n){
	let r[0..n] be new array
	r[0] = 0
	for j = 1..n
		q = -inf
		for i = 1..j
			q = max(q, p[i] + r[j-i])
		r[j] = q
	return r[n]
}

# Record in r[0..n] the values computed recursively
Memoized-cut-rod(p, n){
	let r[0..n] be a new array of -inf
	return Memoized-cut-rod-aux(p, n, r)	
}

Memoized-cut-rod-aux(p, n, r){
	if r[n] >= 0
		return r[n]
	if n == 0
		q = 0
	else
		q = -inf
		for i = 1..n
			q = max(q, p[i] + Memoized-cut-rod-aux(p, n-i, r))
		r[n] = q
		return q
}


```

Knapsack Problem:
```
n = number of items
v.n = value of item n
w.n = weight of item n
W = capacity of backpack

ks-memo(n, W){
	init C[0..n, 0..w] = -inf    //C[i, w] = optimal value
	Knapsack-alt(n, w, C)
}

ks-alt(n, w, C)(
	if C[n, w] > 0{
		return C[n, w]
	}else{
		// is value of taking current item + optimal value of remaining weight
		// more than value of 
		C[n, w] = max(v.n + ks-alt(n-1, w-w.n, C), ks-alt(n-1, w, C))
	}
)

		for j = 10..W         //J increments by 10
			C[i,j] = max(v.i + C[i-1, j-w.i], C[i, j-10])
		//first check for v.i + C[i-1, j-w.i] is correct, but other is not
		//
}
```