# This programe reads data from a CSV file and prints each line.
# Author: Hewa Orang

import csv

FILENAME = 'data.csv'
DATADIR = "my-work/topic-02/data"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)
