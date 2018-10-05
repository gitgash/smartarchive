from gensim import corpora, models, similarities
from pprint import pprint

import pickle as pkl
def save_data(fname, data):
    output = open(fname, 'wb')
    pkl.dump(data, output)
    output.close()  
    
    
def load_data(fname):
    inp = open(fname, 'rb')
    d = pkl.load(inp)
    inp.close()
    return d


print 'Load data'
dct = load_data('../dict_compacted.pkl')
crp = load_data('../corpora1.pkl')
print 'Load finished'

lda = models.ldamodel.LdaModel(crp, id2word=dct, num_topics=100, chunksize=100000, passes=20, iterations=10000)

print "saving lda..."
save_data('../lda3.pkl', lda)
print "Finish"

