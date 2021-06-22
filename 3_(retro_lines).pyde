def setup():
    size(400,400)
   

t=0

def draw():
    background(20)
    global t
    strokeWeight(5)
    translate(width/2,height/2)
    for i in range(10):
        stroke(255-i*20)
        line(x(t+i),y(t+i),x2(t+i),y2(t+i))
    t+=0.6

def x(t):
    return -sin(t/10)*100 - sin(t/30)*50
def y(t):
    return 100*cos(t/10) + 50* sin(t/10)
def x2(t):
    return -sin(t/20)*150 + sin(t/30)*50
def y2(t):
    return 100*cos(t/10)-cos(t/15)*100
