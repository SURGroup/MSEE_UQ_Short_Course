import fire
import os
from os.path import dirname
import os.path
from os import path

def run_model(index):
    # Model is run here using CLI 
    # Runs are performed in run/{index} folder
    name_='elastic_contact_sphere_'+str(index)+'.py'

    current_dir = os.getcwd()

    initial_path = current_dir+'/InputFiles/'+name_
    print(initial_path)
    final_path = current_dir+'/'+name_
    print(final_path)

    copy_input_command='cp -r "' +initial_path+'" "'+final_path+'"'
    print(copy_input_command)
    os.system(copy_input_command) 

    run_model_command='python3 simple.py '+name_
    print(run_model_command)
    os.system(run_model_command)

    output_path=os.path.join(os.path.sep, current_dir, 'OutputFiles')
    os.makedirs(output_path,exist_ok=True)

    copy_output_command='cp ./cube_medium_hexa.vtk ./OutputFiles/cube_medium_hexa_'+str(index)+'.vtk'
    os.system(copy_output_command)

if __name__=='__main__':
    fire.Fire(run_model)


