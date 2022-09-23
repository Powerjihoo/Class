from glob import glob

def file(path):
    img='\n'.join(sorted(glob(path+'/*/*.png')))  #1
    str=open('%s.txt'%path.split('/')[-1],'w')    #2
    [str.writelines(x) for x in img]              #3
    str.close()                                   #4

    
import read_list

read_list.file('./MNIST_fashion/test')
