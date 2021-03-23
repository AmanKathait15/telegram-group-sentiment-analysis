#from textblob.classifiers import NaiveBayesClassifier

import csv,operator,re,itertools
import dictionary
import pandas as pd

from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize 

def remove_stopwords(tweet):

    stop_words = set(stopwords.words('english')) 

    word_tokens = word_tokenize(tweet)  
      
    tweet = [w for w in word_tokens if not w in stop_words]

    tweet = ' '.join(tweet)

    return tweet

def remove_contraction(tweet):

    CONTRACTIONS = dictionary.load_dict_contractions()

    tweet = tweet.replace("’","'")
    
    words = tweet.split()
    
    reformed = [CONTRACTIONS[word] if word in CONTRACTIONS else word for word in words]
    
    tweet = " ".join(reformed)

    return tweet

def clean_tweet(tweet):    
    
    #Escaping HTML characters
    tweet = re.sub(r"http\S+", "", tweet)
   
    #Special case not handled previously.
    tweet = tweet.replace('\x92',"'")

    tweet = remove_contraction(tweet)

    #removing retweet tag
    tweet = tweet.replace('RT',"")
    
    #Removal of hastags
    tweet = re.sub(r"#[A-Za-z0-9]+", "", tweet)

    #Removal of handle
    tweet = re.sub(r"@[A-Za-z0-9_]+", "", tweet,5)
    
    #Removal of address
    tweet = re.sub("(\w+:\/\/\S+)", "", tweet)
    
    #Removal of Punctuation
    tweet = re.sub("[\.\,\!\?\:\;\-\=]", " ", tweet)

    #tweet = re.sub(r'[^a-z]','',tweet)
    
    #Lower case
    tweet = tweet.lower()

    tweet = re.sub(r'[^a-z\s]','',tweet)

    tweet = remove_stopwords(tweet)
    
    return tweet


if __name__ == '__main__':

    df = pd.read_csv('files/train.csv',encoding='latin-1')

    msg = list(df['SentimentText'])

    message = msg[10000:15000]

    fp = open('files/data.csv','w')

    fp.write('tweet')

    for msg in message:

        msg = clean_tweet(msg)

        if(len(msg)>20):

            fp.write("\n"+msg)

    fp.close()

    print('complete')



    