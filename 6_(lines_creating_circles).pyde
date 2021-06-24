x=140
y=140
angle=0
dia=7

def setup():
    size(500,500)

def draw():
    global angle,dia
    background(20)
    translate(width/2,height/2)
    rotate(radians(angle/3))
    for a in range(0,360,15):
        pushMatrix()
        if angle<360:
            rotate(radians(a)*cos(radians(angle)))
        else:
            rotate(radians(a))
        stroke(255)
        strokeWeight(1.5)
        line(x*sin(radians(angle)),0,0,y-dia/2)
        stroke(255)
        noFill()
        circle(x*sin(radians(angle)),0,dia)
        stroke(255)
        noFill()
        circle(0,y,dia)
        popMatrix()
    angle+=1
    
    if frameCount<=540 and frameCount%3==0:
        saveFrame("fr###.gif")
    else:
        exit()
