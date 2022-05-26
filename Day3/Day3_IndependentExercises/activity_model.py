import numpy as np


def model_quadratic(theta):
    domain = np.linspace(0, 10, 50)
    inpt = np.array(theta).reshape((-1,))
    return inpt[0] + inpt[1] * domain + inpt[2] * domain ** 2 + inpt[3] * domain ** 3
