## Line Drawing
**Bresenham lines**
- Point sampling unit width rectangle leads to uneven line width
- Define line width parallel to pixel grid
- Turn on the single nearest pixel in each column
- 45 degree angles are thinner

Midpoint Algorithm
- Line goes from $(x_1, y_1)$ to $(x_2, y_2)$
- y = mx+b
- b will be the intercept for the line

Interpolating Values
Color is interpolated the same way that y is

Other Quadrants
From 45 to -45 degrees (x, y)
From 45 to 135 degrees (y, x)
From 135 to 225 (-x, y)
From 225 to 315 (-y, x)

Parametric View:
$v(x) = v_1 + \frac{x-x_1}{x_2 - x_1} (v_2 - v_1)$
$v_1 + t (v_2 - v_1)$
$v(t) = (1-t)v_1 + t(v_2)$
