from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

from nltk.corpus import stopwords 

df = pd.read_csv('files/train_data.csv',encoding='latin-1')

#df = pd.read_csv('movie_data.tsv',sep = '\t')

#print(np.bincount(df.sentiment))

words = df.iloc[:,0].values

y = df.sentiment

#print(len(words))

vect = TfidfVectorizer() #stop_words = stopwords.words('english'))

vect.fit(words)

#print(vect.vocabulary_)

bgw = vect.transform(words)

#print(bgw)

bgw = bgw.toarray()

#print(arr)

# splitting X and y into training and testing sets 

from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(bgw,y, test_size=0.4, random_state=1) 


# training the model on training set 
from sklearn.naive_bayes import GaussianNB , MultinomialNB 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression

gnb = GaussianNB()

mnb = MultinomialNB() 

knc = KNeighborsClassifier()

rf = RandomForestClassifier()

abc = AdaBoostClassifier()

lr = LogisticRegression()

gnb.fit(X_train, y_train)

#print(gnb.classes_)

print(gnb.class_count_)

knc.fit(X_train, y_train)

rf.fit(X_train, y_train)

abc.fit(X_train, y_train)

lr.fit(X_train, y_train)

mnb.fit(X_train, y_train) 

# making predictions on the testing set 

# text = list(input("enter tweet : "))

# X_test = vect.transform(text).toarray()

#y_pred1 = gnb.predict(X_test)

#print(gnb.predict_proba(X_test))

#print(gnb.predict_log_proba(X_test))

def score(y_pred):

	Class = [0,0]

	for i in y_pred1:

		Class[i]+=1

	if(Class[0] > Class[1]):

		return (Class[0]/len(y_pred1))

	else:

		return (Class[1]/len(y_pred1))



y_pred1 = gnb.predict(X_test)

y_pred2 = knc.predict(X_test)

y_pred3 = rf.predict(X_test)

y_pred4 = abc.predict(X_test)

y_pred5 = lr.predict(X_test) 

y_pred6 = mnb.predict(X_test) 

# y_pred1,y_pred2,y_pred3,y_pred4,y_pred5,y_pred6 = list(y_pred1),list(y_pred2),list(y_pred3),list(y_pred4),list(y_pred5),list(y_pred6) 

# print(score(y_pred1),score(y_pred2),score(y_pred3),score(y_pred4),score(y_pred5),score(y_pred6))

# print()

# comparing actual response values (y_test) with predicted response values (y_pred) 

from sklearn import metrics 

print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred1)*100)

print("MultinomialNB model accuracy(in %):", metrics.accuracy_score(y_test, y_pred6)*100)

print("KNeighborsClassifier model accuracy(in %):", metrics.accuracy_score(y_test, y_pred2)*100)

print("RandomForestClassifier model accuracy(in %):", metrics.accuracy_score(y_test, y_pred3)*100)

print("AdaBoostClassifier model accuracy(in %):", metrics.accuracy_score(y_test, y_pred4)*100)

print("LogisticRegression model accuracy(in %):", metrics.accuracy_score(y_test, y_pred5)*100)
