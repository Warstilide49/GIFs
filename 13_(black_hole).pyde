def setup():
    size(600,400)
    
t=0
collection,collection2=[],[]
collection3=[]

def spiral1(flag):
    r=100
    if flag==0:
        x=r*cos(radians(t))-r
    else:
        x=-r*cos(radians(t))+r
    y=r*2*sin(radians(t))
    if (x**2+y**2)>10000:
        collection.append(PVector(x,y))
    beginShape()
    for i in collection:
        #stroke(20,40,160)
        vertex(i.x,i.y)
    endShape()
'''    
def spiral2():
    r=100
    x=0.7*r*cos(radians(t))-0.7*r
    y=r*2*sin(radians(t))
    if (x**2+y**2)>10000:
        collection2.append(PVector(x,y))
    beginShape()
    for i in collection2:
        #stroke(20,40,160)
        vertex(i.x,i.y)
    endShape()

def spiral3():
    r=100
    x=0.5*r*cos(radians(t))-0.5*r
    y=r*2*sin(radians(t))
    if (x**2+y**2)>10000 :
        collection3.append(PVector(x,y))
    beginShape()
    for i in collection3:
        #stroke(20,40,160)
        vertex(i.x,i.y)
    endShape()
'''    
def draw():
    global t,collection
    background(255)
    translate(width/2,height/2)
    fill(20)    #Change colour to some blue
    circle(0,0,200)
    noFill()
    n=10
    spiral1(0)
    spiral1(1)
    '''elif 360<t<720:
        spiral2()
    elif 360*2<t<360*3:
        spiral3()
    elif 360*3<t<360*4:
        spiral1()'''
    t+=1
    '''if t<360:
        saveFrame('fr###.gif')
    else:
        print('Saved')'''
