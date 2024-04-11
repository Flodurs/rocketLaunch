import physicsBody
import numpy as np

class engine(physicsBody.physicsBody):
    def __init__(self):
        self.I_sp = 200*9.81 #using SI-Units m/s | divide by g to get conventional unit in s
        
       
        
        self.massFlow = 1000 #kg/s
        self.oxFuelRatio = 1 #Oxidizer Fuel Ratio
        
        
        
      
        
        
        super().__init__()
        self.mass = 0
    
    def getMass(self):
        return self.mass
    
    #returns generated Impulse change and used propellant during delta_t
    def fire(self,delta_t):
        
        oxMassFlow = self.massFlow/(1+1/self.oxFuelRatio)
        fuMassFLow = oxMassFlow/self.oxFuelRatio
        
        # print(oxMassFlow+fuMassFLow)
        
        burntMass_ox = oxMassFlow * delta_t
        burntMass_fu = fuMassFLow * delta_t
        
        generatedImpulseChange = np.array([0,0,self.I_sp * self.massFlow * delta_t]) 
        # print(burntMass_ox)
        # print(burntMass_fu)
        return generatedImpulseChange, burntMass_ox, burntMass_fu
        