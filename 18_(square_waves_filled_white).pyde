def periodicFunction(u):
    return map(cos(TWO_PI*u),-1,1,0.2,1.8)

def offset(x,y):
    return 0.01*dist(x,y,width/2,height/2)
    
def setup():
    size(600,600)
    stroke(255)

numFrames=120
collection=["#9400D3","#4B0082","#0000FF","#00FF00","#FFFF00","#FF7F00","#FF0000"]

def draw():
    background(20)
    t=1.0*frameCount/numFrames
    #print t
    m=20
    for i in range(m):
        for j in range(m):
            pushMatrix()
            x=map(i,0,m-1,0,width)
            y=map(j,0,m-1,0,height)
            s=periodicFunction(t-offset(x,y))
            col=floor(map(sin(2*PI*(t-offset(x,y))),-1,1,0,7))
            translate(x,y)
            scale(s)
            #fill(collection[col])
            stroke(collection[col])
            square(0,0,width/(2.5*m))
            popMatrix()
    '''if frameCount<=120:
        saveFrame('fr###.gif')
    else:
        print('Saved')'''
