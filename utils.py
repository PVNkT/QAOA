from contextlib import contextmanager
import os 
import matplotlib.pyplot as plt

@contextmanager
def savefig(path_str, filename):
    dir_name = os.path.dirname(path_str)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    yield plt.savefig(path_str+filename) 













