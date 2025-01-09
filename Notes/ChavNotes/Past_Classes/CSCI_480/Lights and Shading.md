# Shading
**What does the color of a pixel depend on?**
- light location and direction - calculated form light and intersection point
- surface normal - stored in or calculated from object
- material/surface properties - stored in object
- eye direction - calculated from viewing ray and intersection point (-d normalized)

# Light Sources
**Where does light come from?**
- Point and Directional lights
### Point source
	Light emits equally in all directions
direction vector: source - (p+td) normalized 
### Directional light
	All the light comes from a fixed direction 
direction vector: l

### Diffuse (Lambertian) Reflection
