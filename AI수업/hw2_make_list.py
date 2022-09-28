import os

file_list=os.listdir('./images/')
f=open('img_list.txt','w')

for name in file_list:
    f.write('./images/'+name+'\n')
    
f.close()