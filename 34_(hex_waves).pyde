def setup():
    size(600,600)
    stroke("#C1A410")
    strokeWeight(1.5)
    fill("#EAC818")
    smooth(8)

def polygon(x,y,radius,npoints):
    angle = TWO_PI / npoints
    beginShape()
    a=0
    while a < TWO_PI:
        sx = x + sin(a) * radius
        sy = y + cos(a) * radius
        vertex(sx, sy)
        a += angle
    endShape(CLOSE)

def periodicFunction(u):
    return map(cos(TWO_PI*u),-1,1,0.2,1.8)

def offset(x,y):
    return 0.03*(tan(1.33*(x**2+y**2)))
    #return 0.01*dist(x,y,width/2,height/2)

numFrames=150
collection=["#FF0000","#00FF00","#0000FF"]
col=0

def draw():
    global col    
    background("#41713F")
    #background("#365A5D")
    t=1.0*frameCount/numFrames
    #print t
    m=19
    #col=floor(map(sin(2*PI*(t-offset(x,y))),-1,1,0,3))
    for i in range(m):
        for j in range(m):
            pushMatrix()
            x=map(i,0,m-1,75,width-75)
            y=map(j,0,m-1,75,height-75)
            s=periodicFunction(t-offset(x,y))
            col=floor(map(sin(2*PI*(t-offset(x,y))),-1,1,0,2.9))
            translate(x,y)
            scale(1.5*sin(s))
            #fill(collection[col])
            #fill(collection[col])
            polygon(0,0,6,6)
            popMatrix()
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
    else:
        print"Saved"'''
