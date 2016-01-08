
# coding: utf-8

#The only part of this code that is not generic is that the input file
# MUST be called geotweets.csv

# In[263]:

import csv
import numpy


# In[264]:

#Read in the data
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


#Define function to remove twitter handles using regular expressions
def ridHash(ortweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",ortweet).split())
    return(tweet)

#Define function to take the original tweet and remove stopwords and punctuation
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

#Extract each of the tweets from the csv file and put them in a list
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

#Download the movie review data which will be used for training the classifier
nltk.download('movie_reviews')


# In[270]:

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')


# In[271]:

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]


# In[272]:

#Split data into a training and testing set
trainfeats = negfeats[:750] + posfeats[:750]
testfeats = negfeats[751:] + posfeats[751:]


# In[273]:

#Train the classifier
classifier = NaiveBayesClassifier.train(trainfeats)

#Note that all the nltk module is AWESOME. As is Jacob from StreamHackers.com for his amazing tutorial.


# In[274]:

#Classify the tweets and append them into a list
results = []

for c in eachone:
    res = classifier.classify(word_feats(c))
    results.append(res)


# In[278]:

#Count how many tweets in each category (positive or negative)
counts = Counter(results)


# In[276]:

print(counts)


# In[305]:

# Turn the values into a list (much easier to use for the next part)
values = list(counts.values())


# In[277]:

#Plot!
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

#Only a very basic pie chart but you get the idea.

#In theory, it should be relatively easy to reassociate the coordinates with the tweet sentiment, which could then be mapped.
#No time for this, though.


# In[ ]:



