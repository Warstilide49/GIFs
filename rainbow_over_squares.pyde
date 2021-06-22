def setup():
    size(600,600)
    frameRate(60)

a=0
x,y=25,25    
def draw():
    global x,y,a
    background(0)
    stroke(255)
    strokeWeight(1.5)
    for i in range(14):
        for j in range(14):
            '''if random(100)<1:
                fill(random(255),random(255),random(255))
            else:
                noFill()'''
            square(25+i*30+i*10,25+j*30+j*10,30)
    strokeWeight(6)
    stroke(random(255),random(128),random(255))
    line(300,300,x,y)
    x=300+cos(a)*275
    y=300+sin(a)*275
    a+=0.015
    if frameCount<=428:
        saveFrame("fr###.gif")
    else:
        print("Saved")
