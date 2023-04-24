m0=0
m1=0
m2=0
m3=0
m4=0
m5=0
m6=0
m7=0
m8=0
m9=0


from graphics import *

win = GraphWin('Quiz',700,500)
win.setCoords(-2,-2,12,22)

L = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9]
for i in range(3): 
    L = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9]
    box = Rectangle(Point(4*i,0), Point(4*i+2,L[i]))
    box.setFill('brown')
    box.draw(win)
    score = Text(Point(4*i+1,L[i]+0.5),L[i])
    score.setSize(18)
    score.draw(win)    
    
#Horizontal Axis

for i in range(3):
    
    mark = Text(Point(4*i+1,-1) ,str('Quiz '+str(i+1)))
    mark.draw(win)
