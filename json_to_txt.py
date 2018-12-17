import json
import csv
 


# chooseName = input("\nWhat should we name the txt file?\n\n\n")
txtFileName = "newsDatatest.txt"



# csv_out = open(csvFileName, mode='w') #opens csv file
# writer = csv.writer(csv_out) #create the csv writer object

# fields = ['Twitter Handle & User Name', 'Tweet', ' external URL', 'Hashtags', 'Date of Tweet', 'Followers', 'Following', 'RT', 'FAV'] #field names
# writer.writerow(fields) #writes field

tweets = []

# exitClause = "notdone"
# print("whose tweets finna be txt files?\n\n\n")

# while exitClause != "done":
#     exitClause = input("(type done if finished)\n\n@")
#     if exitClause == "done":
#     	break
jsonFileToBeOpened = "news.json"
for line in open(jsonFileToBeOpened, 'r'):
    tweets.append(json.loads(line))

# if exitClause == "done":
#     print("converting...")

for line in tweets:
    textData = line.get('text')
    #print(textData)
    with open(txtFileName, 'a') as the_file:
        the_file.write(textData)


