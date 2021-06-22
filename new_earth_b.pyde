def setup():
    size(600,400)
    strokeWeight(1)
    stroke(20)

t,collection=-90,[]
'''
def spiral1():
    r=100
    x=r*cos(radians(t))-r
    y=r*2*sin(radians(t))
    if (x**2+y**2)>10000:
        collection.append(PVector(x,y))
    beginShape()
    for i in collection:
        #stroke(20,40,160)
        vertex(i.x,i.y)
    endShape()'''

        
def y(t):
    return sin(radians(t))*140

def lengthx(t):
    return 220*cos(radians(t))
            
def draw():
    global t
    background(255)
    translate(width/2,height/2)
    #fill(20)    #Change colour to some blue
    circle(0,0,200)
    noFill()    
    ellipse(0,y(t),lengthx(t),20)
    ellipse(0,-y(t),lengthx(t),20)
    ellipse(y(t),0,20,lengthx(t))
    ellipse(-y(t),0,20,lengthx(t))
    t+=1
    if t<361:
        saveFrame('fr###.gif')
    else:
        print"saved"
