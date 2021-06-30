def periodicFunction(u):
    return map(sin(TWO_PI*u),-1,1,2,8)

def offset(x,y):
    return 0.01*(x**2+y**2)
    
def setup():
    size(600,600)
    textSize(11)
    fill("#00FF00")
    smooth(8)
    
numFrames=60
p=['0','1']

def draw():
    background(20)
    t=1.0*frameCount/numFrames
    #print t
    m=30
    for i in range(m):
        for j in range(m):
            rand=map(noise(i+t),0,1,height*1/2,height)
            x=map(i,0,m-1,0,width)
            y=map(j,0,m-1,0,height)
            #print str(x)+' '+ str(y)
            s=periodicFunction(t-offset(x,y))
            r=0 if s<5 else 1
            fill(0,255,0,map(rand-y,rand,0,255,100))
            #text(p[0],10,10)
            if y<rand:
                text(p[r],x,y)
    '''if frameCount<=numFrames:
        saveFrame('fr###.gif')
    else:
        print('Saved')'''
        
