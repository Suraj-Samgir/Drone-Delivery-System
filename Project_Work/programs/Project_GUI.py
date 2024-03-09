from tkinter import *
import os

root = Tk()
root.title("Drone Operation GUI")
root.geometry("700x350")
root.maxsize(700,350)
root.minsize(700,350)

#Creating frames to hold the components...

f4 = Frame(root,borderwidth=6)
f4.pack(side=TOP,fill=X)

f3 = Frame(root,borderwidth=6)
f3.pack(side=BOTTOM,fill=X)

f1 = Frame(root,borderwidth=6)
f1.pack(side=RIGHT,fill=Y)    

f2 = Frame(root,borderwidth=6)
f2.pack(side=LEFT,fill=Y)

#creating heading for the GUI...
heading = Label(f4,text="- Enter Altitude & Location and Start the Delivery -",font="serif 15 bold",background="cyan")
heading.pack(padx=100,pady=(25,0))

#creating labels for desired input
alt_label = Label(f2,text="Enter the desired altitude : ",font="serif 15 bold")
alt_label.pack(padx=(20,0),pady=25)

lat_label = Label(f2,text="Enter the destination latitude : ",font="serif 15 bold")
lat_label.pack(padx=(20,0))

lon_label = Label(f2,text="Enter the destination longitude : ",font="serif 15 bold")
lon_label.pack(padx=(20,0),pady=(25,0))

#variable for holding the user input...
getalt = DoubleVar()
getlat = DoubleVar()
getlon = DoubleVar()

#Creating entry widget i.e. input box to take input into the created variables
alt_input = Entry(f1,textvariable=getalt,font="serif 15 bold",background="pink")
lat_input = Entry(f1,textvariable=getlat,font="serif 15 bold",background="pink")
lon_input = Entry(f1,textvariable=getlon,font="serif 15 bold",background="pink")

#Packing all the entry widgets to display them on the screen
alt_input.pack(padx=(0,100),pady=27)
lat_input.pack(padx=(0,100))
lon_input.pack(padx=(0,100),pady=(27,0))

def start():
    #To assign the values to the alt,lat and lon variables
    #To establish connection with the sitl
    altitude = getalt.get()
    latitude = getlat.get()
    longitude = getlon.get()
  
    result2=os.system(f"sim_vehicle.py --map --console")

    result=os.system(f"python drone_fly.py --connect 127.0.0.1:14550 --alt {altitude} --lat {latitude} --lon {longitude}")
    
    if(result!=0):
        print("Error! Unable to run the drone script file")
    if(result2!=0):
        print("Error! Unable to run the simulation script file")
    
start_button = Button(f3,text="Start Delivery",foreground="white",background="red",font="serif 15 bold",command=start)
start_button.pack(padx=100,pady=(0,30))

root.mainloop()
