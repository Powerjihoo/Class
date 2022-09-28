from glob import glob

train='\n'.join(sorted(glob('./MNIST_fashion/train/*/*.png')))
test='\n'.join(sorted(glob('./MNIST_fashion/test/*/*.png')))

t1=open('./train.txt','w')
[t1.writelines(x) for x in train]
t1.close()

t2=open('./test.txt','w')
[t2.writelines(y) for y in test]
t2.close()