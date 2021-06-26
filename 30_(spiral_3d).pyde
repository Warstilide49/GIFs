def setup():
    size(600,600,P3D)
    stroke(255)
    noFill()

def spiral(p):
    q=sqrt(p)
    theta=5*TWO_PI*q
    r=0.15*width*q
    z=700*p
    return PVector(r*cos(theta),r*sin(theta),z)

numFrames=60
K=120
def draw():
    t=1.0*frameCount/numFrames
    background(20)
    translate(width/2,height/2)
    for i in range(K):
        p=(i+t)/K
        stroke(75+150*sin(PI*p))
        pushMatrix()
        translate(spiral(p).x,spiral(p).y,spiral(p).z)
        noFill()
        circle(0,0,5)
        fill(255)
        circle(0,0,3*noise(p))
        popMatrix()
    if frameCount<=numFrames:
        saveFrame('fr###.gif')
    else:
        print"SAVED"
