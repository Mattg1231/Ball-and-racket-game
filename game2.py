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
    v=300
    a=45


    window = Tk() 
    canvas = Canvas(window,width=L,height=L,bg="white")
    canvas.pack()
    #creating window
    
    racket1=Racket(mapping,canvas,L/10,L/60,)
    racket2=Racket(mapping,canvas,L/10,L/60,False)
    #creating racket 

    ball1=Ball(mapping,canvas,0,mapping.get_ymin()+racket1.Ly+mapping.get_width()/120,v,a)
    #creating ball

    t=0               # real time between event
    up=True #this is used to switch the key bindings
    racket2.activate()#activates racket 2. This is the first to play
    while True:
        t=t+0.01 #real time between events- in second
        racket=0 #real total time- in second
        side=ball1.update_xy(t,racket1.Ly,racket2.Ly)# Update ball position and return collision event
        window.update()   # update the graphic (redraw)
        if(up):
            canvas.bind("<Button-1>",lambda e:racket2.shift_left())
            canvas.bind("<Button-3>",lambda e:racket2.shift_right())
        else:
            canvas.bind("<Button-1>",lambda e:racket1.shift_left())
            canvas.bind("<Button-3>",lambda e:racket1.shift_right())
        #binding buttons to the move methods
        if side!=0:
            t=0 # reinitialize the local time
            if side==2: #checks to see if hit top and if it hits the racket, not then break loop
                up=False #changes up and checks to see to activate or deactivate rackets
                racket2.deactivate()
                racket1.activate()
                ball1.angle=-1*(0.349065875*(random.uniform(1,9)-1)+0.174533)#gives an angle between -10 and -170 degrees
                if (ball1.x<racket2.x-racket2.Lx/2 or ball1.x>racket2.x+racket2.Lx/2):
                    racket=2
                    break
            if side==1: #checks if hit bottom and if it hits the racket, not then break loop
                up=True #changes up and checks to see to activate or deactivate rackets
                racket1.deactivate()
                racket2.activate()
                ball1.angle=0.349065875*(random.uniform(1,9)-1)+0.174533#gives an angle between 10 and 170 degrees
                if (ball1.x<racket1.x-racket1.Lx/2 or ball1.x>racket1.x+racket1.Lx/2):
                    racket=1
                    break
        time.sleep(0.01)  # wait 0.01 second (simulation time)
    print("Game over for racket %s!"%racket)
    window.mainloop()   
if __name__=="__main__":
    main()
