import engine
import tank
import physicsBody
import numpy as np
import aerodynamics
import transforms

class rocketStage(physicsBody.physicsBody):
    def __init__(self):
    
        self.velocity = np.zeros(3) 
        self.rotationalVelocity = np.zeros(3)
        
        self.position = np.zeros(3) #in global earth fixed frame
        self.position = np.array([0.0,0.0,6371001.0])
        self.rotation = np.zeros(3) #around center of mass 
        
        self.inertiaTens = np.zeros((3,3))
        
        self.engines = [engine.engine() for i in range(6)]
        self.oxTank = tank.tank(300000,1141,3,20)
        self.fuelTank = tank.tank(300000,1000,3,20)
        
        self.structMass = 20000
        
        
        print("Strukturmasseanteil: " +str(self.structMass/(self.oxTank.getFuelMass()+self.fuelTank.getFuelMass()+self.structMass)))
        
        
        
        #Atmospheric Drag 
        self.Cd = 0.013
        self.referenceArea = 10
        self.atmosphereDensity = 1
        
        
       
        
        

        self.launchFlag = 0
        super().__init__()
    
    def launch(self):
        self.launchFlag = 1
        
    def launch nextStage(self):
        pass
        
    def update(self,delta_t):
        #updateMass
        self.mass = self.oxTank.getTotalMass()+self.fuelTank.getTotalMass()+self.structMass
    
    
        #fire engines
        if self.launchFlag and self.oxTank.getFuelMass() > 0 and self.fuelTank.getFuelMass() > 0:
            for engine in self.engines:
                engineResult = engine.fire(delta_t)
                
                self.applyImpulseChange(transforms.rotation_xyz(engineResult[0],self.rotation)) #thrust transformed with rocket rotation
                #print(transforms.rotation_xyz(engineResult[0],self.rotation))
                
                self.oxTank.addFuelMass(-engineResult[1])
                self.fuelTank.addFuelMass(-engineResult[2])
                
        #external forces
        self.applyGravity()
        DragImpChange = self.Cd*self.referenceArea*aerodynamics.getAtmosphereDensity(np.linalg.norm(self.position))*(self.velocity**2)*0.5
        for i in range(3):
            DragImpChange[i] = -np.sign(self.velocity[i])*DragImpChange[i]
        self.applyImpulseChange(DragImpChange)

        
        #update location and attidude
        self.position+=self.velocity*delta_t
        self.rotation+=self.rotationalVelocity*delta_t
    
        
    def applyImpulseChange(self,impulseChange):
        self.velocity+=impulseChange/self.mass
        
    def applyAngularMomentumChange(self,momentChange):
        self.rotationalVelocity+=np.linalg.inv(self.intertiaTens)*momentChange
        
    def setRollVel(self,v): #z-axis (along length of rocket)
        pass
    
    def setPitchVel(self,v): #x-axis
        self.rotationalVelocity[0] = v
    
    def setYawVel(self,v): #y-axis
        pass
    
        
    def getTotalMass(self):
        return self.mass
        
    def getTotalFuelMass(self):
        return self.oxTank.getFuelMass()+self.fuelTank.getFuelMass()
        
    def printState(self):
        print("------------------------")
        print("Velocity: "+str(self.velocity))
        print("Alttitude: "+str(self.position[2]))
        print("Oxidzer Mass: " +str(self.oxTank.getFuelMass()))
        print("Fuel Mass: " +str(self.fuelTank.getFuelMass()))
    
    def getPosition(self):
        return self.position
        
    def getAttitude(self):
        return self.rotation
        
    def applyGravity(self):
        #center of earth at (0,0,0)
        gravDir = -self.position/np.linalg.norm(self.position)
        gravityImpChange = gravDir*0.001*9.81*self.getTotalMass()
        self.applyImpulseChange(gravityImpChange)
    
    def getLaunchFlag(self):
        return self.launchFlag
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    