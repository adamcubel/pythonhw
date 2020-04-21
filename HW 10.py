import statistics

filename = str(input('Please enter the file name: ')) #asks user to input file's name to store a s a variable
file_data = open(filename, a) #opens declared file in edit mode, new data will be appended to file, sets reference variable
file_data = [] #set data in file into an array
file_data.append(print((statistics.mean(file_data))) #will write the average of data at the end of the file, file_data.write() as another possible route?