import csv
import numpy as np
import matplotlib.image as im
image=im.imread('image1.jpg')
red=image[:,:,0]
green=image[:,:,1]
blue=image[:,:,2]
redOutputFile1 = 'red_channel1.csv'
greenOutputFile1 = 'green_channel1.csv'
blueOutputFile1 = 'blue_channel1.csv'
with open(redOutputFile1, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(red)

with open(greenOutputFile1, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(green)

with open(blueOutputFile1, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(blue)
print('Red, green, and blue channels saved to separate CSV files successfully!');
