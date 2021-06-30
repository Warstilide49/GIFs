def setup():
    size(600,600)
    stroke(255)
    
def x_vertex(r,t):
    return r*cos(2*PI*t)

def y_vertex(r,t):
    return r*sin(2*PI*t)

numFrames=180
r=250
delay_factor=-4.1
K=1000
boundaries=21

def draw():
    background(20)
    t=1.0*frameCount/numFrames
    translate(width/2,height/2)
    for i in range(K):
        p=1.0*i/K
        stroke(255,50+100*sin(PI*p))
        for j in range(boundaries):
            angle=map(j,0,boundaries,0,2*PI)
            x=lerp(x_vertex(r,t-delay_factor*pow(p,3.0)),r*cos(angle),p)
            y=lerp(y_vertex(r,t-delay_factor*pow(p,3.0)),r*sin(angle),p)
            point(x,y)
        '''x=lerp(x_vertex(-r,t-delay_factor*pow(p,3.0)),-r,p)
        y=lerp(y_vertex(-r,t-delay_factor*pow(p,3.0)),0,p)
        point(x,y)'''
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("saved")'''
