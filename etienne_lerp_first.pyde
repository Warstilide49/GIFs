from opensimplex import OpenSimplex

def setup():
    size(600,600,P3D)
    stroke(255)
    noFill()
    smooth(8)
    
m=1000
numFrames=130
delay_factor=-1.1
n=OpenSimplex()
random_radius=0.4
number_of_points=3

def x_vertices(t,seed,k):
    required_array=[]
    for i in range(number_of_points):
        required_array.append(0.25*width*(k+1) + 150*n.noise2d(seed[i] + random_radius*cos(TWO_PI*t),random_radius*sin(TWO_PI*t)))
    return required_array
    
def y_vertices(t,seed,k):
    required_array=[]
    for i in range(number_of_points):
        required_array.append(0.25*height + 150*n.noise2d(seed[i] + random_radius*cos(TWO_PI*t),random_radius*sin(TWO_PI*t)))
    return required_array

def draw():
    background(20)
    t=1.0*frameCount/numFrames
    #rect(0.5*width-220,0.75*height-25,440,50)
    for k in range(3):
        seed=[[1234,1235,1236],[1515,1516,1517],[1012,1013,1014]]
        stroke(255)
        ellipse(0.25*width*(k+1),0.75*height,100,50)
        ellipse(0.25*width*(k+1),0.75*height,50,20)
        for i in range(m):
            p=1.0*i/m
            pushStyle()
            strokeWeight(2)
            stroke(20+200*p)
        #stroke(200-150*cos(PI*(50*p*t))) #Snaky type
            x_array=x_vertices(t - delay_factor*p,seed[k],k)
            y_array=y_vertices(t - delay_factor*p,seed[(k+1)%3],k)
            for j in range(number_of_points):
                x=lerp(x_array[j],0.25*width*(k+1),p)
                y=lerp(y_array[j],3*height/4.0,p)
                point(x,y)
            popStyle()
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")'''
