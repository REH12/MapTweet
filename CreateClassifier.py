
# coding: utf-8

# In[51]:

# Thanks to http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/


#Now use the classifier
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews


# In[52]:

def word_feats(words):
    return dict([(word, True) for word in words])


# In[53]:

nltk.download('movie_reviews')


# In[54]:

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')


# In[55]:

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]


# In[56]:

trainfeats = negfeats[:750] + posfeats[:750]
testfeats = negfeats[751:] + posfeats[751:]


# In[57]:

classifier = NaiveBayesClassifier.train(trainfeats)


# In[ ]:

#To classify the new tweets, use: 
# classifier.classify(word_feats(tweet))

