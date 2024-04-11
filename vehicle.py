import rocketStage
import numpy as np




class vehicle:
    def __init__(self):
        self.stages = [rocketStage.rocketStage() for i in range(2)]
        
        
    def update(self):
        for stage in self.stages:
            stage.update()
            
    def launchNextStage(self):
        pass
        