def setup():
    size(600,600)
    stroke(255)
    strokeWeight(3)
    fill(20)
    
def spokes(m,t,x,y):
    beginShape(TRIANGLE_STRIP)
    for i in range(m):
        angle=map(i,0,m-1,0,2*PI)
        vertex(x*cos(angle),x*sin(angle))
        vertex(y*cos(angle),y*sin(angle))
    endShape(CLOSE)
        
numFrames=60
K=10
def draw():
    background(255)
    translate(width/2,height/2)
    t=1.0*frameCount/(numFrames)
    m=30 #no. of balls
    rotate(2*PI*t/5)
    for i in range(K):
        p=(i+t)/K
        r=p-1.0/(360)
        q=map(p,1.0/(numFrames*K),1,0,500)
        stroke(255-(i-1)*40)
        spokes(m,t,q,q+30)
    if frameCount<=60:
        saveFrame("fr###.gif")
    else:
        print("saved")
