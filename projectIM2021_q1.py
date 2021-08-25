import cv2
import numpy as np
import os
from matplotlib.pyplot import figure
figure(num=None, figsize=(16, 16), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import pyplot as plt

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def show(images):
    for image in images:
        plt.subplot(), plt.imshow(image, cmap="gray"), plt.title('')
        plt.xticks([]), plt.yticks([])
        plt.show()


def detectFingeris(images):
    for image in images:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 160, 250)
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2, 25, param1=150, param2=36, minRadius=8, maxRadius=23);

        circles = np.uint16(np.around(circles));
        count = 0
        for i in circles[0]:
            if i[0] < 400 and i[1]<400:
                cv2.circle(image, (i[0], i[1]), 1, (255,0,0), 4)



if  __name__ == "__main__":
    images = load_images_from_folder('./images')
    detectFingeris(images)
    show(images)




