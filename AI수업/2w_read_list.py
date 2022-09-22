import os

path='./MNIST_fashion/'
fold1=os.listdir(path)

for it in range(len(fold1)):
    fold2=os.listdir(path+fold1[it]+'/')
    f=open('%s.txt'%fold1[it],'w')
    for ixx in range(len(fold2)):
        fold3=os.listdir(path+fold1[it]+'/'+fold2[ixx]+'/')
        for iyy in range(len(fold3)):
            f.write(path+fold1[it]+'/'+fold2[ixx]+'/'+fold3[iyy]+'\n')
    f.close()