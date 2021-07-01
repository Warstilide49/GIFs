def setup():
    size(640,640)
    rectMode(CENTER)
    fill(20)
    noStroke()
    #stroke(20)
    #strokeWeight(1)
    smooth(4)
    
numFrames=100

def triangles(large, effect, moving):
    triangle(0, effect+moving, large/2, large/2+moving, -large/2, large/2+moving) #DOWN WILL GO UP
    triangle(effect+moving ,0, large/2+moving , large/2, large/2+moving, -large/2) #RIGHT LEFT
    triangle(0, -effect-moving, -large/2, -large/2-moving, large/2, -large/2-moving) #UP DOWN
    triangle(-effect-moving,0, -large/2-moving, large/2, -large/2-moving, -large/2)  #LEFT RIGHT

def trial(t):
    for i in range(2):
        for j in range(2):
            x=map(i,0,8, width/2-width/8, width/2+width/8)
            y=map(i,0,8, width/2-width/8, width/2+width/8)
            pushMatrix()
            translate(x,y)
            triangles(t,width/8,effect)
            popMatrix()
                
def draw():
    background(255)
    delay=2.2
    t=1.0*frameCount/numFrames
    for i in range(13):
        for j in range(13):
            if (i+j)%2==0:
                x=map(i,0,11, -5*width/16, width+width/16)
                y=map(j,0,11, -5*width/16, height+width/16)
                effect=width/8*abs(sin(PI*t/4)) if t<=2 else width/8
                if t<=delay:
                    moving=0
                elif delay<t<delay+2:
                    moving=width/8*abs(sin(PI*(t-delay)/4))
                else:
                    moving=width/8
                pushMatrix()
                translate(x,y)
                triangles(width/8,effect,moving)
                popMatrix()
                
    '''if frameCount<=numFrames*4.5:
        print(frameCount)
        saveFrame("fr###.gif")
    else:
        print("Saved")'''

    
