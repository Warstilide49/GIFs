def setup():
    size(600,600)
    frameRate(5)
    noStroke()
    
def draw():
    background(255)
    for i in range(30,height,30):
        for j in range(30,width,30):
            if random(100)<50:
                fill(random(255),random(255),random(255),64)
                ellipse(i,j,60,60)
    '''if frameCount<=50:
        saveFrame("fr###.gif")
    else:
        print("Saved")'''
