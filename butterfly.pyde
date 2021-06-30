from opensimplex import OpenSimplex

def vector(r,theta):
    return PVector(r*sin(theta)*(2.7182**cos(theta) - 2*cos(4.0*theta)-sin(theta/12.0)**5),-r*cos(theta)*(2.7182**cos(theta) - 2*cos(4.0*theta)-sin(theta/12.0)**5))
    #return PVector(r* 16* pow(sin(theta),3),-r*(13*cos(theta)-5* cos(2*theta)-2*cos(3*theta) - cos(4*theta)))

def setup():
    size(600,600)
    strokeWeight(1)
    stroke(255)
    #smooth(8)
    
n=OpenSimplex()    
r=100
K=5000
numFrames=180
seed=1234
random_radius=500
offset=4
#n.noise2d(seed+ random_radius*cos(TWO_PI*t),random_radius*sin(TWO_PI*t))
colourpalette=["#fde200", "#ef2626", "#5600ae", "#713df5"]

def draw():
    background(20)
    translate(width/2,2*height/3)
    t=1.0*frameCount/numFrames
    f=map(t,1/numFrames,1,0,2*PI)
    for i in range(K):
        #stroke(255,sin(PI*p))
        for j in range(offset):
            stroke(colourpalette[j%4])
            theta=map(i,0,K,f+2*j*PI/16,f+(2*j+1)*PI/16)
            x=vector(r,theta).x
            y=vector(r,theta).y
            point(x,y)
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")
        '''
        
    
    
