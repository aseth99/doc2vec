from os import listdir
from os.path import isfile, join

docLabels = []
docLabels = [f for f in listdir("/Users/aman/Desktop/Hammer/doc2vec/neg") if f.endswith('.txt')] 

txtFileName = open("testData.txt", 'w')
for fname in docLabels:
	with open("/Users/aman/Desktop/Hammer/doc2vec/neg/" + fname) as infile:
		txtFileName.write(infile.read())
		txtFileName.write('\n')

		infile.close()

txtFileName.close()