import numpy as np


def evaluate_model(samples):
    a0 = samples[0, 0]
    a1 = samples[0, 1]
    a2 = samples[0, 2]
    a3 = samples[0, 3]

    particle_velocity = np.linspace(3.5, 10, num=50)
    shock_velocity = [a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3 for x in particle_velocity]

    return shock_velocity
