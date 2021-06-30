#Copied exactly from etienne's wordpress blog
from opensimplex import OpenSimplex

class Objekt:
    def __init__(self):
        self.seed=random(10,1000)
        self.offset=random(TWO_PI)
        self.ff=random(0.5,2.5)
        self.sw=random(0.8,1.8)
        self.part=0.1+0.5*pow(random(1),2.0)
        self.rf=random(0.5,1.15)
        self.d=random(10,120)
    def show(self,m,n,t):
        for i in range(m):
            p=1.0*i/m
            theta=self.offset+self.part*TWO_PI*i/m
            rad=1.3
            per=2
            x = self.rf*(my_curve(theta).x) + pow(p,3.0)*self.d*n.noise2d(self.seed + rad*cos(TWO_PI*(per*p-t)),rad*sin(TWO_PI*(per*p-t)))
            y = self.rf*(my_curve(theta).y) + pow(p,3.0)*self.d*n.noise2d(2*self.seed + rad*cos(TWO_PI*(per*p-t)),rad*sin(TWO_PI*(per*p-t)))
            strokeWeight(self.sw)
            stroke(255,self.ff*18*sin(PI*p))
            point(x,y)

my_list=[]
n=OpenSimplex()
iterations=200
m=500
numFrames=100
r=200
def setup():
    size(600,600,P3D)
    for i in range(iterations):
        my_list.append(Objekt())
    
def my_curve(angle):
    return PVector(r*pow(cos(angle),3.0),r*pow(sin(angle),3.0))

def draw():
    background(20)
    translate(width/2,height/2)
    t=1.0*frameCount/numFrames
    for i in range(iterations):
        my_list[i].show(m,n,t)
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("saved")'''
