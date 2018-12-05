from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models.deprecated.doc2vec import LabeledSentence
import gensim

class DocIterator(object):
	def __init__(self, doc_list, labels_list):
		self.labels_list = labels_list
		self.doc_list = doc_list
	def __iter__(self):
		for idx, doc in enumerate(self.doc_list):
			yield LabeledSentence(words=doc.split(),labels=[self.labels_list[idx]])