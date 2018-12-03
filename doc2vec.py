#Import all the dependencies
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
# import DocIterator as DocIt
# import nltk

# nltk.download()

with open('testData.txt', 'r') as f:
    data = f.readlines()


tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]
# from os import listdir
# from os.path import isfile, join


# docLabels = []
# docLabels = [f for f in listdir("/Users/aman/Desktop/Hammer/doc2vec/neg") if f.endswith('.txt')]

# data = []
# for doc in docLabels:
# 	txtFile = open("/Users/aman/Desktop/Hammer/doc2vec/neg/" + doc)
# 	data.append(txtFile)
# 	txtFile.close()


# it = DocIt.DocIterator(data, docLabels)

# model = gensim.models.Doc2Vec(size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025) # use fixed learning rate
# model.build_vocab(it)
# for epoch in range(10):
# 	model.train(it)
# 	model.alpha -= 0.002 # decrease the learning rate
# 	model.min_alpha = model.alpha # fix the learning rate, no deca
# 	model.train(it)


max_epochs = 100
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=vec_size,
                alpha=alpha, 
                min_alpha=0.00025,
                min_count=1,
                dm =1)
  
model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")
