#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:35:20 2020

@author: tomaszzurek
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('weather_madrid_LEMD_1997_2015.csv')

for col in ['Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Dew PointC', 'MeanDew PointC', 'Min DewpointC']:
    df[col] = df[col] + 100

def wynik(y_test, predictions):
    print(metrics.confusion_matrix(y_test, predictions))
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))

X = df[
    ["CET",
     "Max TemperatureC",
     "Mean TemperatureC",
     "Min TemperatureC",
     "Dew PointC",
     "MeanDew PointC",
     "Min DewpointC",
     "Max Humidity",
     " Mean Humidity",
     " Min Humidity",
     " Max Sea Level PressurehPa",
     " Mean Sea Level PressurehPa",
     " Min Sea Level PressurehPa",
     " Max VisibilityKm",
     " Mean VisibilityKm",
     " Min VisibilitykM",
     " Max Wind SpeedKm/h",
     " Mean Wind SpeedKm/h",
     " Max Gust SpeedKm/h",
     "Precipitationmm",
     " CloudCover",
     "WindDirDegrees"]
]
y = df[' Events']

for i in range(len(X['CET'])):
    X.at[i, 'CET'] = pd.DatetimeIndex(X['CET']).month[i]

for j in X:
    if X[j].isna().sum() > X['CET'].count() * (1 / 3):
        X = X.drop(j, axis='columns')

X = X.fillna(method='ffill')
y = df[' Events'].fillna('Sunny')
df.ffill(axis=0, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print('random forest')
rf_model = RandomForestClassifier(n_estimators=100, criterion='gini')
rf_model.fit(X_train, y_train)
predictions = rf_model.predict(X_test)
wynik(y_test, predictions)

print('multinomial bayes')
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
predictions = nb_model.predict(X_test)
wynik(y_test, predictions)

print('GaussianNB')
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
predictions = nb_model.predict(X_test)
wynik(y_test, predictions)

print('BernoulliNB')
nb_model = BernoulliNB()
nb_model.fit(X_train, y_train)
predictions = nb_model.predict(X_test)
wynik(y_test, predictions)

# abc = [[41, 32, 28, 20, 16, 14, 100, 100, 100, 100, 1047, 1043, 1041, 31, 31, 31, 182, 39, 103, 1, 360]]
#
# predictionrf = rf_model.predict(abc)
# predictionnb = nb_model.predict(abc)
# print(predictionrf)
# print(predictionnb)