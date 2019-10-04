###########################################################################################################################################################
# Python Script to find the test files (by looking for string set of test/Test/TEST/) from a given path and storing the test file paths in a text file,
# and also storing the paths of remaining files in a different text file.
# Authored by: Navneet Kaushal
# Graduate Student, Master of Engineering, Carleton University, Canada
# December, 2018
###########################################################################################################################################################

import os

directory_name = input("Please enter the path: ")
os.chdir(directory_name)
if os.path.exists("appFile.txt"):
    os.remove("appFile.txt")
if os.path.exists("tfile.txt"):
    os.remove("tfile.txt")
if os.path.exists("afile.txt"):
    os.remove("afile.txt")
c = 0
test_filelist = []
app_filelist = []
status = ""

for root, dirs, files in os.walk(directory_name):
    for name in files:
        app_filelist.append(os.path.join(root, name))
        c += 1
app_filelist = list(set(app_filelist))
print("Total number of files: " + str(len(app_filelist)))
status = "Processing..."

af = open("allFiles.txt","w+")
for f in app_filelist:  
    af.write(f)
    af.write("\r\n")
af.close()
print(status)

open('tfile.txt','w').writelines(line for line in open('appFile.txt') if (('test' in line) or ('Test' in line) or ('TEST' in line)))
#open('tfile.txt','w').writelines(line for line in open('appFile.txt') if (('test' in line) or ('Test' in line) or ('TEST' in line) or ('.t.cpp' in line)))

open('afile.txt','w').writelines(line for line in open('appFile.txt') if (('test' not in line) and ('Test' not in line) and ('TEST' not in line) and (line.strip())))
#open('afile.txt','w').writelines(line for line in open('appFile.txt') if (('test' not in line) and ('Test' not in line) and ('TEST' not in line) and ('.t.cpp' not in line) and (line.strip())))

status = "Filtering of files successfully completed."
print(status)

