 #1 Data we need to retrieve
 #2 The total number of votes cast
 #3 A complete list of candidates who recieved votes 
 #4 The percentage of votes each candidate won
 #5 The total number of votes each candidate won
 #6 The winner of the elections based on the popular vote

file_to_load = 'Resources/election_results.csv'

#with open(file_to_load) as election_data:
    #print(election_data)
#import the dependencies
#import csv module
import csv
#import os module followed by method path and join
import os
#refrence the path with a variable,to load the file
file_to_load = os.path.join("Resources", "election_results.csv")
#reference the path to save the file
file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_load,'r') as election_data:
    #to do: read and analyse the data
    file_reader= csv.reader(election_data)

    header=next(file_reader)
    print(header)


#reference the output path with a variable, where the file will be saved
#create a folder "analysis"
file_to_save= os.path.join("analysis","election_analysis.txt")

with open (file_to_save,"w") as riting:
    riting.write("Counties in the Election\n-----------------------\nArapahoe\n")
    riting.write("Denver\nJefferson")




