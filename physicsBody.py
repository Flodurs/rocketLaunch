import numpy as np

class physicsBody:
    def __init__(self):
        self.mass = 0
        
        #primarly for visualization purpose
        #rocket is made from stacked zylinders
        self.radius = 0
        self.height = 0
        
        
        # every physicsBody coordinate system is in its geometrical center, in this simulation for starters their gonna be assumed symmetrical
        # centerOfMass being at (0,0,0) thus means it's in the geometrical center
        # for the simulation this is gonna be relevant since i want the centerOfMass of the tanks change while they drain 
        # naming convention is x,y,z
        # rocket on launchpad is gonna pe positioned with +z facing upwards
        self.centerOfMass = np.zeros(3)

    def getMass(self):
        return self.mass
        
    def getCenterOfMass(self):
        return self.centerOfMass
        
    def setCenterOfMass(self,com):
        self.centerOfMass = com
        
    def setMass(self,m):
        self.mass = m
        
    def getHeight(self):
        return self.height
    
    def setHeight(self,h):
        self.height = h
        
    def getRadius(self):
        return self.radius
        
    def setRadius(self,r):
        self.radius = r