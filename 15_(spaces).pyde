def setup():
    size(600,600)
    background(20)
    
t=0

def draw():
    global x,t
    translate(width/2,height/2)
    if t<90:
        pushMatrix()
        stroke('#5F4B8B')
        fill('#5F4B8B')
        scale(t)
        circle(0,0,10)
        t+=0.5
        popMatrix()
    elif 90<=t<180:
        pushMatrix()
        stroke('#E69A8D')
        fill('#E69A8D')
        scale(t-90)
        triangle(0,-10,-10*sin(PI/3),10*cos(PI/3),10*sin(PI/3),10*cos(PI/3))
        t+=0.5
        popMatrix()
    elif 180<=t<=240:
        pushMatrix()
        stroke(20)
        fill(20)
        scale(t-180)
        square(-5,-5,10)
        t+=0.5
        popMatrix()
    if frameCount<=480:
        saveFrame('fr###.gif')
    else:
        print'Saved'
