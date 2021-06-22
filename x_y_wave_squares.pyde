def periodicFunction(u):
    return map(sin(TWO_PI*u),-1,1,1,5)

def offset(x,y):
    return x+y
    
def setup():
    size(600,600)
    stroke(255)
    #noFill()

def draw():
    background(20)
    t=1.0*frameCount/60
    #print t
    m=15
    for i in range(m):
        for j in range(m):
            x=map(i,0,m-1,0,width)
            y=map(j,0,m-1,0,height)
            #print str(x)+' '+ str(y)
            s=periodicFunction(t-offset(x,y))
            pushMatrix()
            translate(x,y)
            #strokeWeight(s)
            scale(s)
            square(-3,-3,6)
            #point(x,y)
            popMatrix()
    if frameCount<=60:
        saveFrame("fr###.gif")
    else:
        print("saved")
