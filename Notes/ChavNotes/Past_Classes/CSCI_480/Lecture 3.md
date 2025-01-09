# Modeling
Sphere:
- Center and radius
	- precision/accuracy
	- low storage, high compute cost
	- physics friendly
	- ease of modeling
- Triangle Mesh
	- Flexibility/generality
	- ease of editing
	- ease of storing other properties (besided geometry)
	- rendering efficiency
Both are viable, depending on application. It comes down to data structure selection. 
# Triangle Meshes: Geometry
Advantages:
- Made of very simple primitives
### Triangles
- Defined by three vertices
- Live in the plane containing those vertices
	- 3 vertices are always coplanar
- Vector normal to plane is the triangle's normal
- Conventions
	- Vertices are counter clockwise as seen from the outside or front
	- surface normal points towards the outside
- any other polygon can be triangulated

### Triangle Mesh
	a bunch of triangles connected together to form a surface
Triangles represented by tetrahedrons

### Indexed Triangle Set
	vertices are listed once without duplicates
	each triangle stores indices of its vertices

##### Triangle Strip
	each triangle is usualy adjacent to previous
	next triangle reuses previous two vertices
	every subsequence of 3 vertices is a triangle
e.g.
	vertex sequence 0, 1, 2, 3, 4, 5, 6, 7
triangle strip: (0, 1, 2), 

##### Triangle Fans
	same idea as triangle strips, but keep oldest index rather than newest
	every sequence of three vertices is a triangle
	same benefits as triangle strips