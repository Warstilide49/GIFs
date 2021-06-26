def setup():
    size(600,600)
    strokeWeight(0.5)
    stroke(255)

def formula(i,a,b,m,n1,n2,n3):
    if n1!=0:
        first=abs(cos(m*i/4) /a) **n2
        sec=abs(sin(m*i/4) /b) **n3
        return (first+sec)**(-1/n1)

def structure(t):
    beginShape()
    i=0
    while i<2*PI:
        r=50*formula(i,1,1,16,4,abs(sin(TWO_PI*t)),abs(cos(TWO_PI*t)))
        x=r*cos(i)
        y=r*sin(i)
        vertex(x,y)
        i+=0.001
    endShape(CLOSE)
t=0
def draw():
    global t
    background('#342222')
    m=6
    for i in range(m):
        for j in range(m):
            x=map(i,0,m-1,0,width)
            y=map(j,0,m-1,0,height)
            pushMatrix()
            translate(x,y)
            structure(t)
            popMatrix()
    t+=0.005
    if frameCount<=200:
        saveFrame('fr###.gif')
    else:
        print('Saved')
