def setup():
    size(600,600,P2D)
    noStroke()
    strokeWeight(1)
    smooth(8)

def ease(p, g):
    if p < 0.5:
        return 0.5 * pow(2*p, g)
    else:
        return 1 - 0.5 * pow(2*(1 - p), g)

def remaining_circles(n,t):
    for i in range(1,n):
        pushStyle()
        if 2 < t <=2+i*1.0/n:
            fill(map(t,2,2 + i*1.0/n, colour1, colour2))
        if t>2+i*1.0/n:
            fill(colour2)
        circle(path_rad* cos(t/2 +3*PI/2 + i*2*PI/n), path_rad* sin(t/2 +3*PI/2 +i*2*PI/n), small_radius)
        popStyle()
        
def trial(t,radius):
    #small_radius=30
    if t>=1:
        circle(path_rad*cos(t/2+3*PI/2), path_rad*sin(t/2+3*PI/2), small_radius)
    else:
        pushMatrix()
        increasing_radius=map(ease(t,4),0 ,1 ,0, path_rad)
        translate(increasing_radius*cos(t/2+3*PI/2),increasing_radius*sin(t/2+3*PI/2))
        circle(0,0,map(ease(t,4), 0, 1, radius, small_radius))
        popMatrix()

numFrames=100
main_radius=300
origin=PVector(0,0)
k=4
path_rad=250
small_radius=30
colour1=255
colour2=20

def draw():
    background(colour2)
    t=1.0*frameCount/numFrames
    if t>2:
        fill(map(t,2,3,colour1,colour2))
    else:
        fill(colour1)
    translate(width/2,height/2)
    trial(t,900)
    remaining_circles(30,t)
    '''if frameCount<=numFrames*3:
        saveFrame("fr###.gif")
        print(str(frameCount))
    else:
        print("Saved")'''
