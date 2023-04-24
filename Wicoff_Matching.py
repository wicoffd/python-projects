import random
from graphics import *
from random import random
win = GraphWin('Quiz',700,500)
win.setCoords(-2,-2,12,22)
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
m10=0
m11=0
m12=0
m13=0
m14=0

M= [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14]
for i in range(3):
    
    mark = Text(Point(4*i+1,-1) ,str('Matches '+str(i+1)))
    mark.draw(win)

L = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14]
for i in range(3): 
    L = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9]
    box = Rectangle(Point(4*i,0), Point(4*i+2,M[i]))
    box.setFill('brown')
    box.draw(win)
    score = Text(Point(4*i+1,L[i]+0.5),L[i])
    score.setSize(18)
    score.draw(win)  

for i in range (0,10):

    r=str(random())
    r2=str(random())
    rs=r[2:]
    r2s=r2[2:]
    for i in range(14):
        
        if rs[i-1:i]==r2s[i-1:i]:
        
    
            M[i]=M[i]+1
        else:
             print(False)
             if rs[i-1:i]==r2s[i-1:i]:
                M[i]=M[i]+1
             else:
                print("1match")
