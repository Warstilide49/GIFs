def setup():
    size(600,600)
    stroke(255)
    strokeWeight(1.5)

#Straight from @beesandbombs
def ease(p,g):
    if p<0.5:
        return 0.5 * pow(2*p,g)
    else:
        return 1-0.5* pow(2*(1-p),g)
    
eyes=[]
faceRadiusIn=280
faceRadiusOut=270
eyeLength=30
eyeRes=50
numFrames=200
boundaryRes=310
happy,sad=[],[]

def draw():
    background(20)
    translate(width/2,height/2)
    t=1.0*frameCount/numFrames
    p=map(sin(2*PI*t),-1,1,0,1)
    happy, sad, rightEye, wink ,leftEye, lwink=[],[],[],[],[],[]
    for i in range(boundaryRes):               #Boundary                    
        for j in range(boundaryRes):
            x=map(i,0,boundaryRes,-width/2+width/boundaryRes,width/2)
            y=map(j,0,boundaryRes,-height/2+height/boundaryRes,height/2)
            if faceRadiusOut**2<= x**2+y**2 <= faceRadiusIn**2:
                point(x,y)
    for i in range(eyeRes):             #eyes
        pushMatrix()
        translate(-width/5,-height/5)
        for j in range(eyeRes):                   #Left eye
            x=map(i,0,eyeRes,-eyeLength,eyeLength)
            y=map(j,0,eyeRes,-eyeLength,eyeLength)
            if x**2+ y**2<= eyeLength**2:
                leftEye.append(PVector(x,y))
                #point(x,y)
        popMatrix()
        pushMatrix()
        translate(width/5,-height/5)
        for j in range(eyeRes):                       #Right eye
            x=map(i,0,eyeRes,-eyeLength,eyeLength)
            y=map(j,0,eyeRes,-eyeLength,eyeLength)
            if x**2+ y**2<= eyeLength**2:
                rightEye.append(PVector(x,y))
        popMatrix()
    for i in range(eyeRes):
        pushMatrix()
        translate(width/5,-height/5)
        for j in range(eyeRes):
            x=map(i,0,eyeRes,-1.2*eyeLength,1.2*eyeLength)
            angle=map(i,0,eyeRes,0,1)
            y=map(j,0,eyeRes,-15*sin(PI*angle)+eyeLength/2,eyeLength/2)       #Trials
            wink.append(PVector(x,y))
                #point(x,y)
        popMatrix()
        pushMatrix()
        translate(-width/5,-height/5)
        for j in range(eyeRes):
            x=map(i,0,eyeRes,-1.2*eyeLength,1.2*eyeLength)
            angle=map(i,0,eyeRes,0,1)
            y=map(j,0,eyeRes,-15*sin(PI*angle)+eyeLength/2,eyeLength/2)       #Trials
            lwink.append(PVector(x,y))
                #point(x,y)
        popMatrix()
    for i in range(boundaryRes):                  #Happy and sad arrays
        for j in range(boundaryRes):
            x=map(i,0,boundaryRes,-width/2,width/2)
            y=map(j,0,boundaryRes,-height/2,height/2)
            if 20*(-y+150) < 0.05*(x**2) < 20*(-y+150)+300 and -width/4<=x<=width/4:
                happy.append(PVector(x,y))
            if 20*(y-100) < 0.05*(x**2) < 20*(y-100)+300 and -width/4<=x<=width/4:
                sad.append(PVector(x,y))
    #print(len(happy)-len(sad[0:-18]))
    remainder=len(happy)-len(sad)
    remainder2=len(rightEye)-len(wink)
    remainder3=len(leftEye)-len(lwink)
    for i in range(abs(remainder)):
        if remainder>0:
            happy.pop(0)
        else:
            sad.pop(0)
            
    for i in range(abs(remainder2)):
        if remainder2>0:
            rightEye.pop(0)
        else:
            wink.pop(0)
            
    for i in range(abs(remainder3)):
        if remainder3>0:
            leftEye.pop(0)
        else:
            lwink.pop(0)
    #new_mouth=sad.remove(sad[0:remainder] )        #Trials
    #new_eye=wink[0:remainder2]
    #print(len(leftEye,
    for i in range(len(happy)):
        x=lerp(happy[i].x,sad[i].x,p)
        y=lerp(happy[i].y,sad[i].y,p)
        stroke(255-150*(sin(2*PI*t)))
        point(x,y)
    for i in range(len(wink)):
        pushMatrix()
        translate(width/5,-height/5)
        x=lerp(wink[i].x,rightEye[i].x,p)
        y=lerp(wink[i].y,rightEye[i].y,p)
        stroke(255-150*(sin(2*PI*t)))
        point(x,y)
        popMatrix()
    for i in range(len(lwink)):
        pushMatrix()
        translate(-width/5,-height/5)
        x=lerp(lwink[i].x,leftEye[i].x,p)
        y=lerp(lwink[i].y,leftEye[i].y,p)
        stroke(255-150*(sin(2*PI*t)))
        point(x,y)
        popMatrix()
    if frameCount<=numFrames:
        saveFrame("fr###.gif")
        print(frameCount)
    else:
        print("Saved")
