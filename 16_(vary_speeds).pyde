def setup():
    size(600,600)
    strokeWeight(5)
    stroke(255)

t=0    
def orbit(n):
    total=6*n+1
    speed=t/(2*n)
    r=30*n
    for i in range(1,total+1):
        x=r*cos(i*2*PI/total + 2*PI*speed)
        y=r*sin(i*2*PI/total + 2*PI*speed)
        point(x,y)

def draw():
    global t
    background(20)
    translate(width/2,height/2)
    point(0,0)
    for i in range(8):
        orbit(i+1)
    t+=0.01
    if t<=6:
        saveFrame('fr###.gif')
    else:
        print('Saved')
