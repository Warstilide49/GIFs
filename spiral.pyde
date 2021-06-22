def setup():
    size(600,600)
    stroke(255)
    noFill()

def spiral(p):
    q=sqrt(p)
    theta=5*TWO_PI*q
    r=0.45*width*q
    return PVector(r*cos(theta),r*sin(theta))

numFrames=60
K=120

def draw():
    t=1.0*frameCount/numFrames
    background(20)
    translate(width/2,height/2)
    for i in range(K):
        p=(i+t)/K
        stroke(75+150*sin(PI*p))
        circle(spiral(p).x,spiral(p).y,6)
    '''if frameCount<=numFrames:
        saveFrame('fr###.gif')
    else:
        print"SAVED"'''
