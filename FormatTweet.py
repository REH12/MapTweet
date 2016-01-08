import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer


def tweetFun(tweet):
    tokenizer = RegexpTokenizer(r'\w+')
    twords = tokenizer.tokenize(tweet)
    twords_min = [None]

    stop = set(stopwords.words('english')) 
    
    for w in twords:
        if w.lower() not in stop:
            twords_min.append(w)
    del twords_min [0]
    return(twords_min)


