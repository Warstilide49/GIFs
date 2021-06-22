class PA:
    def __init__(self,radius,angle):
        self.angle=angle
        self.radius=radius
    def drawing(self,t):
        x=self.radius*sin(self.angle+t)
        y=self.radius*cos(self.angle+t)
        strokeWeight(10)
        stroke(255)
        point(x,y)

arr=[]

def setup():
    size(400,400)
    for i in range(8):
        obj=PA(100,i*PI/4)
        arr.append(obj)

t,n=0,0
def draw():
    background(20)
    translate(width/2,height/2)
    global t,n
    for i in range(8):
        arr[i].drawing(t)
    
    strokeWeight(3.5)
    stroke(random(128),random(128),random(128))
    circle(0,0,n*100)
    if floor(t)%2==0:
        n+=0.01
    else:
        n-=0.01
    t+=0.01
    
