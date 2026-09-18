# SMAS-Assignment
All the assignment of SMAS is here.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ASSIGNMENT - 1

Solution-19
I used two libraries here:
  1. Numpy 2. Matplotlib

First, i defined an "Array" whose, dimensions are 6*2.
Then, I print the Matrix using in built PRINT function.
Similarly, I print the X column and Y column using slicing.



Solution-20
I defined 7 vectors which are just 1 dimensional, they represent the X and Y position of the drone at different time.

Make a list including all 7 vector and define a new empty list where all the displacement will be stored.


Then i start a for loop in list of vector and subtract consecutive vector and store the value in displacement list.


Solution-21
I have chosen the data of X-axis as absolute.
I make an array using equal spacing from 0 to 10 with 6 point to be entered in list. This act as base of our X- axis.
Then i defined our desired Y output in a array as 0.5*x
Then i stored all the actual reading we got of Y-axis in another array.

First plot: X as entries for x coordinate and desired Y output as y coordinates of plot. This act as our desired trajectory.

Second plot: X as entries for x coordinates and actual Y coordinates as y coordinates. This our actual trajectory and marked with dash as we do not know the actual coordinates in between.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Assignment 3

Solution-10
I used numpy and PIL
I am applying a geometric transformation to an image using matrix multiplication. First, I load the image and convert it into a numerical array so each pixel can be treated as a point in 2D space. Then I choose a transformation matrix based on the user’s input, such as scaling, rotation, shear, reflection, or projection.

After that, I define the center of the image and move every pixel relative to that center. For each pixel, I form a coordinate vector, multiply it by the selected matrix, and get a new position. I round the values to nearest integers and place the pixel into a new output canvas if the position is valid.

The program then displays the transformed image. In simple words, I am taking every pixel, changing its position using a mathematical rule, and drawing the result on a new image.

### Algorithm
1. Load image.
2. Convert image to array.
3. Select transformation matrix.
4. Find image center.
5. For each pixel:
   - shift to center
   - multiply by matrix
   - move back to output canvas
   - place pixel if inside bounds
6. Display transformed image.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Solution-11

I used numpy, tkinter, PIL

I am using a GUI-based image transformation program. First, I open a window so the user can choose the type of transformation. Then I ask for the image path, load the image, and convert it into a numerical array so each pixel can be handled like a point in 2D space.

I define several transformation matrices for:
- 90° counterclockwise rotation
- 90° clockwise rotation
- resizing
- flipping along X
- flipping along Y
- shear

After that, I choose the required matrix based on the user’s selection. Then I loop through every pixel of the image, shift it relative to the image center, multiply its coordinate vector by the transformation matrix, and find the new pixel position. I round the values and place them into a new output image if the coordinates are valid.

Finally, I display the transformed image. In simple words, I am moving each pixel according to a mathematical rule and showing the result.

### Algorithm
1. Open image chooser.
2. Load image and convert to array.
3. Select transformation matrix.
4. For each pixel:
   - subtract center
   - multiply by matrix
   - round new coordinates
   - place in output image
5. Display transformed result.





