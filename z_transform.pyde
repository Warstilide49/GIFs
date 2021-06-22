def setup():
    size(600,600)
    stroke(255)
    noFill()

def nextcomplex(z_previous,z_main):
    ans=(z_previous-z_main)**0.5
    return ans
    
def base(q):
    z_new=[]
    for i in range(360):
        x=r*cos(radians(i))
        y=r*sin(radians(i))
        z_new.append(nextcomplex(complex(x/r,y/r),q))
    return z_new

def transforms(z,q):
    z_new=[]
    beginShape(POINTS)
    for a in z:
        vertex(a.real*r,a.imag*r)
        z_new.append(nextcomplex(complex(a.real,a.imag),q))
    for a in z:
        vertex(-a.real*r,-a.imag*r)
        z_new.append(nextcomplex(complex(-a.real,-a.imag),q))
    endShape()
    return z_new

q=-0.15-0.8j       
r=200
colours=["#FA0808","#FA8108","#FACA08","#BCFA08","#12FA08","#08FA93","#08E0FA","#0876FA","#5B08FA","#B808FA"]
numFrames=150

def draw():
    translate(width/2,height/2)
    background(20)
    t=1.0*frameCount/numFrames
    q=complex(-0.15,-0.8*sin(TWO_PI*t))
    X=base(q)
    for i in range(9):
        stroke(colours[i])
        X=transforms(X,q)
        #pixels
    '''if frameCount<=150:
        print str(frameCount)+' / ' +str(numFrames)
        saveFrame('fr###.gif')
    else:
        print("saved")'''

    
    
        
        
