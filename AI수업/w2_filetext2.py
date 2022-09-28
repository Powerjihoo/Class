import cv2

f=open('img_list.txt')
for line in f:
    img=cv2.imread(line[:-1])
    cv2.imshow('img',img)
    cv2.waitKey(-2)

f.close()