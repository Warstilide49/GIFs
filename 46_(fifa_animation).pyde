from opensimplex import OpenSimplex

class BlueSquare:
    def __init__(self,reach,p,seed,colour1,colour2):#,x,y,colour1,colour2):
        self.centre=PVector(0,0)
        self.colour=color( lerpColor(colour1,colour2, simplexvalue(p,seed) ) )
        self.points=[ [self.centre.x+reach,self.centre.y], [self.centre.x,self.centre.y+reach], [self.centre.x-reach,self.centre.y], [self.centre.x,self.centre.y-reach]]
        self.skew=[1,simplexvalue(p,seed),simplexvalue(p,seed+10),1]
        #self.skew=[1,random(0.3,1),random(0.1,0.2),1]
    def show(self,p):
        # pushMatrix()
        pushStyle()
        fill(self.colour,300.0*pow(p,0.6))
        beginShape()
        for i in range(4):
            vertex(multiplication(self.skew,self.points[i]))
        endShape()
        popStyle()
        
def simplexvalue(p,seed):
    scl=7.0
    return pow((n.noise2d(scl*p,seed)+1)/2.0,2.0)       

def multiplication(matrix1,matrix2):
    return [matrix1[0]*matrix2[0]+ matrix1[1]*matrix2[1],matrix1[2]*matrix2[0] + matrix1[3]*matrix2[1]]

def setup():
    size(600,600)
    noStroke()

quantity=15
numFrames=60
test=[]
n=OpenSimplex()
across=15

a=color(33,143,255) #Favourite colour
b=color(191,217,255)
def creation(p,seed):
    test=[]
    for i in range(quantity):
        test.append(BlueSquare(10,p,seed,a,b))
    return test

#for i in range(quantity):
        #test.append(BlueSquare(10))
        
def draw():
    background(20)
    t=1.0*frameCount/numFrames
    translate(width/2,height/2)
    for dim in range(4):
        rotate(PI/2*dim)
        for i in range(across):
            mapped_across=map(i,0,across,0,height)
            for j in range(quantity):
                p=1.0*(j+t)/quantity
                mine=creation(p,(i+dim)*1000)
                pushMatrix()
                s=map(p,1.0/(numFrames*quantity),1,0.2,1.1)
                x=map(p,1.0/(numFrames*quantity),1,0,-0.5*width-20)
                y=map(p,1.0/(numFrames*quantity),1,0,-0.5*height+mapped_across-20)
                translate(x,y)
                scale(s)
                mine[j].show(p)
                popMatrix()
        
    #print(len(mine))
    '''if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")
    
    '''
