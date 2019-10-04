###########################################################################################################################################################
# Python Script to plot the LOC and CC graphs at function level for a given text file where paths of metrics files are stored. It automatically saves the plots too.
# Authored by: Navneet Kaushal
# Graduate Student, Master of Engineering, Carleton University, Canada
# December, 2018
###########################################################################################################################################################

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
import numpy as np
from pandas.plotting import table
import os

directory_name = input("Please enter the path: ")
os.chdir(directory_name)
file_list = input("Please enter the csv file: ")

with open(file_list) as f:
    for srcfile_path_t in f:
        srcfile_path_t = srcfile_path_t.strip()
        srcfile_t = os.path.split(srcfile_path_t)[1]

        data = pd.read_csv(srcfile_path_t)
        filename = srcfile_t[:-4]

        if(file_list == 'csvFile_C.txt'):
            func_data = data[(data.Kind == 'Function')]
        elif(file_list == 'csvFile_J.txt'):
            func_data = data[(data.Kind == 'Method')]
        elif(file_list == 'csvFile_CJ.txt'):
            func_data = data[(data.Kind == 'Function')]
            func_data2 = data[(data.Kind == 'Method')]
            func_data.append(func_data2)
            
                
        fname = filename + '_cc' +'.png'        
        plt.plot(func_data.Name, func_data.Cyclomatic)
        plt.title("Cyclomatic Complexity Plot")
        plt.xlabel("Functions")
        plt.ylabel("Cyclomatic Complexity (CC)")
        plt.xticks(rotation='vertical')
        plt.tick_params(axis='x', which='major', labelbottom=False, bottom=False)
        plt.savefig(fname)
        print(fname)

        fname = filename + '_loc_func' +'.png'
        plt.plot(func_data.Name, func_data.CountLineCode)
        plt.title("LOC Plot")
        plt.xlabel("Functions")
        plt.ylabel("Line of Code (LOC)")
        plt.xticks(rotation='vertical')
        plt.tick_params(axis='x', which='major', labelbottom=False, bottom=False)
        plt.savefig(fname)
        print(fname)

        file_data = data[(data.Kind == 'File')]
        
        fname = filename + '_sc' +'.png'
        plt.plot(file_data.Name, file_data.SumCyclomatic)
        plt.title("SumCyclomatic Complexity Plot")
        plt.xlabel("Files")
        plt.ylabel("SumCyclomatic Complexity")
        plt.xticks(rotation='vertical')
        plt.tick_params(axis='x', which='major', labelbottom=False, bottom=False)
        plt.savefig(fname)
        print(fname)

        fname = filename + '_loc_file' +'.png'
        plt.plot(file_data.Name, file_data.CountLineCode)
        plt.title("LOC Plot")
        plt.xlabel("Files")
        plt.ylabel("LOC")
        plt.xticks(rotation='vertical')
        plt.tick_params(axis='x', which='major', labelbottom=False, bottom=False)
        plt.savefig(fname)
        print(fname)

