import numpy as np
import pickle

def read_output(index):
    #Here you can read output files generated from the model runs
    filepath = './OutputFiles/hugoniot_results_'+str(index)+'.pkl'
    filehandler = open(filepath, 'rb') 
    loaded_list = pickle.load(filehandler)
    filehandler.close()
    return loaded_list