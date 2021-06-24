def setup():
    size(800, 800)
    background(20)
    smooth()
    stroke(180,30,0)
    noFill()
    colorMode(RGB, 100, 10, 10)
    frameRate(1)
    
def triangleSier(x1, y1, x2, y2,x3,y3,n):
    if ( n > 0 ):
        #fill(0, 128/n, 128)
        triangle(x1, y1, x2, y2, x3, y3)
        h1 = (x1+x2)/2.0
        w1 = (y1+y2)/2.0
        h2 = (x2+x3)/2.0
        w2 = (y2+y3)/2.0
        h3 = (x3+x1)/2.0
        w3 = (y3+y1)/2.0
        triangleSier(x1, y1, h1, w1, h3, w3, n-1)
        triangleSier(h1, w1, x2, y2, h2, w2, n-1)
        triangleSier(h3, w3, h2, w2, x3, y3, n-1)
  
n=1

def draw():
    global n
    translate(200,175)
    triangleSier(0, 350, 200, 0, 400, 350, n)
    n+=1
    if frameCount<9:
        saveFrame("fr###.gif")
    else:
        print("Saved")
