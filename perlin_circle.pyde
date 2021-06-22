noisepara=1.2
phase=0

def setup():
    size(600,600)
    #frameRate(30)
 
def draw():
    global phase
    background(20)
    translate(width/2,height/2)
    stroke(255)
    noFill()
    beginShape()
    #noisepara=map(noise(phase),0,1,4,4.2)
    for i in range(0,360,10):
        xoff=map(cos(radians(i+phase)),-1,1,0,noisepara)
        yoff=map(sin(radians(i+phase)),-1,1,0,noisepara)
        r=map(noise(xoff,yoff),0,1,100,200)
        x=r*cos(radians(i))
        y=r*sin(radians(i))
        vertex(x,y)
    endShape(CLOSE)
    phase+=1
    
    if frameCount<361:
        saveFrame("fr###.gif")
    else:
        print("Saved")
    
