t=0

def setup():
    size(600,600)
    stroke(255)

def shape1(t):
    fill("#97BC62")
    r=50*cos(radians(t))-50
    beginShape()
    vertex(-100+r,-100-r)
    vertex(-60+r,-100-r)
    vertex(-60+r,60-r)
    vertex(100+r,60-r)
    vertex(100+r,100-r)
    vertex(-100+r,100-r)
    endShape(CLOSE)
    
def draw():
    global t
    background(255)
    translate(width/2,height/2)
    rotate(PI/4)
    if t%1440<360:
        shape1(t)
    elif 720>t%1440>360:
        rotate(PI)
        shape1(t)
    elif 1080>t%1440>720:
        rotate(PI/2)
        shape1(t)  
    else:
        rotate(3*PI/2)
        shape1(t)
    fill('#00203F')
    #noFill()
    rect(-100,-100,200,200)
    t+=6
    if  frameCount<241:
        saveFrame("fr###.gif")
    else:
        print("saved")
    
