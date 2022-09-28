import cv2
import os

file_list=os.listdir('./images/')
#print(file_list)

for img_name in file_list:
    #print(img)
    img=cv2.imread('./images/'+img_name)
    cv2.imshow('img',img)
    cv2.waitKey(-1)