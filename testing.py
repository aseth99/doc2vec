from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"


model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
test_data = word_tokenize("disaster is bad".lower())
v1 = model.infer_vector(test_data)
# print("V1_infer", v1)

# to find most similar doc using tags
similar_doc = model.most_similar([v1])
# print(similar_doc)

print('%s:\n %s' % (model, model.most_similar([v1], topn=9)))

# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs['1'])