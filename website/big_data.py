import pickle
import bcolz
import numpy as np
import nltk
from nltk.corpus import words, stopwords
from nltk.stem import WordNetLemmatizer
from wordfreq import top_n_list

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

common_words = top_n_list('en',10000)

english_words = [lemmatizer.lemmatize(word.lower(), pos='v') for word in common_words if word.lower() not in stopwords]

words = []
idx = 0
word2idx = {}
glove_path = '/Users/phantsure/Documents/Coding/Projects/contexto/MyGame/glove.6B'
vectors = bcolz.carray(np.zeros(1), rootdir=f'{glove_path}/6B.300.dat', mode='w')

with open(f'{glove_path}/glove.6B.300d.txt', 'rb') as f:
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
    
vectors = bcolz.carray(vectors[1:].reshape((len(words), 300)), rootdir=f'{glove_path}/6B.300.dat', mode='w')
vectors.flush()

pickle.dump(words, open(f'{glove_path}/6B.300_words.pkl', 'wb'))
pickle.dump(word2idx, open(f'{glove_path}/6B.300_idx.pkl', 'wb'))
