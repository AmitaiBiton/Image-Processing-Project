# Project---Image-Processing
## final Project in the course  

## Q1:

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


## Q2:

The main problem - find 9 points on the hands that if you draw a line between them, it will surround the wrist:

## my idea is:
In one word - identifying the relevant points Predicting the other points and correcting them at the end by edges (Canny)  

![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q2/idea.png) 

### step 1:
As you can see in the figure you can identify these 3 fingers in the following way -
Y values:
1. The thumb is the lowest value on the Y-axis
2. Middle finger value in second place
3. Very small value
According to the previous exercise we will again mark the points on the nails and we will select the points according to their Y values ​​according to the illustration we presented
We will sort by Y values then we can get the point area number 7 which I am looking for first.  

### step 2:
We will use the function goodFeaturesToTrack to mark important points I adjusted the values ​​of the function so that we get only the point 7 or close to it
By calculating the Y values we will take the points closest to the Y axis but the distant ones on the X axis and thus we will get the blue dot marked in the figure.
Sometimes he does not find the most accurate point but I tried to optimize it as much as possible


### step 3:
Once we have found point number 7 it is possible to calculate points 6 and 8 in two ways
1. Finger distances I built a function that passes over the Canny and calculates finger thickness so twice this thickness is approximately the distance of these points from point 7 on the Y axis and the X axis the same value as the digit 7
2. It is possible to draw a line between the thumb (on the X-axis) and the finger and mark a point of distance two fingers on the Y-axis (according to what I have seen so far this method is preferable) together with the use of a point on the finger
Axis X by the thumb line, Axis Y by the point on the nail of the "finger".
Summary I built a function that performs the calculation for each image which is more appropriate 1 or 2
1 is in a straight line with the finger and 2 is adjusts itself to the thumb line the small value between 1 and 2 is made minimum in them (makes sense)  

##### An example of an illustration:
![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q2/step_3.png)   


### Step 4:
Predicting the rest of the points on the hand by the thickness of the fingers (it is not as infallible as it sounds there is a relationship between the size of the hand and the distances of the points on the palm unless the palm is completely symmetrical)

### Step 5: Perhaps the most important step
After predicting the points fix the points by using Canny over it and stretching the points on the X or Y axis respectively
One can imagine it beyond the X-axis 50 pixels if we found a place where there are edges I mean
Canny == 255 Then move the point there as well as on the X-axis
Can also go down (-).
In addition a test on certain points like point 5 can not be too small compared to point 4 or 6 so I also performed such a test.  

### final stage:
Writing the points into Excel
Displays the new images in which the required illustration appears.
Tests and corrections made on the prediction of the points on the palm:
#### We found 5 points on the nails:
If we were able to find 5 points on 5 nails then the program works as I detailed above finds point number 7 by minimum distance on the Y axis then takes into account the T. axis of the point on the little finger (nail) and by sizes finds point number 8 then computers The thumb line and the y-axis of the dot on the nail of the "finger" and decide which of them is better the rest of the fingers contract according to the sizes of the fingers and finally fix on the edges (canny).  

#### We did not find 5 points on the nails:
I built a function that finds point 7 by going over the canny so if we encountered edges skip it and hold a number if it is equal to 4 I mean I got to the middle finger it usually happens at the top of the finger so need to fix about the size of the finger so I took a logical number fixed with it on the axis X After we have built the point seven the point 6 and 8 we build at a distance of 2 fingers from it on the Y-axis and continue in the same method on all the other fingers and at the end fixtures with canny usually in this part the points come out less accurate on the hand.

#### An example of an illustration:  

![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q2/step_6.png)  

## result:

## result images and mp point to Xls file:
![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q2/g_result.png)  

### More results:
![alt text](https://github.com/AmitaiBiton/Project---Image-Processing/blob/main/results/results_q2/result.png)  



