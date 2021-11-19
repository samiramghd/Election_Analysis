# add your dependencies
import csv
import os


# Assigne a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
    
# create a file name variable to a direct or indirect pathon the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize total votes
total_votes = 0

candidate_options = []
# declare the empty candidate dictionary
candidate_votes = {}
# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open the election results and read the data
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # print the header row
    headers = next(file_reader)
    # print(headers)
    
    # print each row in csv file
    for row in file_reader:
        #print(row)
        #add to the total vote count
        total_votes += 1
        # print the candidate name from each row
        candidate_name = row[2]
        # If the candidate name does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # add candidate name to the candidate list
            candidate_options.append(candidate_name)
            # begin tracking that candidate vote
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # retrive vote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # print candidate name and percentages of votes
        #print(f"{candidate_name}: recieved {vote_percentage}% of the vote")
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count and candidate
        # determine if the vote is grater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
                    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
                    
            
                
            
    # print the total votes
    # print(total_votes)
    #print(candidate_votes)      
    
    
        
    
