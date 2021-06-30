from opensimplex import OpenSimplex

n=OpenSimplex()
nperiod=4.0
rad=1.5
SEED=random(10,1000)

def setup():
    size(600,600)
    

m=1500    
numFrames=120
K=12
r=20
def draw():
    background(20)
    noFill()
    stroke(255,120)
    strokeWeight(1.3)
    t=1.0*frameCount/numFrames
    for j in range(K):
        angle=map(j,0,K-1,0,2*PI)
        pushMatrix()
        translate(width/2,height/2)
        rotate(angle)
        #u=1.0*(i+t)/K
        #circle_rad=u*50
        for i in range(m):
            p=1.0*i/m
            stroke(20+p*400)
            dx = 25*n.noise3d(SEED + rad*cos(TWO_PI*(nperiod*p-t)),rad*sin(TWO_PI*(nperiod*p-t)),4.0*p)
            dy = 25*n.noise3d(2*SEED + rad*cos(TWO_PI*(nperiod*p-t)),rad*sin(TWO_PI*(nperiod*p-t)),4.0*p)
            point(p*width+dx+r*sin(p),r*cos(p)+dy)
        popMatrix()
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")'''
