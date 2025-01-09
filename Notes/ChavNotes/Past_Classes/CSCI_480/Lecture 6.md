# Image Order/Ray tracing

**How do we make images?**
IRL:
- Pencils, paintbrushes, watercolors, etc
- Eyes
- Cameras
On Computers:
- MS paint
- manually writing pixel values into Julia arrays
- virtual cameras

The world is 3D but images are 2D, we need to lose a D somehow.

### Math
A ray is half a line
- An origin (p) where the ray begins
- A direction (d) in which the ray goes
$r(t) = p + td$ - parametric equation for the ray, generating points on a line ($t>0$ gives all points on the ray)

### Projections
	ways to lose a D
A picture-frame method is called perspective projection
All viewing rays begin at one point
- eye, center of projection, camera center

### Parallel Projection
- all viewing rays come out of the center of the pixel and are parallel to one another

Ray Tracing Psudocode
```
for each pixel:
	generate a viewing ray for the pixel
	find the closest object it intersects
	determine the color of the object
```

### Viewing Rays
	are determined by the position and orientation of the camera
- for perspective projection, viewing rays originate at the eye.
- the direction varies depending on the pixel

**Simple Camera Example**
- Eye is at the origin (0, 0, 0)
- Looking down the negative z axis
- Viewport is parallel to the xy plane
- vh(height) = vw(width) = 1
- D(distance from view port) = 1
- W = width of image in pixels
- H = height of image in pixels

### Translating from (x, y) to (i, j)
To simplify the math replace (x, y) with (u, v) since we might not always be at the origin or looking down the -z axis.

$$u = (\frac{j-\frac{1}{2}}{W}-\frac{1}{2})*vw$$
$$v = (\frac{i-\frac{1}{2}}{W}-\frac{1}{2})*vh$$
Eye isn't always at the origin, but that only changes the $p + dt$ equation and not the direction.

For viewports that aren't aligned with x, y, z looking down negative z:
- it works the same way if we replace (x, y, z) with (u, v, w) and worrying about translating those later
- $\mathbf{p} = \mathbf{e}$
- $\mathbf{d} = u \cdot \mathbf{u}, v \cdot \mathbf{v}, d  \cdot \mathbf{w}$

### Creating Camera Basis
	given eye, view, and up
e = eye
w = -view
u = cross product of up and w
v = cross product of u and w

# Ray-Sphere Intersection

Ray (parametric): $\mathbf{p} + t\mathbf{d}$ = $[p_x +td_x, p_y+td_y, p_z + td_z]$ 
Sphere (parametric): $[\cos \Theta \sin \theta, \sin \Theta, \cos \Theta]]$ 

How many times might a ray intersect a sphere?
- 0, 1, or 2
What's an implicit equation for a sphere/What's true for all points on a sphere?
- They are all the same distance, $r$ from the origin.
Unit Sphere: $\sqrt{x^2 + y^2 + z^2} = 1(radius)$ 
Square both sides: $x^2 + y^2 + z^2 - 1 = 0$
Let vector a ($\mathbf{a}$) = $[x, y, z]$, then:
$xx+yy+zz-1=0$ so $\mathbf{\mathbf{a} \cdot \mathbf{a}-1=0}$ 

Subsitute:
$(p+td)^T (p+td)-1=0$
LOIF:
$d \cdot dt^2+(2p\cdot d)t+p \cdot p-1=0$
   A $t^2$           B t           C = 0

Number of intersections: 
$$t = \frac{-B \pm \sqrt{B^2-4AC}}{2A} \rightarrow t = \frac{-d\cdot p \pm \sqrt{(d\cdot p)^2-(d\cdot d)(p\cdot p -1)}}{d \cdot d}$$ 
