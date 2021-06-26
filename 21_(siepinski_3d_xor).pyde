def setup():
    size(600,600,P3D)
    #stroke(255)
    noFill()

def tri():
    # translate(width/2-64,height/2+32,0)
    # rotateY(PI/2)
    # # rotateX(PI/2)
    # rotateY(2*PI*t)
    scale(1.5,1.5,1.5)
    beginShape(TRIANGLE)
    for i in range(128):
        for j in range(128):
            vertex(i,j,((i)^(j)))
    endShape(CLOSE)
       
t=0    
def draw():
    background(255)
    global t
    # camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    X=(width/2-64)*sin(TWO_PI*t)
    Y=(height/2-64)*cos(TWO_PI*t)
    camera(X,Y,400,80,100,0, cos(PI/3), cos(PI/3), cos(PI/3))
    tri()
    t+=0.005
    if frameCount<=200:
        saveFrame("fr###.gif")
    else:
        print"Saved"
