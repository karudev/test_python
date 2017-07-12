import os.path
import json
import math

class Agent:

 def __init__(self, position, **data):
  self.data = data
  self.position = position

  for name,value in data.items():
   setattr(self, name, value)

class Position:
  
 def __init__(self, longitude_degrees, latitude_degrees):
  self.longitude_degrees = longitude_degrees
  self.latitude_degrees = latitude_degrees

 @property
 def longitude(self):
  return self.longitude_degrees * math.pi / 180
 
 @property
 def latitude(self):
  return self.latitude_degrees * math.pi / 180
 
class Zone:
 ZONES = []
 MIN_LONGITUDE_DEGREES = -180
 MAX_LONGITUDE_DEGREES = 180
 WIDTH_DEGREES = 1
 HEIGHT_DEGREES = 1
 MIN_LATITUDE_DEGREES = -90
 MAX_LATITUDE_DEGREES = 90
     
 def __init__(self, corner1, corner2):
  self.corner1 = corner1
  self.corner2 = corner2
  self.inhabitants = 0

 @classmethod
 def initialize_zones(cls):
  for latitude in range(cls.MIN_LATITUDE_DEGREES,cls.MAX_LATITUDE_DEGREES,cls.HEIGHT_DEGREES):
   for longitude in range(cls.MIN_LONGITUDE_DEGREES,cls.MAX_LONGITUDE_DEGREES,cls.WIDTH_DEGREES):
    bottom_left_corner = Position(longitude, latitude)
    top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
    zone = Zone(bottom_left_corner, top_right_corner)
    cls.ZONES.append(zone)
    print(len(cls.ZONES))
    

def main():
 # Init zone
 Zone.initialize_zones()

 # get json data
 for data in json.load(open(os.path.dirname(__file__)+"/../data/agents-100k.json")):
    longitude_degrees = data.pop("longitude")
    latitude_degrees = data.pop("latitude")

    position = Position(longitude_degrees, longitude_degrees)
    agent = Agent(position, **data)
#    print("Longitude : "+str(agent.position.longitude)+" Latitude : "+str(agent.position.longitude))


main()
