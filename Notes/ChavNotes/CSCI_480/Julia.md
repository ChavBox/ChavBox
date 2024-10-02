# 2D Arrays
Image: A height-by-width array of pixels
- Each pixel is 3 single-precision floats

```
					  v- of type RGB{Float32}
canvas = zeros(RGB{Float32}, height, width)
			^- make an array      ^- with dimensions height by width
			     of zeros  
```

Matrix-style 1-based indexing (row, column), top left pixel center location is (1,1)
	top left corner of image location is (0.5, 0.5)

# Draw rectangle on canvas
```
using FileIO
using Images
using ImageView

height = 100
width = 100

canvas = zeros(RGB{Float32}, height, width)

#red, green, blue values range from 0.0 to 1.0
color = RGB{Float32}(1.0, 0.0, 0.0)

#top left coords:
tli = 25
tlj = 25

bottom right coords:
bri = 75
brj = 75

# set each of the pixels in the rectangle to the desired color
for i = tli:bri
	for j = tlj:brj
		canvas[i,j] = color
	end
end

# alternative way:

canvas[tli:bri, tlj:blj] .=color

# Display the image
# in vscode this will show image to the right
# otherwise it will print some of it's values
display(canvas)

# you can also "using ImageView" and call the imshow
# function to show the image in a window
imshow(canvas)

# save the image to png
save("box.png", canvas)
```