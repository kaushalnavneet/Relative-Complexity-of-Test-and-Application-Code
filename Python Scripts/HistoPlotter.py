###########################################################################################################################################################
# Python Script to plot the histogram and descriptive table for a given column of a csv file. It automatically saves the plots too.
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

        func_data = data[~data['Cyclomatic'].isnull()]
        func_data = func_data[func_data['Cyclomatic'] != 0] 

        fname = filename + '_cc_histo' +'.png'
        fig, ax = plt.subplots()
        func_data.hist('Cyclomatic', ax=ax, bins = 20)
        plt.title("Cyclomatic Complexity - Histogram")
        plt.xlabel("Cyclomatic Complexity")
        plt.ylabel("No. of Functions")
        ind = (np.arange(min(func_data.Cyclomatic), max(func_data.Cyclomatic)+1, 5))
        plt.xticks(ind, rotation=90)
        fig.savefig(fname)
        print(fname)

        fname = filename + '_cc_desc' +'.png'
        desc = func_data['Cyclomatic'].describe()
        plot = plt.subplot(111, frame_on=False)
        plot.xaxis.set_visible(False) 
        plot.yaxis.set_visible(False) 
        table(plot, desc,loc='upper right')
        plt.savefig(fname)
        print(fname)

        fname = filename + '_loc_histo' +'.png'
        fig, ax = plt.subplots()
        func_data.hist('CountLineCode', ax=ax, bins = 20)
        plt.title("Cyclomatic Complexity - Histogram")
        plt.xlabel("Cyclomatic Complexity")
        plt.ylabel("No. of Functions")
        ind = (np.arange(min(func_data.Cyclomatic), max(func_data.Cyclomatic)+1, 5))
        plt.xticks(ind, rotation=90)
        fig.savefig(fname)
        print(fname)

        fname = filename + '_loc_desc' +'.png'
        desc = func_data['CountLineCode'].describe()
        plot = plt.subplot(111, frame_on=False)
        plot.xaxis.set_visible(False) 
        plot.yaxis.set_visible(False) 
        table(plot, desc,loc='upper right')
        plt.savefig(fname)
        print(fname)


