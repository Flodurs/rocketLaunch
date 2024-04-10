import rocketStage
import numpy as np
import matplotlib.pyplot as plt

class simulation:
    
    def __init__(self):
        self.rocket = rocketStage.rocketStage()
        self.running = 1
        self.rocket.launch()
        
        
        
        self.zPos = []
        self.fuelMass = []
        self.time = 0
        self.timeData = []
        
        
    def update(self):
        self.time+=0.001
        self.rocket.update(0.001)
        
        
        
        
        
        self.zPos.append(self.rocket.getPosition()[2])
        self.fuelMass.append(self.rocket.getTotalFuelMass())
        self.timeData.append(self.time)
        
        
        if self.rocket.getPosition()[2] < -1:
            self.running = 0
        
        
    def run(self):
        while self.running:
            self.update()
            self.rocket.printState()
            
        fig, axs = plt.subplots(2)
        
        axs[0].plot(self.timeData, self.zPos)
        axs[1].plot(self.timeData, self.fuelMass)
        
        plt.show()
            
sim = simulation()
sim.run()