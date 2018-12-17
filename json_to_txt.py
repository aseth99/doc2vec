import json
import csv
 
txtFileName = "newsDatatest.txt"

tweets = []

jsonFileToBeOpened = "news.json"
for line in open(jsonFileToBeOpened, 'r'):
    tweets.append(json.loads(line))

for line in tweets:
    textData = line.get('text')
    str2 = textData.replace("\n", " ")
    with open(txtFileName, 'a') as the_file:
        the_file.write(str2 + "\n")

with open('newsDatatest.txt') as infile, open('sanitizedOutput.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
