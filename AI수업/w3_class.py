class Car:
    color=""
    speed=0
    count=0
    
    def __init__(self):
        self.speed=0
        Car.count+=1
    
    def upSpeed(self,value):
        self.speed+=value
        #속도가 150이 넘으면 150으로 지정
        if self.speed>=150:
            self.speed=150
        
    def downSpeed(self,value):
        self.speed-=value
        
myCar1,myCar2=None,None


myCar1=Car()
myCar1.speed=30
myCar1.upSpeed(60)
print('자동차1의 현재 속도는 %dkm입니다. 생상된 자동차는 총 %d대입니다'%(myCar1.speed,Car.count))
myCar2=Car()
myCar2.speed=60
print('자동차2의 현재 속도는 %dkm입니다. 생상된 자동차는 총 %d대입니다'%(myCar2.speed,myCar2.count))

