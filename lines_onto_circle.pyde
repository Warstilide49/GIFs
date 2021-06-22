def setup():
    size(600,600)
    stroke(20)
    noFill()
    strokeWeight(2.5)

y=0
t=0
x1=-300
changer=2.5
def draw():
    global t,x1,changer
    translate(width/2,height/2)
    background(255)
    if -70<x1<60:
        changer=2.5-sin(radians(x1))*2.5
        strokeWeight(changer)
        #line(x1,0,x1+20,0)
        circle(0,0,120)
    else:
        strokeWeight(changer)
        line(x1+10,0,x1,0)
        line(0,x1+10,0,x1)
        line(-x1-10,0,-x1,0)
        line(0,-x1-10,0,-x1)
        circle(0,0,120)
        changer=2.5
    x1+=t
    t+=0.03
    if frameCount<240:
        saveFrame("fr###.gif")
    else:
        print("Saved")
        
