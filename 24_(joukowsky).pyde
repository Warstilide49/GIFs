def setup():
    size(600,600)
    strokeWeight(1)
    background(20)
    noFill()

def transform(input):
    return input+(1/input)

collection=[]
def structure():
    global collection
    t=0
    beginShape()
    stroke("#405BEA")
    while t<TWO_PI:
        r=1
        x=r*cos(2*PI*t)+0.18
        y=r*sin(2*PI*t)-0.51
        z=complex(x,y)
        vertex(transform(z).real*75,transform(z).imag*75)
        if t*100%15==0:
            collection.append(z)
        t+=0.01
    endShape()

def follower(time,k):
    global collection
    t=0    
    beginShape()
    stroke("#D1BD56")
    while t<PI/32:
        r=1+sin(2*PI*k)/16
        x=r*cos(2*PI*time)+0.18
        y=r*sin(2*PI*time)-0.51
        z=complex(x,y)
        vertex(transform(z).real*75,transform(z).imag*75)
        t+=0.01
        time+=0.01
    endShape()
   
def mousePressed(): 
    global dont,count
    count+=1
    if count%2==0:
        dont=1
        print t
    else:
        dont=0
t=0
dont=0
count=0
def draw():
    background(20)
    stroke(255)
    global t
    translate(width/2,height/2)
    #structure() #the airfoil
    for i in range(10):
        j=map(i,0,9,0.5,1.5)
        #offset=map(i,0,9,0,2*PI)
        follower(t,j)
        follower(t+PI,j)
        follower(t+2*PI,j)
        follower(t+3*PI,j)
        follower(t+4*PI,j)
    # follower(t,6.67) #the arcs moving around
    # follower(t+PI/4,7.8)
    # follower(t+PI/2,3.8)
    # follower(t+PI,4.65)
    if dont==0:
        t+=0.005
    if frameCount<=200:
        saveFrame("fr###.gif")
    
    #print "X: ",mouseX," Y: ",mouseY
