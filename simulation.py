import rocketStage
import numpy as np
import matplotlib.pyplot as plt

class simulation:
    
    def __init__(self):
        self.rocket = rocketStage.rocketStage()
        self.running = 1
        self.rocket.launch()
        
        
        
        self.zPos = []
        self.yPos = []
        self.xPos = []
        
        self.rotX = []
        self.rotY = []
        self.rotZ = []
        
        
        self.fuelMass = []
        self.time = 0
        self.timeData = []
        
        
    def update(self):
        self.time+=0.001
        self.rocket.update(0.001)
        
        
        
        if self.time > 15 and self.time < 23:
            self.rocket.setPitchVel(0.2)
        else:
            self.rocket.setPitchVel(0)
        
        
        self.zPos.append(self.rocket.getPosition()[2])
        self.xPos.append(self.rocket.getPosition()[0])
        self.yPos.append(self.rocket.getPosition()[1])
        
        self.rotX.append(self.rocket.getAttitude()[0])
        self.rotY.append(self.rocket.getAttitude()[1])
        self.rotZ.append(self.rocket.getAttitude()[2])
        
        self.fuelMass.append(self.rocket.getTotalFuelMass())
        self.timeData.append(self.time)
        
        
        if np.linalg.norm(self.rocket.getPosition()) < 6371000 or self.time > 10000:
            self.running = 0
        
        
    def run(self):
        step = 0
        while self.running:
            self.update()
            # self.rocket.printState()
            step+=1
            if step%10000 == 0:
                #print(self.time)
                pass
        
        fig, axs = plt.subplots(4,2)
        axs[0,0].plot(self.timeData, self.xPos)
        axs[0,0].set_title("X-Position") 
        axs[1,0].plot(self.timeData, self.yPos)
        axs[1,0].set_title("Y-Position") 
        axs[2,0].plot(self.timeData, self.zPos)
        axs[2,0].set_title("Z-Position") 
        
        axs[0,1].plot(self.timeData, self.rotX)
        axs[0,1].set_title("X-Rotation") 
        axs[1,1].plot(self.timeData, self.rotY)
        axs[1,1].set_title("Y-Rotation") 
        axs[2,1].plot(self.timeData, self.rotZ)
        axs[2,1].set_title("Z-Rotation") 
        
        axs[3,0].plot(self.timeData, self.fuelMass)
        axs[3,0].set_title("Fuel Mass") 
       
        axs[3,1].set_title("Y-X Trajectory") 
        
        
        fig2, axs2 = plt.subplots(1)
        axs2.set_ylim(-10000000,10000000)
        axs2.set_xlim(-10000000,10000000)
        axs2.set_aspect('equal')
        axs2.plot(self.yPos, self.zPos)
        
        #draw earth
        earthX = 6371000*np.cos(np.linspace(0,2*np.pi,1000))
        earthY = 6371000*np.sin(np.linspace(0,2*np.pi,1000))
        
        
        
        axs2.plot(earthX,earthY)
        
        fig.tight_layout()
        plt.show()
            
sim = simulation()
sim.run()