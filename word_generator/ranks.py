import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
import random
import pickle
import bcolz

glove_path = './glove.6B'
vectors = bcolz.open(f'{glove_path}/6B.300.dat')[:]
words = pickle.load(open(f'{glove_path}/6B.300_words.pkl', 'rb'))
word2idx = pickle.load(open(f'{glove_path}/6B.300_idx.pkl', 'rb'))

glove = {w: vectors[word2idx[w]] for w in words}

embeddings = np.array([glove[word] for word in words])
word2id = word2idx

# Function to calculate the cosine similarity between two word vectors
def get_word_similarity(embeddings, word2id, word1, word2):
    word1_vector = embeddings[word2id[word1]]  # Get the vector representation of word1
    word2_vector = embeddings[word2id[word2]]  # Get the vector representation of word2
    # Compute the cosine similarity between the two vectors
    similarity = cosine_similarity(word1_vector.reshape(1, -1), word2_vector.reshape(1, -1))

    return similarity[0][0]

vocab = set(word2id.keys())
rand_word = random.choice(tuple(vocab))
print(rand_word)

similarity = [(get_word_similarity(embeddings, word2id, rand_word, w), w) for w in vocab]

rank_dict = {word[1]:rank for rank, word in enumerate(sorted(similarity, reverse=True))}

with open('result.json', 'w') as fp:
    json.dump(rank_dict, fp)
