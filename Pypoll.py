 #1 Data we need to retrieve
 #2 The total number of votes cast
 #3 A complete list of candidates who recieved votes 
 #4 The percentage of votes each candidate won
 #5 The total number of votes each candidate won
 #6 The winner of the elections based on the popular vote
 #7 The voter turnout for each county.
 #8 The percentage of votes each county contributed to the election.
 #9 The county with the largest turnout.

#import the dependencies
#import csv module
import csv
#import os module followed by method path and join
import os
#refrence the path with a variable,to load the file
file_to_load = os.path.join("Resources", "election_results.csv")
#reference the path to save the file
file_to_save = os.path.join("analysis","election_analysis.txt")

#initial a total vote counter
total_votes = 0 
s
candidate_option=[]
candidate_voters={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load,'r') as election_data:
    #to do: read and analyse the data
    file_reader= csv.reader(election_data)

    header=next(file_reader)
    print(header)

    for row in file_reader:
        total_votes += 1
        
        candidate_name= row[2]
        

        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_voters[candidate_name]= 0
        candidate_voters[candidate_name] += 1

#save results to text file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    

    for candidate_name in candidate_voters:
        votes = candidate_voters[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        Candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(Candidate_results)
        txt_file.write(Candidate_results)
        
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
            






