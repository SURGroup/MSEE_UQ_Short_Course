import fire
import os


def matlab(index):
    command1 = "cp ./InputFiles/sum_scalar_" + str(index) + ".m ."
    command2 = "/Applications/MATLAB_R2019a.app/bin/matlab " \
               "-nosplash -nojvm -nodisplay -nodesktop -r 'run sum_scalar_" + str(index) + ".m; exit'"
    command3 = "mv ./OutputFiles/oupt.out ./OutputFiles/oupt_" + str(index) + ".out"
    command4 = "rm sum_scalar_" + str(index) + ".m"
    os.system(command1)
    os.system(command2)
    os.system(command3)
    os.system(command4)


if __name__ == '__main__':
    fire.Fire(matlab)
