def setup():
    size(600,600)

def vector(p,r):
    q=sqrt(p)
    theta=5*TWO_PI*q
    return PVector(r* 16* pow(sin(theta),3),-r*(13*cos(theta)-5* cos(2*theta)-2*cos(3*theta) - cos(4*theta)))

numFrames=60
K=100

def draw():
    t=1.0*frameCount/numFrames
    background(20)
    translate(width/2,height/2)
    for i in range(K):
        fill("#fdbaf8")
        stroke("#fdbaf8")
        p=(i+t)/(K)
        circle(vector(p,7).x,vector(p,7).y,6)
        fill("#b0efeb")
        stroke("#b0efeb")
        circle(vector(p,11).x,vector(p,11).y,6)
        fill("#edffa9")
        stroke("#edffa9")
        circle(vector(p,15).x,vector(p,15).y,6)
    if frameCount<=numFrames:
        saveFrame('fr###.gif')
    else:
        print"SAVED"
