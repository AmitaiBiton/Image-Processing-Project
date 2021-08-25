import cv2
import numpy as np
import os
from matplotlib.pyplot import figure
figure(num=None, figsize=(16, 16), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import pyplot as plt
import xlwt
from xlwt import Workbook

"""
    # Finding the fingertips in the image to build guiding
    # points for the continuation of the project, as well as
    # maintaining 3 lists one where we will hold the X and Y values
    # for each point a second list we will hold the X values
#and a third list the Y values
"""
def find_circles(image):
    edges = cv2.Canny(image, 160, 250)

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2, 25, param1=150, param2=36, minRadius=8, maxRadius=23);
    temp_list = []
    list = []
    t = []

    for i in circles[0]:
        if i[0] < 400 and i[1] < 400:
            cv2.circle(image, (int(i[0]), int(i[1])), 1, (255, 0, 0), 4)
            list.append((i[0], i[1]))
            temp_list.append(i[0])
            t.append(i[1])

    return  np.array(temp_list) , np.array(t) , list  ,circles


"""
    By the 3 lists we built we can find the points that appear on the toe the 
    points that appear on the middle finger and the points that appear on the 
    little finger, then we can actually predict by the finger sizes the
    distances and build a model where each hand can fit the points well to the desired places
    The finding of the fingers is done according to the sizes of the finger we know that the 
    middle finger is the largest and therefore on the X-axis it is closest 
    to zero however the farthest toe and therefore on the X-axis it will get the highest value
"""
def build_Guiding_Points(sort_by_x_distance , list):
    f1y = sort_by_x_distance[2]
    f2y = sort_by_x_distance[0]
    f3y = sort_by_x_distance[4]
    f4y = sort_by_x_distance[1]
    f1x = 0
    f2x = 0
    f3x = 0
    f4x = 0
    for l in list:
        if l[1] == f1y:
            f1x = l[0]
        if l[1] == f2y:
            f2x = l[0]
        if l[1] == f3y:
            f3x = l[0]
        if l[1] == f4y:
            f4x = l[0]
    points =[(f1x,f1y) ,(f2x,f2y) ,(f3x,f3y) ,(f4x,f4y)]

    return points



# using corner to drew important points on image and
# #using list to record the point
def draw_first_point(corners , points , image):
    list = []
    for i in corners:
        x, y = i.ravel()
        if x > 215 and x < 290 and y > 200 and y < 280 :
            cv2.circle(image, (x, y), 3, 255, -1)
            list.append((x, y))
    return list

"""
Once we have found the points on the fingers one can find point number 7 by calculating distances
On the Y-axis the point between the two fingers and on the X-axis the same is the desired 
number of course at a reasonable distance according to the logic of finger thickness
"""
def find_point_7_by_circles(points  ,list):
    temp = []
    x= 0
    y = 0
    for l in list:
        temp.append(abs(l[1] - points[0][1]))
    temp = np.array(temp)
    if len(temp) != 0:
        min_point = temp.min()
        for l in list:
            if abs(l[1] - points[0][1]) == min_point  :
                x, y = l
                break

    return x,y

def find_point_7_by_canny(canny , image):
    count =0
    list = []
    for i in range(canny.shape[1]-1):
        count=0
        for j in range(canny.shape[0]-1):
            if i >=canny.shape[1]:
                return
            if canny[j][i]==255:
                count+=1
                i +=40
            if count==4:
                return j, i

"""
We want to build points 6 and 8 by calculating the average size of the fingers
 double 2 in the same line take left and right of course we took into account 
 this function in both the toe and the little finger
We have taken the little one of their sons logically the toe nest is parallel to point number
 6 and the pinky line on the X-axis is parallel to the number 8
So we took the smallest of them calculating finger sizes or finger lines
"""
def point_to_start(points , x ,y):
    if int(points[1][0]) > x :
        point6X = int(points[1][0])
    elif int(points[1][0]) <= x  :
        point6X = x

    point8y = 0
    if int(points[2][1]) > y :
        point8y = int(points[2][1])
    elif int(points[2][1]) <= y :
        point8y = x

    point6y = 0
    if int(points[3][1]) < y:
        point6y = int(points[3][1])
    elif int(points[3][1]) >= y:
        point6y = y
    return point6X , point8y , point6y



"""
After we got the points 7 6 8 you can continue to the rest of the fingers 
according to the finger sizes, there is a direct relationship between the
 structure of the hand and the width of the fingers so you can
  predict more or less in each hand where the other points will appear. By Canny
"""
def build_points(point6X ,point8y ,point6y ,x ,y , size_finger):

    point1 = (x + 4 * int(size_finger), point8y- int(size_finger / 6))
    point2 = (point6X + 4 * int(size_finger), point6y + int(size_finger))
    point3 = (point6X + 3 * int(size_finger), point6y)
    point4 = (point6X + int(size_finger), point6y)
    point5 = (point6X + int(size_finger / 2), point6y )
    point6 = (point6X - int(size_finger / 2), point6y)
    point7 = (x, y)
    point9 = (x + 2 * int(size_finger), point8y + int(size_finger / 8))
    point8 = (x + int(size_finger), point8y - int(size_finger / 6))

    all_point = [point1, point2, point3, point4, point5, point6, point7, point8, point9]
    return  all_point

