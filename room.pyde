from opensimplex import OpenSimplex

def setup():
    size(600,600,P3D)
    stroke(255)
    noFill()
    smooth(8)
    
def triangle_points(radius,npoints,inter_points):
    angle = TWO_PI / npoints
    my_points=[]
    a=0
    while a < TWO_PI:
        sx = sin(a) * radius
        sy = cos(a) * radius
        my_points.append(PVector(sx,sy))
        a += angle
    for i in range(len(my_points)):
        for j in range(inter_points):
            p=1.0*j/inter_points
            x=lerp(my_points[i].x,my_points[(i+1)%3].x,p)
            y=lerp(my_points[i].y,my_points[(i+1)%3].y,p)
            my_points.append(PVector(x,y))
    return my_points          
 
def x_vertices(t):
    #seed=[[1234,1235,1236],[1515,1516,1517],[1012,1013,1014]]
    return 0.5*width + 100*n.noise2d(seed+ random_radius*cos(TWO_PI*t),random_radius*sin(TWO_PI*t))

    
def y_vertices(t):
    return 0.5*width + 25*n.noise2d(seed + random_radius*cos(TWO_PI*t),random_radius*sin(TWO_PI*t))
    
m=1000
numFrames=120
delay_factor=-1.5
n=OpenSimplex()
random_radius=0.4
triangle_inter_points=20
seed=1234
base_triangle=triangle_points(100,3,triangle_inter_points)
end_triangle=triangle_points(600,3,triangle_inter_points)
r1=75
r2=200
inter_points=20

def draw():
    background(20)
    #translate(width/2,height/2) #figure a way to make triangle in centre
    t=1.0*frameCount/numFrames
    #for i in base_triangle:
       # point(i.x,i.y)
    for i in range(m):
        p=1.0*i/m
        stroke(20+250*p)
        for j in range(inter_points+1):
            q=1.0*j/(inter_points+1)
            canvas_lerped=lerp(0,width+width/inter_points,q)
            x=lerp(canvas_lerped,x_vertices(t-delay_factor*pow(p,3.0)),p)
            y=lerp(0,y_vertices(t-delay_factor*pow(p,3.0)),p)
            point(x,y)
            x=lerp(0,x_vertices(t-delay_factor*pow(p,3.0)),p)
            y=lerp(canvas_lerped,y_vertices(t-delay_factor*pow(p,3.0)),p)
            point(x,y)
            x=lerp(width,x_vertices(t-delay_factor*pow(p,3.0)),p)
            y=lerp(canvas_lerped,y_vertices(t-delay_factor*pow(p,3.0)),p)
            point(x,y)
            x=lerp(canvas_lerped,x_vertices(t-delay_factor*pow(p,3.0)),p)
            y=lerp(height,y_vertices(t-delay_factor*pow(p,3.0)),p)
            point(x,y)
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")'''
