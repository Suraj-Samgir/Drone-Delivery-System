from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import qr
import decimal

#Connect to the vehicle
import argparse
parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
parser.add_argument('--alt',type=str,help='description of arg1')
parser.add_argument('--lat',type=str,help='description of arg2')
parser.add_argument('--lon',type=str,help='description of arg2')
args = parser.parse_args()

connection_string = args.connect
alt = float(args.alt) 
lat = float(args.lat)
lon = float(args.lon)

print("Connection to the vehicle on %s"%connection_string)
vehicle = connect(connection_string,wait_ready=False)
vehicle.wait_ready(True, timeout=300)

#function the take off
def arm_and_takeoff(tgt_altitude):
	print("Arming Motors")
	
	while not vehicle.is_armable:
		time.sleep(1)
	
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True
	
	print("Takeoff")
	vehicle.simple_takeoff(tgt_altitude) #actual takeoff of drone
	
	#wait to reach the target altitude
	while True:
		altitude = vehicle.location.global_relative_frame.alt
		
		if altitude >= tgt_altitude -1:
			print("Altitude reached")
			break
		time.sleep(1)
		
#..Main Program


arm_and_takeoff(alt)

#..set the default speed
vehicle.airspeed = 7

#Go to waypoint 1
print("Go to way point 1")



wp1 = LocationGlobalRelative(lat,lon,alt)

vehicle.simple_goto(wp1)
#while True:
	#print(vehicle.location.global_relative_frame.lat , " ",vehicle.location.global_relative_frame.lon )
	#if vehicle.location.global_relative_frame.lat == lat and vehicle.location.global_relative_frame.lon == lon :
	        #break
	        	
#..Here you can do all you want..
time.sleep(20)

while True:
	if qr.qr_recognition() == False:
		print("Wrong qr code , please try again ")
		time.sleep(3)
	else:
		break

#vehicle.mode = VehicleMode('LAND')

#while True:
	#if vehicle.location.global_relative_frame.alt == 0:
		#print("Succesfully delivered..Coming back")
		#break
		
#time.sleep(30)
		
#arm_and_takeoff(10)
#..Coming back

vehicle.mode = VehicleMode("RTL")

time.sleep(10) # here to run the qr recognition code for start...

#close connection
vehicle.close()
		
		
		
		
