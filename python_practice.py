print("Hello World!")

counties = ["Araphoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

temp = int(input("What is the temp outside"))

if temp >80:
    print("turn on the AC")
else:
    print("open the window")

score=int(input("what's your score?"))

if score>=90:
    print("grade A")
elif score >=80:
    print("grade B")
elif score >=70:
    print("grade C")
else:
    print("fail")

for i in range(len(counties)):
    print(counties[i])

for county in counties:
    print(county[0])

x= [1,2,3,4,5]

for i in x:
    print(x[2])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for i in counties_dict:
    print(i)
    
for i in counties_dict:
    print(counties_dict[i])
    

for i,j in counties_dict.items():
    print(i + " county has " +str(j)+ " registered voters")
    

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# here we convereted i into an int by using range and len(), so then
#we can print the list based on the index, as when we use range and len we convert i into int

for i in range(len(voting_data)):
    print(voting_data[i])

#here i remains a dictnory, because voting_data is a list of dictionaries, so in print 
# statement we can use dictionary functions with i. such as .get, .value, .keys..


for i in voting_data:
    print(i.get("registered_voters"))

for i,j in counties_dict.items():
    print(f"{i} county has {j:,} registered voters.")


for i in voting_data:
    print (f"{i['county']} county has {i.get('registered_voters'):,} registered voters.")


#dir() - takes in module,dictionary, string


f=5+9*3/2-4
print(f)


for j in candidate_voters:
        votes = float(candidate_voters[j])/float(total_votes)*100
        #vote_percent = float(votes)/float(total_votes)*100
        print(f"{j} received {votes:.1f} votes")
        

        
            #or


for i,j in candidate_voters.items():
        votes = float(j)/float(total_votes)*100
        print(f"{i} received {votes:.1f} votes")
        
            
#reference the output path with a variable, where the file will be saved
#create a folder "analysis"
file_to_save= os.path.join("analysis","election_analysis.txt")

with open (file_to_save,"w") as riting:
    riting.write("Counties in the Election\n-----------------------\nArapahoe\n")
    riting.write("Denver\nJefferson")



#461621
#422239
#461002
#460737
#460739

#461000
#460835
#460731
#459695
#458446