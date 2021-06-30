def setup():
    size(600,600,P3D)
    noStroke()
k=55
R=200
numFrames=300
count=0

def vectorTransformSouth(a):
    x=2.0*(R**2)*(a.x)/(a.x**2 + a.y**2 + R**2)
    y=2.0*(R**2)*(a.y)/(a.x**2 + a.y**2 + R**2)
    z=R*(R**2- a.x**2 -a.y**2)/(a.x**2 +a.y**2 +R**2)
    return PVector(x,y,z)

def vectorTransformNorth(a):
    x=-2.0*(R**2)*(a.x)/(a.x**2 + a.y**2 + R**2)
    y=-2.0*(R**2)*(a.y)/(a.x**2 + a.y**2 + R**2)
    z=R*(3*R**2- a.x**2 -a.y**2)/(a.x**2 +a.y**2 +R**2)
    return PVector(x,y,z)

def draw():
    global count
    background(20)
    t=1.0*frameCount/numFrames
    translate(width/2,height/2,0)
    p=map(sin(2*PI*(t)),0,1,0,1)
    l,new=[],[]
    #rotateY(2*PI*t)
    for i in range(k):
        for j in range(k):
            x=map(i,0,k,-width/2+1.0*width/k,width/2)
            y=map(j,0,k,-height/2+1.0*height/k,height/2)
            a=PVector(x,y,0)
            l.append(a)
    for i in l:
        new.append(vectorTransformSouth(i))
        #new.append(vectorTransformNorth(i))
    #print(len(l))
    # for i in new:
    #    point(i.x,i.y,i.z)
    for i in range(k**2):
        x=lerp(l[i].x,new[i].x,p)
        y=lerp(l[i].y,new[i].y,p)
        z=lerp(l[i].z,new[i].z,p)
        pushMatrix()
        fill(180)
        translate(x,y,z)
        circle(0,0,3.3)
        popMatrix()
    #print(count)
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print('Saved')'''
