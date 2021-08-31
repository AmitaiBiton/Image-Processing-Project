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
First thing - use Canny to get the edges of the image (the desired hand) then use the Hough Circles function to get all the circles in the image that have a function according to the parameters we enter such as the radius of the circle we are looking for and the maximum and minimum parameters get circles After adjusting the function to the requirements of the exercise I got all the possible circles then I made a loop transition on all the circles obtained and sculpted some of them for example a wristwatch is usually on the X axis at the end so there I did not mark a circle according to logic according to the pictures we got (not I got ).
Finally a function responsible for the display in the manner required one after the other show ().

#### result:
![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q1/image3.png) 
![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q1/image1.png) 

see more at https://github.com/AmitaiBiton/Project---Image-Processing/tree/main/results/results_q1  
see code - https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/projectIM2021_q1.py     


### Q2:

The main problem - find 9 points on the hands that if you draw a line between them, it will surround the wrist:

#### my idea is:
In one word - identifying the relevant points Predicting the other points and correcting them at the end by edges (Canny)  
![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q2/idea.png) 

##### step one :
As you can see in the figure you can identify these 3 fingers in the following way -
Y values:
1. The thumb is the lowest value on the Y-axis
2. Middle finger value in second place
3. Very small value
According to the previous exercise we will again mark the points on the nails and we will select the points according to their Y values ​​according to the illustration we presented
We will sort by Y values then we can get the point area number 7 which I am looking for first.  

##### step two :
We will use the function goodFeaturesToTrack to mark important points I adjusted the values ​​of the function so that we get only the point 7 or close to it
By calculating the Y values we will take the points closest to the Y axis but the distant ones on the X axis and thus we will get the blue dot marked in the figure.
Sometimes he does not find the most accurate point but I tried to optimize it as much as possible


