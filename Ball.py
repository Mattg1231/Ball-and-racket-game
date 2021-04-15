from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time

class Ball:
    def __init__(self,mapping,canvas,x0,y0,velocity,angle):
        self.mapping=mapping
        self.canvas=canvas
        self.x0=x0
        self.y0=y0
        self.velocity=velocity  
        self.angle=math.radians(angle)
        self.x=x0
        self.y=y0
        self.r=mapping.get_width()/120
        self.circle=canvas.create_oval(self.mapping.get_i(x0-self.r),self.mapping.get_j(y0-self.r),self.mapping.get_i(x0+self.r),self.mapping.get_j(y0+self.r),fill="blue")
    #constructor used to initialize all the attributes in the function. Also create oval using canvas and methods from mapping
    def update_xy(self,t,Ly=0,Ly1=0):
        f=0
        self.x=self.x0+self.velocity*math.cos(self.angle)*t
        self.y=self.y0+self.velocity*math.sin(self.angle)*t
        if(self.x<=self.mapping.get_xmin()+self.r or self.x>=self.mapping.get_xmax()-self.r):  
            if(self.x>=self.mapping.get_xmax()-self.r):
                self.angle=(math.pi-self.angle)
                self.x=self.mapping.get_xmax()-self.r
                self.x0=self.x
                self.y0=self.y
                f=4

            else:
                self.angle=(math.pi-self.angle)
                self.x=self.mapping.get_xmin()+self.r
                self.x0=self.x
                self.y0=self.y
                f=3

        if(self.y<=self.mapping.get_ymin()+self.r+Ly or self.y>=self.mapping.get_ymax()-self.r):
            if(self.y<=self.mapping.get_ymin()+self.r+Ly):
                    self.angle=(-self.angle)
                    self.y=self.mapping.get_ymin()+self.r+Ly
                    self.x0=self.x
                    self.y0=self.y
                    f=1

            else:
                self.angle=(-self.angle)
                self.y=self.mapping.get_ymax()-self.r-Ly1
                self.x0=self.x
                self.y0=self.y
                f=2

        self.canvas.coords(self.circle,self.mapping.get_i(self.x-self.r),self.mapping.get_j(self.y-self.r),self.mapping.get_i(self.x+self.r),self.mapping.get_j(self.y+self.r))
        return f
    #update method first updates the x and y cords. After it checks to see if they are out or not. If they are out i set them equal to the bounds,
    #then i set x0 and y0 to the current cords and change my circle cords. At the end I return an int, and if the int is not 0 it hit a boundary
    # which triggers the function in the main method to make the temporary time start over.
    """ to complete """












    

def main(): 
        ##### create a mapping
        swidth=input("Enter window size in pixels (press Enter for default 600): ")
        if swidth=="":
            width=600
        else:
            width=int(swidth)

        L=width
        mapping=Mapping_for_Tkinter(-L/2,L/2,-L/2,L/2,L)
        
        
        ##### User Input 
        data=input("Enter velocity and theta (press Enter for default: 500 pixel/s and 30 degree):")
        if data=="":
            v=500
            a=30
        else:
            datalist=data.split()
            v=int(datalist[0])
            a=int(datalist[1])
        #checks for user input and splits it
        

        
        ##### create a window, canvas and ball object

        
        root = Tk() 
        canvas = Canvas(root,width=L,height=L,bg="white")
        canvas.pack()
        ball1=Ball(mapping,canvas,0,0,v,a)
        #creates ball object

           
        ############################################
        ####### start simulation
        ############################################
        t=0               # real time between event
        t_total=0         # real total time
        count=0           # rebound_total=0
        while True:
            t=t+0.01 #real time between events- in second
            t_total=t_total+0.01 #real total time- in second
            side=ball1.update_xy(t)# Update ball position and return collision event
            root.update()   # update the graphic (redraw)
            if side!=0:
                count=count+1 # increment the number of rebounds
                t=0 # reinitialize the local time
            time.sleep(0.01)  # wait 0.01 second (simulation time)
            if count==10: break # stop the simulation
            
        print("Total time: %ss"%t_total)
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

