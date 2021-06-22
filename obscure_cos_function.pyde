t=0
k=200/TAU

def setup():
    size(600,350)
    stroke(0)
    

def f(x):
    return (cos(x)-abs(cos(x)))*cos(x*96+t)/2
        
def draw():
    scale(2)
    global t
    translate(50,25)
    background(255)
    rect(0,0,200,100)
    for a in range(199,0,-1):
        line(a,50+f(a/k)*k,a+1,50-f((a+1)/k)*k)
    t+=PI/96
    if frameCount<97:
        saveFrame("fr###.gif")
    else:
        print("Saved")
