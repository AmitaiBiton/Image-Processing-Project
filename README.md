# Project---Image-Processing
## final Project in the course  

### Q1:

We were asked to identify the tips of the fingers (nails) in photos of hands taken by a thermal camera
Each hand should identify 5 edges.
Some of the requirements is that we load the whole file of the images in a generic way
so that if there are 10 images or 50 the program will still be executed.
I used the OS library to load the images into an array (list) and from the list
we can access the whole image for that matter first place image number 1 and so on
See function - load_images_from_folder (folder)
Perception of the desired places in the picture for marking:
First thing - use Canny to get the edges of the image (the desired hand) then use the Hough Circles function to get all the circles in the image that have a function according to the parameters we enter such as the radius of the circle we are looking for and the maximum and minimum parameters get circles