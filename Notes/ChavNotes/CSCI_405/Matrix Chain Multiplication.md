	Input: A1, A2, ... , An
	Want: A1*A2*...*An
	(A1*A2)A3 or A1(A2*A3) etc

Multiplying matricies:
C = AB
- A (p x q)
- B (q x r)
- C (p x r)
$C_{ij} = \Sigma_{k=1}^qA_{ik}B_{kj}$
One entry: i * k work
All of C: O(p * q * r)

**Example**
A1: 10 * 100
A2: 100 * 5
A3: 5 * 50

5,000 + 2,500 = 7500
(A1 x A2)A3

25,000 + 50,000 = 52,500
A1(A2 x A3)

