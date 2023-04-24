from graphics import *

from graphics import *
x=int(input("window size x"))
y=int(input("window size y"))

    #"""Dieview is a widget that displays a graphical representation of a standard six-sided die."""
win = GraphWin('Final Exam',x,y)


win.setCoords(0,0,10,10)
class dieView:
    




        def __makePip(self,x,y):
            pip=Circle(Point(x,y),self.psize)
            pip.setFill(self.background)
            pip.setOutline(self.background)
            pip.draw(self.win)
            return pip
        def setValue(self,value):
            "set this die to display value."
            #turn all pips off
            self.pip1.setFill(self.background)
            self.pip2.setFill(self.background)
            self.pip3.setFill(self.background)
            self.pip4.setFill(self.background)
            self.pip5.setFill(self.background)
            self.pip6.setFill(self.background)
            self.pip7.setFill(self.background)
            

        def __init__(self,win,center,size):
            """Create the view of a die,e.g.:
                d1=DieView(myWin, Point(40,50),20)
            creates a die centered at (40,50) having sides of length 20."""
            #first define some standard values.
           
            self.background="white"
            self.foreground="black"
            self.psize=.1 #radius of pip
            hsize=size/2.0 #half size of die
            offset=.6*hsize


            #square for the face
            cx,cy=center.getX(), center.getY()
            p1=Point(cx-hsize, cy-hsize)
            p2=Point(cx-hsize, cy-hsize)
            rect=Rectangle(p1,p2).draw(win)
            #rect.draw(win)
            rect.setFill(self.background)

            #Create 7 circles for pip
            self.pip1=self.__makePip(cx-offset,cy-offset)
            self.pip2=self.__makePip(cx-offset,cy)
            self.pip3=self.__makePip(cx-offset,cy+offset)
            self.pip4=self.__makePip(cx,cy)
            self.pip5=self.__makePip(cx+offset, cy-offset)
            self.pip6=self.__makePip(cx+offset,cy)
            self.pip7=self.__makePip(cx+offset,cy+offset)
            #an initial value
            self.setValue(1)
       


