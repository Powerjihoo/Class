import cv2
import os

file_list=os.listdir('./images/')
#print(file_list)

for img_name in file_list:
    #print(img)
    img=cv2.imread('./images/'+img_name)
    cv2.imshow('img',img)
    cv2.waitKey(-1)
    
    if not os.path.exists('./images_copy/'):
        os.makedirs('./images_copy/')
        
    cv2.imwrite('./images_copy/'+img_name,img)