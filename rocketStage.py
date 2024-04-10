import engine
import tank
import physicsBody
import numpy as np

class rocketStage(physicsBody.physicsBody):
    def __init__(self):
    
        self.velocity = np.zeros(3) 
        self.rotationalVelocity = np.zeros(3)
        
        self.position = np.zeros(3)
        self.rotation = np.zeros(3)
        
        
        self.engines = [engine.engine() for i in range(3)]
        self.oxTank = tank.tank(100000,1141,3,20)
        self.fuelTank = tank.tank(100000,1000,3,20)
        
        
        
        
        
        
        #Atmospheric Drag 
        self.Cd = 0.001
        self.referenceArea = 10
        self.atmosphereDensity = 1
        
        
        
        
        

        self.launchFlag = 0
        super().__init__()
    
    def launch(self):
        self.launchFlag = 1
        
    def update(self,delta_t):
        #updateMass
        self.mass = self.oxTank.getTotalMass()+self.fuelTank.getTotalMass()+sum([engine.getMass() for engine in self.engines])+1000
    
    
        #fire engines
        if self.launchFlag and self.oxTank.getFuelMass() > 0 and self.fuelTank.getFuelMass() > 0:
            for engine in self.engines:
                engineResult = engine.fire(delta_t)
                self.applyImpulseChange(engineResult[0])
                self.oxTank.addFuelMass(-engineResult[1])
                self.fuelTank.addFuelMass(-engineResult[2])
                
        #external forces
        self.applyImpulseChange(np.array([0,0,0.001*-25.81*self.getTotalMass()]))
        self.applyImpulseChange(np.array([0,0,-np.sign(self.velocity[2])*self.Cd*self.referenceArea*self.atmosphereDensity*(self.velocity[2]**2)*0.5]))

        
        #update location and attidude
        self.position+=self.velocity*delta_t
        self.rotation+=self.rotationalVelocity*delta_t
    
        
    def applyImpulseChange(self,impulseChange):
        self.velocity+=impulseChange/self.mass
        
    def applyMoment(self,):
        pass
        
    def getTotalMass(self):
        return self.mass
        
    def getTotalFuelMass(self):
        return self.oxTank.getFuelMass()+self.fuelTank.getFuelMass()
        
    def printState(self):
        print("------------------------")
        print("Velocity: "+str(self.velocity))
        print("Oxidzer Mass: " +str(self.oxTank.getFuelMass()))
        print("Fuel Mass: " +str(self.fuelTank.getFuelMass()))
    
    def getPosition(self):
        return self.position
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    