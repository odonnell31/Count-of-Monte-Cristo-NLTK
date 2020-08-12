# -*- coding: utf-8 -*-
"""
Created on Tue Aug 06 12:33:36 2019

@author: Michael O'Donnell

Count of Monte Cristo NLP!
"""

# import libraries
import nltk
import requests

url = "https://www.gutenberg.org/files/1184/1184-0.txt"

response = requests.get(url)
raw = response.text
# lowercase the text
raw = raw.lower()


print "type of text", type(raw)
print "length of text:", len(raw)
print "first 100 characters:", raw[:100]
print "=========="

# create a version of the text without puncuation
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
raw_nonpunct = tokenizer.tokenize(raw)

### want to replace contractions before tokenizing
#replacer = RegexpReplacer()
#raw_replaced = nltk.word_tokenize(replacer.replace(raw))

### Now, to tokenize the text
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# filter the text for stopwords
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
word_tokens_clean = [word for word in raw_nonpunct if word not in english_stops]
COMC_text = nltk.Text(word_tokens_clean)
raw_text = nltk.Text(word_tokens)

print word_tokens_clean[150000:150020]
print "=========="


# bigrams
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

bcf = BigramCollocationFinder.from_words(word_tokens_clean)
print bcf.nbest(BigramAssocMeasures.likelihood_ratio, 20)
print "==========="

# now, trigrams!
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

tcf = TrigramCollocationFinder.from_words(word_tokens_clean)
print tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 10)
print "=========="

### Current variables:
# raw = raw text file
# sent_tokens = raw sentances
# word_tokens = raw words
# word_tokens_clean = cleaned words
# bcf = top x bigrams
# tcf = top y trigrams


# to create a dispersion plot
print COMC_text.dispersion_plot(["count", "edmond", "danglars", "wilmore"])
print "=========="

# to count the amoujnt of unique words in the book
print "number of words:", len(set(COMC_text))
print "number of raw words:", len(set(raw_text))

print "count of raw words:", ((len(raw_text))/(len(set(raw_text))))
print "=========="

# to count appearances of a word:
print "number of Edmond references:", COMC_text.count('edmond')
print "number of Wilmore references:", COMC_text.count('wilmore')
print "number of Abbe Faria references:", COMC_text.count('faria')
print "number of Abbe Busoni references:", COMC_text.count('busoni')
print "=========="

# an easy function to figure lexical diversity of any text
# use below to compare COMC with other famous books!
def lexical_diversity(text):
    print len(text)/len(set(text))

# using Frequency Distributions!
fdist_clean = nltk.FreqDist(COMC_text)
print (fdist_clean.keys())[:50]
print fdist_clean.most_common(25)
print "=========="
print fdist_clean.plot(20, cumulative = True)
print "=========="

# find the longest words!
long_words = [w for w in set(COMC_text) if len(w)>15]
print sorted(long_words)
for i in long_words:
    print raw_text.concordance(long_words[i])

# look at collocations
collos = COMC_text.collocations()
print collos

# to find certain text (page 23)
print [w for w in set(COMC_text) if w.startswith('abb')]

# to find if two characters were in the same sentance!
[w for w in sent_tokens if "busoni" in w and "count" in w]

