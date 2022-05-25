import fire
import os
from os.path import dirname
import os.path
from os import path

def run_model(index):
    # Model is run here using CLI 
    # Runs are performed in run/{index} folder
    name_='HugoniotCalculations_'+str(index)+'.py'

    current_dir = os.getcwd()

    initial_path = current_dir+'/InputFiles/'+name_
    final_path = current_dir+'/'+name_

    copy_input_command='cp -r "' +initial_path+'" "'+final_path+'"'
    os.system(copy_input_command) 

    run_model_command='python3 '+name_
    os.system(run_model_command)

    output_path=os.path.join(os.path.sep, current_dir, 'OutputFiles')
    os.makedirs(output_path,exist_ok=True)

    copy_output_command='cp ./hugoniot_results.pkl ./OutputFiles/hugoniot_results_'+str(index)+'.pkl'
    os.system(copy_output_command)

if __name__=='__main__':
    fire.Fire(run_model)


