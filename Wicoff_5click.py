import graphics
from graphics import Rectangle
from graphics import Point
from graphics import Polygon
win=graphics.GraphWin("5Click",600,300)
win.setBackground("cyan")

p=win.getMouse()
p2=win.getMouse()
py=p.getY()
px=p.getX()
p2y=p2.getY()
p2x=p2.getX()
fifth=(p2x-px)/5
df=fifth/2
fwin=df/2
myrect=Rectangle((p),(p2))
myrect.setFill("gray")
myrect.draw(win)
door=win.getMouse()
dy=door.getY()
dx=door.getX()
dl=Point((dx-df),dy)
dr=Point((dx+df),dy)
dll=Point(dx+df,py)
dlr=Point(dx-df,py)
mydoor=Polygon(dl,dlr,dll,dr)
proof=Point(px,p2y)
mydoor.draw(win)
mydoor.setFill("red")
windp=win.getMouse()
windx=windp.getX()
windy=windp.getY()
windll=Point(windx-fwin,windy-fwin)
windur=Point(windx+fwin, windy+fwin)
window=Rectangle(windll,windur)
window.setFill("yellow")
window.draw(win)
roof=Polygon (p2,proof,win.getMouse())
roof.setFill("orange")
roof.draw(win)
print(door)
print(dx)
print(df)

print(dy)
