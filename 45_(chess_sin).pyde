class WeirdSquare:
    def __init__(self,x,y,t):
        self.pos=PVector(x,y)
        self.state=0
        self.t=t
        
    def show(self):
        t1=ease(self.t,2)
        rect(self.pos.x,self.pos.y,(width/8* cos(2*PI*t1)),width/8)

def ease(p, g):
    if p < 0.5:
        return 0.5 * pow(2*p, g)
    else:
        return 1 - 0.5 * pow(2*(1 - p), g)
    
def setup():
    size(600,600)
    noStroke()
    fill(0)
    
numFrames=200
def draw():
    background(255)
    t=1.0*frameCount/numFrames
    for i in range(9):
        for j in range(9):
            if (i+j)%2!=0:
                x=map(i,0,8,0,width)
                y=map(j,0,8,0,height)
                a=WeirdSquare(x,y,t)
                a.show()
                # x=map(i,0,8,0,width)
                # y=map(j,0,8,0,height)
                # square(x,y,width/8)
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")'''
