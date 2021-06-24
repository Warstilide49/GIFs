def periodicFunction(u):
    return map(sin(TWO_PI*u),-1,1,2,8)

def offset(x,y):
    if x<width/2 and y<height/2:
        return 0.01*dist(x,y,0,0)
    elif x>width/2 and y<height/2:
        return 0.01*dist(x,y,width,0)
    elif x<width/2 and y>height/2:
        return 0.01*dist(x,y,0,height)
    else:
        return 0.01*dist(x,y,width,height)
    
def setup():
    size(600,600)
    stroke(255)


def draw():
    background(20)
    t=1.0*frameCount/60
    #print t
    m=40
    for i in range(m):
        for j in range(m):
            x=map(i,0,m-1,0,width)
            y=map(j,0,m-1,0,height)
            #print str(x)+' '+ str(y)
            s=periodicFunction(t-offset(x,y))
            strokeWeight(s)
            point(x,y)
    if frameCount<=60:
        saveFrame('fr###.gif')
    else:
        print('Saved')
            
