def setup():
    size(600,600)
    noStroke()
    textSize(15)
    
dia=20
k=20
numFrames=100

def yin_yang(dia):
    fill(0)
    arc(0,0,dia, dia, PI/2,PI+PI/2)     #Black arc
    fill(255)
    arc(0,0,dia, dia, PI+PI/2,TWO_PI+PI/2)    #White arc
    fill(0)
    circle(0,-dia/4, dia/2)        #Black extension
    fill(255)
    circle(0,dia/4,dia/2)        #White extension
    #Anticlockwise
    fill(0)
    circle(0,dia/4, dia/8)        #Black circle
    fill(255)
    circle(0,-dia/4, dia/8)

def draw():
    background("#C3C9A0")
    t=1.0*frameCount/numFrames
    for i in range(k):
        for j in range(k):
            p= (1.0*i + 1.0*j) / (2*k)
            x=map(i,0,k,width/k,width)
            y=map(j,0,k,width/k,width)
            pushMatrix()
            translate(x,y)
            rotate(2*PI*(t+p))
            yin_yang(dia)
            popMatrix()
            
