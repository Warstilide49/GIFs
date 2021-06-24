def setup():
    size(600,600)
    noFill()
    strokeWeight(2)
    stroke(150,0,40)
    
a=0
collection1,collection2=[],[]

def first(a):
    stroke(150,0,40)
    global collection1
    beginShape()
    for i in collection1:
        vertex(i.x,i.y)
    endShape()
    
    x=220*sin(radians(a)+PI)
    y=120*sin(4*radians(a)+PI/16+PI)
    collection1.append(PVector(x,y))
    if len(collection1)>40:
        collection1.pop(0)
    
def Second(a):
    stroke(0,150,40)
    global collection2
    beginShape()
    for i in collection2:
        vertex(i.x,i.y)
    endShape()
    
    x=220*sin(radians(a))
    y=120*sin(2*radians(a)+PI/4)
    collection2.append(PVector(x,y))
    if len(collection2)>40:
        collection2.pop(0)
        
def draw():
    global a
    background(20)
    translate(width/2,height/2)
    first(a)
    Second(a)
    a+=2
    if frameCount<361:
        saveFrame("fr###.gif")
    else:
        print('saved')
