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


pkls = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']

if __name__ == "__main__":
	whole_pickle = []
	for p in pkls:
	    n = '../texts' + p + '.pkl'
	    print 'adding pickle ' + n
	    whole_pickle.extend(load_data(n))
	print 'Saving result...'
	save_data('../all_texts.pkl', whole_pickle)

