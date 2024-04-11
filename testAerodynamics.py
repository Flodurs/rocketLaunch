import aerodynamics
import matplotlib.pyplot as plt

densitys = []
for i in range(100000):
    densitys.append(aerodynamics.getAtmosphereDensity(i))
    
plt.plot(densitys)
plt.show()
    