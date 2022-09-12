import random
#from tkinter.simpledialog import * 

def getString():
    reStr=''
    reStr=askstring('문자열입력','거북이 쓸 문자열을 입력')
    return reStr

def getRGB():
    r=random.random()
    g=random.random()
    b=random.random()
    return (r,g,b)

def getXYAS(sw,sh):
    x=random.randrange(-sw/2,sw/2)
    y=random.randrange(-sh/2,sh/2)
    
    angle=random.randrange(0,360)
    size=random.randrange(10,50)
    return[x,y,angle,size]