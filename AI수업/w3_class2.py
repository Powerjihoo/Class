class Car:
    speed=0
    def upSpeed(self,value):
        self.speed+=value
        
        print('현재속도(슈퍼클래스)%d'%self.speed)
        
class Sedan(Car):
    def upSpeed(self,value):
        self.speed+=value
        #속도가 150이 넘으면 150으로 지정
        if self.speed>=150:
            self.speed=150
            
        print('현재속도(서브클래스)%d'%self.speed)
        
class Truck(Car):
    pass

class Sonata(Sedan):
    pass

sedan1,truck1,sonata1=None,None,None

truck1=Truck()
seda1=Sedan()
sonata1=Sonata()

print('트럭-->',end2='')
truck1.upSpeed(200)

print('승용차-->',end="")
seda1.upSpeed(200)            

print('소나타-->',end='')
sonata1.upSpeed(200)