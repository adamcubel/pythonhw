import statistics
import os

filename = str(input('Please enter the file name: ')) #asks user to input file's name to store a s a variable
filename = os.path.abspath(filename)

if filename:
    totalLines = 0
    lines = {}
    total = 0

    print(filename)
    file = open(filename)
    lines = file.readlines()

    for line in lines:
        print(line)
        print(totalLines)
        if line.rstrip().isnumeric():
            totalLines += 1
            total += float(line.rstrip())

print('avg from file: ' + str(total / totalLines))