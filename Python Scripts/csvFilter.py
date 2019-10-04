###########################################################################################################################################################
# Python Script to find the .csv files in a given directory and saving the paths of these files into a text file. 
# Authored by: Navneet Kaushal
# Graduate Student, Master of Engineering, Carleton University, Canada
# December, 2018
###########################################################################################################################################################


#Finding All Files
import os
import fnmatch
import sys
from shutil import copy

directory_name = input("Please enter the path: ")
os.chdir(directory_name)
if os.path.exists("allfile.txt"):
    os.remove("allfile.txt")
if os.path.exists("csvFile.txt"):
    os.remove("csvFile.txt")
c = 0
csv_filelist = []
status = ""

for root, dirs, files in os.walk(directory_name):
    for name in files:
        csv_filelist.append(os.path.join(root, name))
        c += 1
csv_filelist = list(set(csv_filelist))
print("Total number of files: " + str(len(csv_filelist)))
status = "Processing..."

af = open("allfile.txt","w+")
for f in csv_filelist:  
    af.write(f)
    af.write("\r\n")
af.close()
print(status)

open('csvFile.txt','w').writelines(line for line in open('allfile.txt') if (('.csv' in line)))

status = "Path of csv files successfully copied."
print(status)

