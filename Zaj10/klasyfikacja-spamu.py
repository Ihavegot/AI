#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:21:05 2020

@author: tomaszzurek
"""

import pandas as pd
from mlxtend.feature_selection import ColumnSelector
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn import metrics


def wynik(y_test, predictions):
    print(metrics.confusion_matrix(y_test, predictions))
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))


df = pd.read_csv('train-amazon.tsv', sep='\t')
X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train.shape)
print(y_train.shape)

text_clf = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1, 2), smooth_idf=False)), ('clf', LinearSVC())]) # 88%
# text_clf = Pipeline([('count_vec', CountVectorizer(stop_words='english', ngram_range = (1,2))), ('clf', RandomForestClassifier())]) # 83%
# text_clf = Pipeline([('count_vec', CountVectorizer(stop_words='english')), ('clf', LinearSVC())]) # 81%
# text_clf = Pipeline([('count_vec', CountVectorizer()), ('clf', RandomForestClassifier())]) # 83%
print(text_clf)
text_clf.fit(X_train, y_train)
predictions = text_clf.predict(X_test)
print(predictions)
wynik(y_test, predictions)
proba = [
    "I've seen many other reviews saying this monitor does not tilt, but it in fact does. I'm guessing people didn't "
    "take a close enough look at the hinge mechanism in the base, which attaches to the main display and allows for "
    "backwards tilt of approximately 15 degrees. The monitor is very light, thin, has small bezels, and produces "
    "reasonably good colors. It doesn't have a vesa mount, but I knew that before purchasing it, and wasn't planning "
    "to mount it. For $89, it is a great value.",
    "I very rarely write reviews, but am so disappointed with this monitor, that I felt the need to warn others. "
    "Originally bought this last year to use for school and work. After a few weeks, started having issues with it "
    "turning off and repeatedly blinking in mid-use, as well as dead pixels in the middle of the screen. Contacted "
    "Amazon, and they sent a replacement and I returned the original. Again, a few weeks of perfect operation. Then on "
    "the replacement unit, the power and menu buttons stopped working. The only way to turn on and off was to physically "
    "unplug the unit. Contacted Amazon again, and they referred me to the manufacturer. After several attempts, "
    "I finally got a hold of a person. They said they would look at, but I would have to ship it back on my own dime, "
    "and they would not replace it. I declined (mostly because I didn't have a box to pack it in, and was severely "
    "unimpressed with customer service). "
    ]
predictions = text_clf.predict(proba)
print(predictions)