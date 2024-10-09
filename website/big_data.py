import pickle
import bcolz
import numpy as np
import nltk
from nltk.corpus import words


nltk.download('words')
english_words = set(words.words())

words = []
idx = 0
word2idx = {}
glove_path = '/Users/phantsure/Documents/Coding/Projects/contexto/MyGame/glove.6B'
vectors = bcolz.carray(np.zeros(1), rootdir=f'{glove_path}/6B.50.dat', mode='w')

with open(f'{glove_path}/glove.6B.50d.txt', 'rb') as f:
    for l in f:
        line = l.decode().split()
        word = line[0]
        

        if word not in english_words:
            continue
        
        words.append(word)
        word2idx[word] = idx
        idx += 1
        vect = np.array(line[1:]).astype(np.float64)
        vectors.append(vect)
    
vectors = bcolz.carray(vectors[1:].reshape((len(words), 50)), rootdir=f'{glove_path}/6B.50.dat', mode='w')
vectors.flush()


pickle.dump(words, open(f'{glove_path}/6B.50_words.pkl', 'wb'))
pickle.dump(word2idx, open(f'{glove_path}/6B.50_idx.pkl', 'wb'))
