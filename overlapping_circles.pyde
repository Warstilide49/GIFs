def setup():
    size(600,600)
    noFill()
    strokeWeight(4)
    stroke(255)

r,t=500,0
def draw():
    global r,t
    background(20)
    translate(width/2,height/2)
    #blendMode(DIFFERENCE)
    if r>30:
        for i in range(1,30):
            circle(0,0,r+i*30)
        r-=2
    else:
        x=82*sin(2*PI*t/300)
        y=82*cos(2*PI*t/300)
        for i in range(1,30):
            circle(x,0,r+i*30)
            circle(-x,0,r+i*30)
        t+=1
    '''if frameCount<=535:
        saveFrame("fr###.gif")
    else:
        print("Saved")'''
