fp1=open('./data.txt','r',encoding='UTF-8')
fp3=open('./data1.txt','w')


fpstr=fp1.readlines()

for i in fpstr:
    fp3.writelines(i)
    
fp1.close()
fp3.close()