import os.path
import json

class Agent:

 def __init__(self, data):
  self.data = data

  for name,value in data.items():
   setattr(self, name, value)

 

def main():
 # get json data
 for data in json.load(open(os.path.dirname(__file__)+"/../data/agents-100k.json")):
    agent = Agent(data)
    print(agent.language)


main()
