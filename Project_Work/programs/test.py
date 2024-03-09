import argparse

parser = argparse.ArgumentParser(description="This is description of program")
parser.add_argument('--alt',type=float,help='description of arg1')
parser.add_argument('--lat',type=float,help='description of arg2')
parser.add_argument('--lon',type=float,help='description of arg2')

args = parser.parse_args()

altitude = args.alt
latitude = args.lat
longitude = args.lon

def display():
    print(altitude)
    print(latitude)
    print(longitude)

display()    