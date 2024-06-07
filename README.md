# Title : Automated Drone Delivery System

# Description :

 Automated drone delivery system will enable us 
to transport a package within a particular weight from source 
to its destination. The device will help faster delivery of packages 
as the aviation transport would not have problem of traffic 
congestion. This project can solve many time complex issues like 
transporting medical equipment in time and saving lives. As the 
delivering items with drone is much more cheaper than that of 
a bike it can be a big market of business for various food delivery 
items and package transfer services.

# Work Done :

A. Setting up the OS environment
To perform the drone operations virtually the Operating 
System or environment used would be Linux OS. The Ubuntu 
Linux system is been setup with all the essential modules to 
support drone operations.

B. Setting up the GCS
The Ground Control Station (GCS) is used to establish the 
control over the drone operations as a centralized controller.
The MAVProxy software is used as the Ground Control 
Station which helps to provide commands for operating the 
drone.

C. Setting up the Communication Protocol
The communication protocol framework is established to 
transfer the command signals/packets between the GCS and 
drone to perform operations specified by the commands. 
MAVLink protocol has been used as the communication 
protocol.

D. Setting up the Virtual Drone
To test the drone operations, virtual drone is been setup. 
The Software In The Loop (SITL) is been used for 
establishing the virtual drone along with the integrated 
environment to navigate the drone on map and get the time to 
time drone status on the console log window.

E. Setting up the Programming Environment
To code the scripts for the drone operations, the python 
interpreter is been used. Several necessary python modules 
and libraries are been installed.

F. Assembling the Ardupilot Script
The Ardupilot script is 700,000 lines of code script which 
is cloned from the git repository. It is used to run the specific
C++ code files by analyzing the command received from the 
GCS to perform the specified drone operation.

G. Drone hardware specifications
The following is the technical data of A2212/13T
• 2 to 3 Li-Poly 
• 6 to 10 NiCad/NiMH 
• 1000 RPM/V for Kv
• 80% maximum efficiency
• 4 to 10 A, Maximum Efficiency Current (>75%)
• Current without load: 0.5A @10V
• 0.090 ohms for resistance
• Maximum Current: 60S at 13A
• 150W maximum wattage
• Weight: 1.86 oz/52. 7 g
• 28 mm bell length x 28 mm dia.
• Size of the shaft: 3.2 mm
• Model Weight: 300–800g/10.5–28.2 oz 
• Poles: 14

# How to Execute 

1. 
