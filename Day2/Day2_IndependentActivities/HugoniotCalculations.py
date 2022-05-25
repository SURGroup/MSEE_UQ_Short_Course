import numpy as np
import pickle 

a0 = <a0> 
a1 = <a1>
a2 = <a2> 
a3 = <a3> 

initial_density = 3.52
particle_velocity = list(np.linspace(3.5, 10, 131))
shock_velocity = [a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 for x in particle_velocity]
density=[initial_density * x[1] / (x[1] - x[0]) for x in zip(particle_velocity, shock_velocity)]
pressure = [initial_density * x * y for (x, y) in zip(shock_velocity, particle_velocity)]
energy=[0.5*p*(1/initial_density-1/d) for (p, d) in zip(pressure, density)]

results= [particle_velocity]
results.append(shock_velocity)
results.append(density)
results.append(pressure)
results.append(energy)


filehandler = open("hugoniot_results.pkl", 'wb') 
pickle.dump(results, filehandler)
filehandler.close()
