
# coding: utf-8

# In[263]:

import csv
import numpy


# In[264]:

exampleFile = open('geotweets.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


# In[265]:

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


# In[266]:

eachone = []
i = 0
for r in range(0,len(exampleData),):
    current = stripTweet(exampleData[r][1])
    del current [0]
    eachone.append(current)
    i+=1


# In[267]:

#Now use the classifier
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews


# In[268]:

def word_feats(words):
    return dict([(word, True) for word in words])


# In[269]:

nltk.download('movie_reviews')


# In[270]:

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')


# In[271]:

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]


# In[272]:

trainfeats = negfeats[:750] + posfeats[:750]
testfeats = negfeats[751:] + posfeats[751:]


# In[273]:

classifier = NaiveBayesClassifier.train(trainfeats)


# In[274]:

results = []

for c in eachone:
    res = classifier.classify(word_feats(c))
    results.append(res)


# In[278]:

counts = Counter(results)


# In[276]:

print(counts)


# In[305]:

values = list(counts.values())


# In[277]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[307]:

# Data to plot
labels = 'Negative', 'Positive'
sizes = [values[0]/sum(values), values[1]/sum(values)]
colors = ['lightcoral', 'lightskyblue']
 
# Plot
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)
 
plt.axis('equal')
plt.show()


# In[ ]:



