# This programe reads data from a CSV file and prints each line.
# Author: Hewa Orang

import csv

FILENAME = 'data.csv'
DATADIR = "PFDA/PFDA-assignments/my-work/topic-02/"

with open( FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total += int(line[1]) # line one as 0 is the header
        linecount += 1
    print(f"average is {total/(linecount-1)}") # 
