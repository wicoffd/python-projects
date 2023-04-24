from graphics import *
x=int(input("window size x"))
y=int(input("window size y"))

    #"""Dieview is a widget that displays a graphical representation of a standard six-sided die."""
win = GraphWin('Final Exam',x,y)


win.setCoords(0,0,10,10)
class dieView:
    

    def __init__(self,win,center,size):
        """Create the view of a die,e.g.:
            d1=DieView(myWin, Point(40,50),20)
        creates a die centered at (40,50) having sides of length 20."""
        #first define some standard values.
        self.win=win
        self.background="white"
        self.foreground="black"
        self.psize=.1 #radius of pip
        hsize=size/2.0 #half size of die
        offset=.6*hsize






