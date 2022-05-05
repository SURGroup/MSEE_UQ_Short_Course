import numpy as np


def read_sum_scalar(index):
    x = np.loadtxt("./OutputFiles/oupt_%d.out" % index)
    return x

