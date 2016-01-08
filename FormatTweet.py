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