class lpoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
def periodicFunction(u):
    return map(cos(TWO_PI*u),-1,1,0.2,1.8)

def offset(x,y):
    return 0.01*dist(x,y,width/2,height/2)
    
def setup():
    size(600,600)
    stroke(255)

def circlelines(r):
    j=0
    while j<2*PI:
        point1=lpoint(r*cos(j),r*sin(j))
        point2=lpoint(r*cos(j+PI/3),r*sin(j+PI/3))
        line(point1.x,point1.y,point2.x,point2.y)
        j+=2*PI/3
 
def draw():
    background(20)
    numFrames=60
    t=1.0*frameCount/numFrames
    #print t
    m=10
    translate(width/2,height/2)
    for i in range(m):
        newRadius=200*sin(radians(i*t*10))#+100*sin(radians(i*t*10)+PI)
        circlelines(newRadius)
            
    if 0<t<=3 or 15<t<=18:
        saveFrame('fr###.gif')
    else:
        print('Saved')
