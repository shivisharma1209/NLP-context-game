import pickle
import bcolz
import numpy as np
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from wordfreq import top_n_list

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')  # For POS tagging

# Initialize tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to map POS tag to WordNet POS (verb, noun, adjective, etc.)
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun if uncertain

# Get the top 5,000 common words using wordfreq
common_words = top_n_list('en', 5000)

# POS tagging the words to determine noun, verb, adjective, etc.
tagged_words = nltk.pos_tag(common_words)

# Filter out stop words and apply lemmatization based on POS tagging
english_words = [
    lemmatizer.lemmatize(word.lower(), get_wordnet_pos(pos_tag)) 
    for word, pos_tag in tagged_words if word.lower() not in stop_words
]

words = []
idx = 0
word2idx = {}
glove_path = './glove.6B'
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
