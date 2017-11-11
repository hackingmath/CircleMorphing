'''Circle Morphing a la Shiffman
November 10, 2017'''

circle_points = []
triangle_points = []

num_of_points = 105 #divisible by 3
rad = 200 #radius of circle
v1 = PVector(0,-rad)
v2 = PVector(rad/2*sqrt(3),rad/2)
v3 = PVector(-rad/2*sqrt(3),rad/2)
side1 = v2 - v1
side2 = v3 - v2
side3 = v1 - v3
steps = 60 #increments of the morphing
step = 0
ds = 1 #velocity?
#fill morphing points list with 0's
morph_points = [0 for i in range(num_of_points)]

def setup():
    global circle_points, triangle_points,num_of_points,rad
    size(600,600)
    sidepts = num_of_points/3
    #side 1:
    #1 segment of the side:
    seg = side1.div(sidepts)
    #seg = PVector(side1.x/num_of_points,side1.y/num_of_points)
    triangle_points.append(v1)
    for n in range(1,sidepts):
        print(seg)
        pt = triangle_points[-1] + seg
        triangle_points.append(pt)
            
    #side 2:
    #1 segment of the side:
    seg2 = side2.div(sidepts)
    triangle_points.append(v2)
    for n in range(1,sidepts):
        pt = triangle_points[-1] + seg2
        triangle_points.append(pt)
            
    #side 3:
    #1 segment of the side:
    seg3 = side3.div(sidepts)
    triangle_points.append(v3)
    for n in range(1,sidepts):
        pt = triangle_points[-1] + seg3
        triangle_points.append(pt)
        
    #circle points
    for i in range(num_of_points):
        circle_points.append(PVector(rad*cos(i*TWO_PI/num_of_points-PI/2),
                                     rad*sin(i*TWO_PI/num_of_points-PI/2)))
    
def draw():
    global circle_points, triangle_points,num_of_points,rad,step,morph_points,ds
    background(255)
    translate(width/2,height/2)
    
    for i,t in enumerate(triangle_points):
        path = PVector(circle_points[i].x - t.x,
                       circle_points[i].y - t.y)
        seg = path.div(steps)
        morph_points[i] = t + step*seg
        
    #draw the morph points
    strokeWeight(4)
    noFill()
    beginShape()
    for p in morph_points:
        vertex(p.x,p.y)
        #ellipse(p.x,p.y,10,10)
    endShape(CLOSE)
    
    '''#draw the triangle
    noFill()
    beginShape()
    for p in triangle_points:
        vertex(p.x,p.y)
        ellipse(p.x,p.y,10,10)
    endShape(CLOSE)
    
    
    fill(0,255,0)
    #draw circlepoints:
    for p in circle_points:
        ellipse(p.x,p.y,5,5)

    noFill()
    ellipse(0,0,2*rad,2*rad)
    fill(255,0,0)
    ellipse(v1.x,v1.y,10,10)
    ellipse(v2.x,v2.y,10,10)
    ellipse(v3.x,v3.y,10,10)'''
    step += ds
    if step == 60 or (step == 0 and ds < 0):
        ds = -ds