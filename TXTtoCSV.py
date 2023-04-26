'''
In this file, the task is to take in all the results files and
extract the names and data from verilog output files
'''

# open the .txt for header names
namesfile = open("names.txt", 'w')
namesfile.write('') # empty the file
namesfile.close()
# open the .txt for our verilog output data to go in
datafile = open("DATA.txt", 'w')
datafile.write('') # empty the file
datafile.close()
# open the name and data file in append mode
namesfile = open("names.txt", 'a')
datafile = open("DATA.txt", 'a')

# writting the values in
for i in range(1, 9):
    for j in range(1, 29):
        with open("Results/Output"+str(i)+"[0, "+str(j)+"].txt", "r") as f:
            line = f.read()
            #print(line[:line.find("[", 5)-2].replace(",", ";")) # for names
            namesfile.write(line[:line.find("[", 5)-2].replace(",", ";")+str(", "))
            print(line[line.find("[", 5)+1:-2])
            #datafile.write(line[line.find("[", 5)+1:-2]+str("\n")) # for data
            f.close()

namesfile.close()
datafile.close()
