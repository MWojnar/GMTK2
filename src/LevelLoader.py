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
                    self.world.roomHeight = instance[item]["Height"]
                    self.world.roomWidth = instance[item]["Width"]
                    
                if item == "Name":
                    y = instance["Y"]
                    x = instance["X"]
                    angle = instance["Angle"]
                    if instance[item] == "Satellite Platform":
                        imageIndex = instance["Image Index"]
                        
                        platform = Platform(self.world, x, y)
                        self.levelObjects.append(platform)
                        
                    elif instance[item] == "Spikes":
                        imageIndex = instance["Image Index"]
                        
                        spike = Spike(self.world, x, y)
                        self.levelObjects.append(spike)
                        
                    elif instance[item] == "Checkpoint":
                        
                        checkpoint = Checkpoint(self.world, x, y)
                        self.levelObjects.append(checkpoint)
                        
                    elif instance[item] == "Pull Orb":
                        
                        pass
                        #pullOrb = PullOrb(self.world, x, y)
                        #self.levelObjects.append(pullOrb) FIXME: Needs player to function?
                              
                    elif instance[item] == "Attract Tether":
                        
                        pass
                        #pullOrbTether = PullOrbTether(self.world, x, y)
                        #self.levelObjects.append(pullOrbTether) FIXME: Same as above
                              
                    elif instance[item] == "End Rocket":
                        
                        rocket = Rocket(self.world, x, y)
                        self.levelObjects.append(rocket)
                              
                    elif instance[item] == "Earth":
                        pass
                              
                    elif instance[item] == "Bouncy":
                        
                        bouncy = Bouncy(self.world, x, y)
                        self.levelObjects.append(bouncy)
                              
                    else:
                        pass
                    
        return self.levelObjects
                
        
        
