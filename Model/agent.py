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
 

def main():
 # get json data
 for data in json.load(open(os.path.dirname(__file__)+"/../data/agents-100k.json")):
    longitude_degrees = data.pop("longitude")
    latitude_degrees = data.pop("latitude")

    position = Position(longitude_degrees, longitude_degrees)
    agent = Agent(position, **data)
    print("Longitude : "+str(agent.position.longitude)+" Latitude : "+str(agent.position.longitude))


main()
