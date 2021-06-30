def setup():
    size(600,600)
    #stroke("#E81010")
    noFill()
    smooth(8)
    blendMode(LIGHTEST)
    
def hexagon(radius,npoints):
    angle = TWO_PI / npoints
    beginShape()
    a=0
    while a < TWO_PI:
        sx = sin(a) * radius
        sy = cos(a) * radius
        vertex(sx,sy)
        a += angle
    endShape(CLOSE)

collection=["#F50A2D","#960AF5","#0A5AF5","#0AF5A0","#6BF50A","#F5EA0A"]
#collection=["#E81010","#E810B6","#7A0EC9","#1A0EC9","#0EC963","#C2C90E","#C9490E"]

def polygon(radius,npoints):
    angle = TWO_PI / npoints
    l=list()
    a=0
    while a < TWO_PI:
        sx = sin(a) * radius
        sy = cos(a) * radius
        s=PVector(sx,sy)
        l.append(s)
        a += angle
    return l    

def hexagon_creation(m,vertices,t,q):
    stroke(collection[q])
    c=map(t,1/numFrames,1,0,6)
    a=floor(map(t,1/numFrames,1,0,6))
    b=floor(map(c%1,0,1,0,50))
    if a<6:
        for i in range(b):
            x = lerp(vertices[a].x, vertices[(a+1)%6].x, i/50.0)
            y = lerp(vertices[a].y, vertices[(a+1)%6].y, i/50.0)
            line(vertices[a].x,vertices[a].y,x,y)
        for i in range(a):
            line(vertices[i].x,vertices[i].y,vertices[i+1].x,vertices[i+1].y)
    else:
        #stroke("#20E3DE")
        hexagon(m,6)
    '''elif a==5:
        for i in range(b):
            stroke(collection[a])
            x = lerp(vertices[5].x, vertices[0].x, i/20.0)
            y = lerp(vertices[5].y, vertices[0].y, i/20.0)
            line(vertices[5].x,vertices[5].y,x,y)
        for i in range(a):
            stroke(collection[i])
            line(vertices[i].x,vertices[i].y,vertices[i+1].x,vertices[i+1].y)'''

numFrames=60
r=300
q=0
def draw():
    background(20)
    t=1.0*frameCount/numFrames
    z=map(t,1/numFrames,1,1,11)
    
    #scale(z)
    k=6
    for i in range(k):
        p=1.0*(i+t)/k
        pushMatrix()
        translate(width/2,height/2)
        #rotate(PI*p)
        vertices=polygon(460*p,6)
        for j in range(6):
            real=vertices[j:]+vertices[0:j]
            hexagon_creation(460*p,real,p,j)
        popMatrix()
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
    else:
        print("Saved")'''
