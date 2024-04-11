import physicsBody
import numpy as np

class tank(physicsBody.physicsBody):
    def __init__(self,fuelMass,fuelDensity,tankRadius,tankHeight):
        self.fuelMass = fuelMass #amount of fuel in kg
        self.fuelDensity = fuelDensity
        self.tankRadius = tankRadius
        self.tankHeight = tankHeight
        
        
        super().__init__()
        self.mass = 0
        
        
    def getFuelMass(self):
        return self.fuelMass
        
    def setFuelAmount(self,m):
        self.fuelMass = m
        self.recalculateCenterOfMass()
        
    def addFuelMass(self,m):
        self.fuelMass+=m
        if self.fuelMass < 0:
            self.fuelMass = 0
        self.recalculateCenterOfMass()
        
    def getTotalMass(self):
        return self.mass+self.fuelMass
        
    def recalculateCenterOfMass(self):
        self.centerOfMass = np.array([0,0,self.tankHeight/2-self.fuelMass*(self.tankRadius**2)*np.pi*self.fuelDensity/2]) #assuming no sloshing and the fluid as zylinder filling the tank from bottom to some level 