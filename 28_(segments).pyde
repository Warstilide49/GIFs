def setup():
    size(600,600)
    noStroke()
    frameRate(60)
    
numFrames=60

def segments(r1,r2,t):
    m=10
    j=0
    k=0
    for i in range(m):
        angle=map(i+1,0,m,0,360)
        fill("#368FEA")
        beginShape()
        while j<angle-10:
            x1=r2*cos(radians(j))
            y1=r2*sin(radians(j))
            x2=r1*cos(radians(j))
            y2=r1*sin(radians(j))
            vertex(x1,y1)
            vertex(x2,y2)
            j+=1
        endShape(CLOSE)
        # fill(20)
        # beginShape()
        # vertex(0,0)
        # while k<angle-4:
            
        #     vertex(x1,y1)
        #     k+=1
        # endShape(CLOSE)
        j,k=angle,angle
            

def draw():
    background(20)
    t=1.0*frameCount/numFrames
    translate(width/2,height/2)
    r=170*abs(sin(0.2*PI*t))
    r2=130*abs(sin(0.2*PI*t))
    r3=90*abs(sin(0.2*PI*t))
    for i in range(10):
        r=i*30*abs(sin(0.2*PI*t))
        segments(r+10,r+30,t)

    # inner_circle(t)
    # outer_circle(t)
    
    '''if frameCount<=300:
        saveFrame("fr###.gif")
    else:
        print"Saved"'''
