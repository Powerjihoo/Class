from glob import glob

def file(path):
    train='\n'.join(sorted(glob(path+'/*/*.png')))
    test='\n'.join(sorted(glob(path+'/*/*.png')))

    if path=='./MNIST_fashion/train':    
        t1=open('./train.txt','w')
        [t1.writelines(x) for x in train]
        t1.close()
    else:
        t2=open('./test.txt','w')
        [t2.writelines(y) for y in test]
        t2.close()