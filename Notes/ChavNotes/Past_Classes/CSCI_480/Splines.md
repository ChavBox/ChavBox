	goal: draw curvy lines
Math:
- points for control
- piecewise low-degree polynomials for smoothness

**Start Simple: Linear Interpolation**
	2 ways to write a line:
Implicit
	y = mx+b
	ax+by+c = 0
Parametric:
	r(t) = p + td

For two points p0, p1:
	$r(t) = p0 + (p1-p0)t$
	$r(t) = (1-t)p0 + t*p1$

Convention: use u as a parameter that only ranges from 0 to 1

$f(u) = (1-u)p_0+up_1$ 

To see how this is a degree one polynomial, re-write as:
	$a_0 = p_0$
	$a_1 = p_1 - p_0$
$f(u) = a_0 + ua_1 = u^0a_0 + u^1a_1$, which is the dot product of $[u^0,u^1]$ and $[a_0,a_1]$ 

## Quadratic

$f(u) = u^0a_0+u^1a_1+u^2a_2$

$p_0 = f(0) = [1, 0, 0] \cdot [a_0, a_1, a_2]^T = a_0$  
$p_1 = f(0.5) = [1, 0.5, 0.25] \cdot [a_0, a_1, a_2]^T = a_1$ 
$p_2 = f(1) = [1, 1, 1] ...$

