import nltk
from nltk.stem.porter import PorterStemmer
# import nltk_utils
import numpy as np

stemmer = PorterStemmer()

def tokenize(kalimat):
    return nltk.word_tokenize(kalimat)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_kalimat, all_words):
    tokenized_kalimat =[stem(w) for w in tokenized_kalimat]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_kalimat:
            bag[idx]=1.0
    return bag

# kalimat = ["hello", "how","are","you"]
# words = ['hi','hello','I','you','bye','thank','cool']
# bog = bag_of_words(kalimat,words)
# print(bog)

# a = ["Organized", "organize","organizing"]
# stemmed_words = [stem(w) for w in a]
# print(stemmed_words)
