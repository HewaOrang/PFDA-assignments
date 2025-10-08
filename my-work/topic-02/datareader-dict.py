# This programe reads data from a CSV file and prints each line.
# Author: Hewa Orang

import csv

FILENAME = 'data.csv'
DATADIR = "PFDA/PFDA-assignments/my-work/topic-02/"

with open( FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age'] 
        # print (line)
        count += 1
    print(f"average is {total/(count)}") # DictReader automatically skips the header row
