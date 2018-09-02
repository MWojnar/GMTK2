import json
from pathlib import Path
from AssetLoader import AssetLoader
from Platform import Platform
from Spike import Spike
from Checkpoint import Checkpoint
from PullOrb import PullOrb
from PullOrbTether import PullOrbTether
from Rocket import Rocket
from Bouncy import Bouncy

class LevelLoader():
    def __init__(self, world, fileName):
        self.world = world
        self.fileName = fileName
        self.levelObjects = []
        self.roomWidth = 960
        self.roomHeight = 540
        
    def loadLevel(self):
        levelFile = open(self.fileName, "r")
        jsonString = levelFile.read()
        parsedJson = json.loads(jsonString)
        
        for instance in parsedJson["Level"]:
            for item in instance:
                if item == "Room":
                    self.roomHeight = instance[item]["Height"]
                    self.roomWidth = instance[item]["Width"]
                    
                if item == "Name":
                    if instance[item] == "Satellite Platform":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        imageIndex = instance["Image Index"]
                        
                        platform = Platform(self.world, x, y)
                        self.levelObjects.append(platform)
                        
                    elif instance[item] == "Spikes":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        imageIndex = instance["Image Index"]
                        
                        spike = Spike(self.world, x, y)
                        self.levelObjects.append(spike)
                        
                    elif instance[item] == "Checkpoint":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        
                        checkpoint = Checkpoint(self.world, x, y)
                        self.levelObjects.append(checkpoint)
                        
                    elif instance[item] == "Pull Orb":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        
                        #pullOrb = PullOrb(self.world, x, y)
                        #self.levelObjects.append(pullOrb) FIXME: Needs player to function?
                              
                    elif instance[item] == "Attract Tether":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        
                        #pullOrbTether = PullOrbTether(self.world, x, y)
                        #self.levelObjects.append(pullOrbTether) FIXME: Same as above
                              
                    elif instance[item] == "End Rocket":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        
                        rocket = Rocket(self.world, x, y)
                        self.levelObjects.append(rocket)
                              
                    elif instance[item] == "Earth":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                              
                    elif instance[item] == "Bouncy":
                        y = instance["Y"]
                        x = instance["X"]
                        angle = instance["Angle"]
                        
                        bouncy = Bouncy(self.world, x, y)
                        self.levelObjects.append(bouncy)
                              
                    else:
                        pass
                    
        return self.levelObjects
                
        
        
