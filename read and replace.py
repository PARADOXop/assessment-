import os
def replace(file_name):
    print('Original file content')
    
    fin = open(file_name, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace(x, y)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_name, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    
    print("Text successfully replaced")

x = 'placement'
y = 'screening'     
replace('example.txt')