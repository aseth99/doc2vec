from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import os
import math
import gensim
import collections
import smart_open
import random

os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"


model= Doc2Vec.load("RAREd2v.model")

# Set file names for train and test data
test_data_dir = '{}'.format(os.sep).join([gensim.__path__[0], 'test', 'test_data'])
lee_train_file = test_data_dir + os.sep + 'lee_background.cor'
lee_test_file = test_data_dir + os.sep + 'lee.cor'

def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            print("reading ....")
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])

print("bout to process txt data...")
test_corpus = list(read_corpus("sanitizedOutput.txt"))


ranks = []
second_ranks = []
for doc_id in range(math.floor(len(test_corpus)/100)):
    print(doc_id)
    inferred_vector = model.infer_vector(test_corpus[doc_id].words)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)
    
    second_ranks.append(sims[1])

print("COLLECTIONS.COUNTER(RANKS)")
print(collections.Counter(ranks))

#print(test_corpus)
# Pick a random document from the test corpus and infer a vector from the model
# doc_id = random.randint(0, len(test_corpus) - 1)
doc_id = random.randint(0, len(test_corpus) - 1)

inferred_vector = model.infer_vector(test_corpus[doc_id].words)
sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))

# Compare and print the most/median/least similar documents from the train corpus
print('Test Document ')
print(doc_id)
print(' '.join(test_corpus[doc_id].words))

print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
	# print(label)
	# print(index)
	newIndex = int(sims[index][0])
	# print(train_corpus[newIndex])
	# print(' '.join(train_corpus[newIndex].words))
	print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(test_corpus[newIndex].words)))
	print("DONee")



# #to find the vector of a document which is not in training data
# test_data = word_tokenize("disaster is bad".lower())
# v1 = model.infer_vector(test_data)
# # print("V1_infer", v1)

# # to find most similar doc using tags
# similar_doc = model.docvecs.most_similar([v1])
# print(similar_doc)

# print('%s:\n %s' % (model, model.docvecs.most_similar([v1], topn=9)))

# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs['1'])