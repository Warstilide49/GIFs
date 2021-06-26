def setup():
    size(600,600)
    stroke(20)

def polygon(x,y,radius,npoints):
    angle = TWO_PI / npoints
    beginShape()
    a=0
    while a < TWO_PI:
        sx = x + cos(a) * radius
        sy = y + sin(a) * radius
        vertex(sx, sy)
        a += angle
    endShape(CLOSE)


def re(n):
    if frameCount<=n:
        saveFrame("fr###.gif")
    else:
        print("Saved")
        
def come(t):
    stroke(255-t*9.8)
    
def gone(z):
    stroke(20+z*9.79)

z=0
def effect(top,bottom,w,time):
    global z
    noFill()
    erase_length=time*10
    n=50 #no. of stuff
    if erase_length<(bottom-top):
        stroke(255)
        fill(255)
        rect(-w,(bottom-erase_length),2*w ,erase_length)
        stroke(20)
        line(-w,bottom-erase_length,w,bottom-erase_length)
    else:
        background(255)
        gone(z)
        line(-w,top,w,top)
        z+=0.2
        # for i in range(n):
        #     # if i%2==1:
        #     #     fill(20)
        #     # else:
        #     #     noFill()
        #     x=map(i,0,n-1,-w,w)
        #     y=bottom-erase_length+sin(i)
        #     pushMatrix()
        #     translate(x,y)
        #     stroke(20)
        #     if i!=n-1:
        #         square(0,0,2*w/n)
        #     popMatrix()
        
t=0
recording=0
n=760
def draw():
    noFill()
    strokeWeight(1)
    global t
    background(255)
    translate(width/2,height/2)
    if t<24:
        come(t)
        polygon(0,0,200,10)
        circle(0,0,80)
        polygon(0,0,90,3)
        polygon(0,0,130,4)
        polygon(0,0,165,5)
        polygon(0,0,180,8)
    else:
        polygon(0,0,200,10)
        circle(0,0,80)
        polygon(0,0,90,3)
        polygon(0,0,130,4)
        polygon(0,0,165,5)
        polygon(0,0,180,8)
        effect(-200,200,200,t-24)
    # effect(100,-100,100,t)
    t+=0.1
    print(frameCount)
    if recording==1:
        re(n)
