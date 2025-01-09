Rasterizer asumes triangles are on screen which is problematic to have triangles crosing the plane z=0

After projection
- clip against the planes x, y, z = 1, -1 (6 planes)
- primitive operation: clip triangle against axis-aligned plane

## Clipping a triangle against a plane
	4 cases based on sidedness of verts
- All in (keep)
- all out(discard)
- one in, two out (one clipped triangle)
- two in, one out (two clipped triangles)