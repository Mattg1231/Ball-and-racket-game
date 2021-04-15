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

    text=canvas.create_text(40,20,text="Score: 0",fill="black",font=("Courier",10))
    #creating score
    
    racket1=Racket(mapping,canvas,L/10,L/60,)
    racket2=Racket(mapping,canvas,L/10,L/60,False)
    #creating racket 

    ball1=Ball(mapping,canvas,0,mapping.get_ymin()+racket1.Ly+mapping.get_width()/120,v,a)
    ball2=Ball(mapping,canvas,0,mapping.get_ymax()-racket2.Ly-mapping.get_width()/120,v,-a)
    #creating balls
            

    window.bind("<a>",lambda event:racket2.shift_left())
    window.bind("<d>",lambda event:racket2.shift_right())

    window.bind("<Left>",lambda event:racket1.shift_left())
    window.bind("<Right>",lambda event:racket1.shift_right())
    #binding the keys. Player 1 is bottom. Player 2 is top.

    t1=0               # real time between event
    t2=0
    score=0           # keeps the total score 

    while True:
        t1=t1+0.01 #real time between events- in second for ball 1
        t2=t2+0.01 #real time between events- in second for ball 2
        racket=0 #says which racket it is
        side1=ball1.update_xy(t1,racket1.Ly,racket2.Ly)# Update ball position and return collision event for ball1
        side2=ball2.update_xy(t2,racket1.Ly,racket2.Ly)# Update ball position and return collision event for ball1
        canvas.itemconfig(text,text="Score: "+str(score))#updates score
        window.update()   # update the graphic (redraw)

        #binding buttons to the move methods
        if side1!=0:
            t1=0 # reinitialize the local time
            if side1==2: #checks to see if hit top and if it hits the racket, not then break loop
                ball1.angle=-1*(0.349065875*(random.uniform(1,9)-1)+0.174533)#gives an angle between -10 and -170 degrees
                if (ball1.x<racket2.x-racket2.Lx/2 or ball1.x>racket2.x+racket2.Lx/2):
                    racket=2
                    break
                else:
                    score+=1#adds score
            if side1==1: #checks if hit bottom and if it hits the racket, not then break loop
                ball1.angle=0.349065875*(random.uniform(1,9)-1)+0.174533#gives an angle between 10 and 170 degrees
                if (ball1.x<racket1.x-racket1.Lx/2 or ball1.x>racket1.x+racket1.Lx/2):
                    racket=1
                    break
                else:
                    score+=1#adds score
        if side2!=0:
            t2=0 # reinitialize the local time
            if side2==2: #checks to see if hit top and if it hits the racket, not then break loop
                ball2.angle=-1*(0.349065875*(random.uniform(1,9)-1)+0.174533)#gives an angle between -10 and -170 degrees
                if (ball2.x<racket2.x-racket2.Lx/2 or ball2.x>racket2.x+racket2.Lx/2):
                    racket=2
                    break
                else:
                    score+=1#adds score
            if side2==1: #checks if hit bottom and if it hits the racket, not then break loop
                ball2.angle=0.349065875*(random.uniform(1,9)-1)+0.174533#gives an angle between 10 and 170 degrees
                if (ball2.x<racket1.x-racket1.Lx/2 or ball2.x>racket1.x+racket1.Lx/2):
                    racket=1
                    break
                else:
                    score+=1#adds score
        time.sleep(0.01)  # wait 0.01 second (simulation time)
    canvas.itemconfig(text,text="Player %s loses. Score: %s"%(racket,score),font=("Courier",25))
    canvas.coords(text,300,250)
    window.update()
    window.mainloop()   
if __name__=="__main__":
    main()
