from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *

class Racket:
    def __init__(self,mapping,canvas,Lx,Ly,pos=True):
            self.mapping=mapping
            self.canvas=canvas
            self.Lx=Lx
            self.Ly=Ly
            self.x=0
            if(pos):
                self.y=mapping.get_ymin()+Ly/2
            else:
                self.y=mapping.get_ymax()-Ly/2
            self.rectangle= canvas.create_rectangle(self.mapping.get_i(self.x-Lx/2),self.mapping.get_j(self.y-Ly/2),self.mapping.get_i(self.x+Lx/2),self.mapping.get_j(self.y+Ly/2),fill="black")
    #This is my constructor. rectangle is found by using the mapping method get i and get j in order to map it
    def shift_left(self):
        if(self.x-self.Lx/2>self.mapping.get_xmin()):
            self.x=self.x-self.Lx/2
            self.canvas.move(self.rectangle,-self.Lx/2,0)
    #This is my shift left. First checks if it can move left then uses canvas.move to move it lx/2
    def shift_right(self):
        if(self.x+self.Lx/2<self.mapping.get_xmax()):
            self.x=self.x+self.Lx/2
            self.canvas.move(self.rectangle,self.Lx/2,0)
    #This is my shift right. First checks if it can move right then uses canvas.move to move it lx/2
    def activate(self):
        self.canvas.itemconfig(self.rectangle,fill="red")
    #changes the color to red
    def deactivate(self):
        self.canvas.itemconfig(self.rectangle,fill="black")
    #changes the color to black
    
def main():

    ###### create a mapping
    swidth=input("Enter window size in pixels (press Enter for default 600): ")
    if swidth=="":
        width=600
    else:
        width=int(swidth)
    L=width
    mapping=Mapping_for_Tkinter(-L/2,L/2,-L/2,L/2,L)
    #creating mapping
      
    ##### create a window, canvas, and racket
    window = Tk() 
    canvas = Canvas(window,width=L,height=L,bg="white")
    canvas.pack()
    #creating window

    racket=Racket(mapping,canvas,L/10,L/60)
    #creating racket 

    ####### bind mouse click with action
    
    canvas.bind("<Button-1>",lambda e:racket.shift_left())
    canvas.bind("<Button-3>",lambda e:racket.shift_right())
    #binding buttons to the move methods
    window.mainloop()   
    #looping main

if __name__=="__main__":
    main()