# using cv to draw the points anf after the line
def drawLineAndPoint(allPoint , image):
    for i in range(len(all_point)):
        cv2.circle(image, allPoint[i], 5, (255, 255, 0), -1)


    for j in range(len(all_point)-1):
        cv2.line(image, allPoint[j], allPoint[j+1], 255, 3)
    cv2.line(image, allPoint[0],  allPoint[len(all_point)-1], 255, 3)

    return image

# after we predict the points we can fix the points by using canny
#Stretching the points to the right place
def fixPoint(all_point  , canny):
    for i in range(len(all_point)):
        point = all_point[i]
        x= point[1]
        y = point[0]

        if x > canny.shape[0] or y > canny.shape[1]:
            return all_point
        for j in range(80):
            if canny[x][y]==0:
                x -=1
            elif canny[x][y]==255:
                all_point[i] = y,x
                break
        for j in range(80):
            if canny[x][y]==0:
                x +=1
            elif canny[x][y]==255:
                all_point[i] =  y,x
                break

        if  i==5:
            point1 = all_point[i]
            x1 = point1[1]
            point2 = all_point[i-1]
            x2 = point2[1]
            y2 = point2[0]
            if x1 > x2+15 :
                all_point[i-1]= y2 ,x1



    return all_point


# calculate the size of finger for every image (hand)
def Finger_Size(circles):
    list =[]
    for i in circles[0]:
        for j in circles[0]:
            if i[1]!=j[1] and abs(i[1]-j[1])>10:
                list.append(abs(i[1]-j[1]))
    if len(list)!=0:
        if min(list) <35:
            return 50
    elif len(list) ==0:
        return 50
    return min(list)


# write the points to exel
def write_points(all_points ,sheet1, count ,pic):


    sheet1.write(0 ,pic +0,  float(count))

    sheet1.write(1 ,pic + 0, 'Point')
    sheet1.write(1, pic +1, 'X')
    sheet1.write(1, pic +2, 'Y')
    for i in range(0 , len(all_points)):
        sheet1.write(i+2, pic +0, float(i+1))
        sheet1.write(i+2, pic +1, float(all_points[i][0]))
        sheet1.write(i+2, pic +2, float(all_points[i][1]))




def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


if  __name__ == "__main__":
    images = load_images_from_folder('./images')
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    count_picture = 0
    space_in_exel = 0

    for image in images:
        new_image = np.copy(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 0, 255)
        corners = cv2.goodFeaturesToTrack(canny, 50, 0.01, 10)
        corners = np.int0(corners)
        temp_list, t, list1, circles = find_circles(gray)
        sort = np.sort(t)
        if len(sort) >= 5:
            points = build_Guiding_Points(sort, list1)
            finger = Finger_Size(circles)
            list = draw_first_point(corners, points, image)
            x, y = find_point_7_by_circles(points, list)
            if x == 0 or y == 0:
                x = int(points[0][0]) +200
                y  = int(points[0][1])+15
            point6X, point8y, point6y = point_to_start(points, x, y)
            if (y-point6y) < finger+25:
                y += int(finger)
                point6X, point8y, point6y = point_to_start(points, x, y)
            if (point8y-y) < finger+25:
                point8y +=int(finger/2)
            all_point = build_points(point6X, point8y, point6y, x, y, finger)


        elif len(sort)<5:
            x,y  = find_point_7_by_canny(canny, new_image)
            finger = Finger_Size(circles)
            point7X =  x
            point7y = y
            point8y  = y +2*int(finger)
            point6y = y- 2*int(finger)
            point7 = (x,y)
            point6 = (x + int(finger), point6y)
            point8 = (x + int(finger) , point8y)
            point1 = (x + 4 * int(finger), point8y - int(finger / 2))
            point2 = (x + 4 * int(finger), point6y + int(finger))
            point3 = (x + 3 * int(finger), point6y)
            point4 = (x + int(finger), point6y)
            point5 = (x + int(finger / 2), point6y + int(finger / 4))
            point9 = (x + 2 * int(finger), point8y + int(finger / 8))
            all_point = [point1, point2, point3, point4, point5, point6, point7, point8, point9]

        all_point = fixPoint(all_point, canny)
        new_image = drawLineAndPoint(all_point, new_image)
        count_picture += 1
        write_points(all_point, sheet1, count_picture, space_in_exel)
        space_in_exel += 4

        plt.imshow(new_image)
        plt.show()
    wb.save('xlwt example.xls')














