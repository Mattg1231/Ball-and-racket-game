from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
from Ball import Ball
from Racket import Racket
import time
import random

def main():
    width=600
    L=width
    mapping=Mapping_for_Tkinter(-L/2,L/2,-L/2,L/2,L)
    #creating mapping
      
    ##### create a window, canvas, and racket
    v=200
    a=53


    window = Tk() 
    canvas = Canvas(window,width=L,height=L,bg="white")
    canvas.pack()
    #creating window
    racket=Racket(mapping,canvas,L/10,L/60)
    ball1=Ball(mapping,canvas,0,mapping.get_ymin()+racket.Ly+mapping.get_width()/120,v,a)
    #creating ball
    #creating racket 

    ####### bind mouse click with action
    
    canvas.bind("<Button-1>",lambda e:racket.shift_left())
    canvas.bind("<Button-3>",lambda e:racket.shift_right())

    #binding buttons to the move methods


    t=0               # real time between event
    t_total=0         # real total time
    while True:
        t=t+0.01 #real time between events- in second
        t_total=t_total+0.01 #real total time- in second
        side=ball1.update_xy(t,racket.Ly)# Update ball position and return collision event
        window.update()   # update the graphic (redraw)
        if side!=0:
            t=0 # reinitialize the local time
            if side==2: #checks to see if hit top
                ball1.angle=-1*(0.349065875*(random.uniform(1,9)-1)+0.174533)#gives an angle between -10 and -170 degrees
                ball1.velocity=ball1.velocity*1.25
            if side==1: #checks if hit racket if not then break loop
                if (ball1.x<racket.x-racket.Lx/2 or ball1.x>racket.x+racket.Lx/2):
                    break
        time.sleep(0.01)  # wait 0.01 second (simulation time)
    print("Game over! Total time: %ss"%t_total)
    window.mainloop()   

if __name__=="__main__":
    main()
