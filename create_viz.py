from gensim import corpora, models, similarities
from pprint import pprint
import pyLDAvis.gensim

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
lda = load_data('../lda3.pkl')
# Print the Keyword in the 10 topics
for t in lda.print_topics():
    print t[1]

vis = pyLDAvis.gensim.prepare(lda, crp, dct)
save_data('../vis1.pkl', vis)
