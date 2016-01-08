
# coding: utf-8

# In[122]:

import csv
import numpy


# In[67]:

exampleFile = open('tweets.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


# In[178]:

#I'd rather do this:
# from FormatTweet import stripTweet

import nltk
import string
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer


def ridHash(ortweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",ortweet).split())
    return(tweet)

def stripTweet(ortweet):
    tweet = ridHash(ortweet)
    tokenizer = RegexpTokenizer(r'\w+')
    twords = tokenizer.tokenize(tweet)
    twords_min = [None]
    stop = set(stopwords.words('english')) 
    
    for w in twords:
        if w.lower() not in stop:
            twords_min.append(w)
    del twords_min [0]
    return(twords_min)


# In[197]:

eachone = []
i = 0
for r in range(0,10,2):
    current = stripTweet(exampleData[r][1])
    del current [0]
    eachone.append(current)
    i+=1


# In[190]:

#Now use the classifier
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews


# In[191]:

def word_feats(words):
    return dict([(word, True) for word in words])


# In[182]:

nltk.download('movie_reviews')


# In[183]:

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')


# In[184]:

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]


# In[185]:

trainfeats = negfeats[:750] + posfeats[:750]
testfeats = negfeats[751:] + posfeats[751:]


# In[186]:

classifier = NaiveBayesClassifier.train(trainfeats)


# In[194]:

results = []

for c in eachone:
    res = classifier.classify(word_feats(c))
    results.append(res)


# In[198]:

print(results)


# In[ ]:



