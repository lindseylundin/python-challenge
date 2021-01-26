# import libraries
import csv, os
# read csv
csv_path = os.path.join("Resources", "election_data.csv")
# open file to read, read in rows, break all rows up by columns using comma
with open(csv_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)
    
#initialize list    
    vote_list = []
    candidate_column = []
    
    
    for row in election_data:
        vote_list.append(row[0]) 
        candidate_column.append(row[2])

#total number of votes - each row is one vote
    vote_count = len(vote_list)
    candidate_list = set(candidate_column)
    
    #print(candidate_list)
    complete_cand_list = list(candidate_column)
    
    #print(complete_candidate_list)
    count_cand_Li = complete_cand_list.count('Li')
    count_cand_Khan = complete_cand_list.count('Khan')
    count_cand_Correy = complete_cand_list.count('Correy')
    count_cand_OTooley = complete_cand_list.count("O'Tooley")
 
    Cand_dict = {'Li': count_cand_Li,
                     'Khan': count_cand_Khan,
                     'Correy': count_cand_Correy,
                     "O'Tooley": count_cand_OTooley}
    
    
    
    percent_cand_Li = round((count_cand_Li/vote_count*100),2)
    percent_cand_Khan = round((count_cand_Khan/vote_count*100),2)
    percent_cand_Correy = round((count_cand_Correy/vote_count*100),2)
    percent_cand_OTooley = round((count_cand_OTooley/vote_count*100),2)
    
    #print(F'Li: {percent_cand_Li}% ({count_cand_Li} votes)\n' 
    #      f'Khan: {percent_cand_Khan}% ({count_cand_Khan} votes)\n'
    #      f'Correy: {percent_cand_Correy}% ({count_cand_Correy} votes)\n'
    #      f"O'Tooley: {percent_cand_OTooley}% ({count_cand_OTooley} votes)\n")
    
    
    Winner = max(Cand_dict, key=Cand_dict.get)
    #print(F'Winner: {Winner}')
    
    print('Election Results')
    print('------------------')
    print(f'Total Votes: {vote_count}')
    print(f'Khan: {percent_cand_Khan}% ({count_cand_Khan} votes)')
    print(f'Correy: {percent_cand_Correy}% ({count_cand_Correy} votes)')
    print(f'Li: {percent_cand_Li}% ({count_cand_Li} votes)')
    print(f"O'Tooley: {percent_cand_OTooley}% ({count_cand_OTooley} votes)")
    print(f'Winner: {Winner}')

    #tell computer where to create the new file
txtpath_out = os.path.join('analysis', 'election_results.txt')
#what type the new file should be
with open(txtpath_out, 'w', newline='') as txtfile:
#we need to tell it  how to write on the file
    txtfile.write(f'Election Results\n'
                  f'-----------------\n'
                  f'Total Votes: {vote_count}\n' 
                  f'Khan: {percent_cand_Khan}% ({count_cand_Khan} votes)\n' 
                  f'Correy: {percent_cand_Correy}% ({count_cand_Correy} votes)\n' 
                  f'Li: {percent_cand_Li}% ({count_cand_Li} votes)\n'
                  f"O'Tooley: {percent_cand_OTooley}% ({count_cand_OTooley} votes)\n"
                  f'Winner: {Winner}')