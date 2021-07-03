def setup():
    size(600,600,P3D)
    stroke(255)
    #strokeWeight(0.2)
    noFill()
    smooth(8)
    colorMode(HSB)

numFrames=60    
a=10
b=28
c=8.0/3
base=PVector(0.1,0,0)
dt=0.01
n=3

def vertices():
    required_array=[]
    base=PVector(0.1,0,0)
    for i in range(numFrames*35):
        dx = a*(base.y-base.x)*dt
        dy = (base.x*(b-base.z)-base.y)*dt
        dz = (base.x*base.y-c*base.z)*dt
        base=PVector((base.x+dx),base.y+dy, (base.z+dz))
        required_array.append(base)
    return required_array

collection=vertices()        
h=0

def Lorenz(angle,t, h_value):
    global h
    h=h_value
    pushMatrix()
    pushStyle()
    rotateX(PI*t/2 + angle)
    rotateY(PI*t/2 + angle)
    rotateZ(PI*t/2 + angle)
    strokeWeight(0.2)
    scale(5)
    beginShape()
    for i in range(len(collection)):
        h+=0.1
        stroke(h,255,180)
        vertex(collection[i].x, collection[i].y, collection[i].z)
        if h>255:
            h=0
    h=0
    endShape()
    popMatrix()
    popStyle()

# def Lorenz(angle,t, h_value):
#     global h
#     h=h_value
#     pushMatrix()
#     pushStyle()
#     rotateX(PI*t/2 + angle)
#     rotateY(PI*t/2 + angle)
#     rotateZ(PI*t/2 + angle)
#     scale(5)
#     p=map(t,0,2,0,1)
#     for i in range(len(collection)):
#         strokeWeight(0.4)
#         if i+1>=len(collection):
#             i=0
#         h+=0.1
#         if h>255:
#             h=0
#         stroke(h,255,180)
#         #stroke(h)
#         new_x = lerp(collection[i].x, collection[i+1].x , p)
#         new_y = lerp(collection[i].y, collection[i+1].y , p)
#         new_z = lerp(collection[i].z, collection[i+1].z , p)
#         #point(collection[i].x, collection[i].y, collection[i].z)
#         point(new_x,new_y,new_z)
#         #line( new_x, new_y, new_z, new_x+1, new_y+1, new_z+1)
#     h=0
#     popMatrix()
#     popStyle()


def draw():
    t=1.0*frameCount/numFrames
    background(20)
    translate(width/2,height/2)
    for i in range(n):
        Lorenz(2*PI*i/n , t, 50*i)
    '''if frameCount<=4*numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")'''
