[[Julia]]

# Model to Image
	transform image coordinate to model coordinate
```
for each pixel p:
	if p is inside triangle
	turn on pixel
```

# Vectors
Vector between 2 points (p, q) is q-p

Dot product
	one version of multiplying 2 vectors


$u = (u_x, u_y)$
$v = (v_x, v_y)$
$u dot v = u_xv_x + u_yv_y$

# Point in Triangle
draw vectors to each point of the triangle in counterclockwise order
	a point is inside the triangle if it is to the left of all three vectors