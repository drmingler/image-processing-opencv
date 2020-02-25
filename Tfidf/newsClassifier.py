import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

dataFile = pd.read_csv('./news.csv')

# checks the data  dataFile.head()

labels = dataFile.label

#DataFlair - Split the dataset. Train data usually be 70%~, more or less doesn't really make any change.
x_train,x_test,y_train,y_test=train_test_split(dataFile['text'], labels, test_size=0.30, random_state=0,shuffle=False)

# DataFlair - Initialize a TfidfVectorizer. stop_words is english, japanese is http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?JUMAN
# Juman library is written by Kyoto University senseis. Honor them!

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.70)

#DataFlair - Fit and transform train set, transform test set. fit is applied to test data, fit&transform is for train data.
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

#PAC 二分類Classifier : Passive Aggressive Classifier
# 二値分類ではデータが入力xから二値の出力y∈{-1, +1}を推定。 
#その中でも線形分類器はモデルパラメタWで特徴づけられ、入力xに対し、sign(WTx)を推定。sign(x)はxが0以上ならば１を、負ならば-1を返す関数。

pac=PassiveAggressiveClassifier(max_iter=50) #How many times the data will be filtered. 
pac.fit(tfidf_train,y_train) #fit the trained data and label.
y_pred=pac.predict(tfidf_test) # calculate accuracy of the test data compared to original label data. - > FAKE OR REAL

#y_pred is PAC implemented list of "real | fake" of tfidf train data. 
score=accuracy_score(y_test,y_pred)
print("Acurracy with PAC, %d" % score)

table = confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])
#This contains compared table of fake\real news analysis.


# Things I wanted to do but could not
# Use Tfidf_Vectorizer that is trained to test full raw data with 
datafile = dataFile.drop["label"]
# So that I could test this Tfidf_vectorizor to aquire result. 

#WHAT IN THE DATA SCIENCE'S NAME IS THIS!?
