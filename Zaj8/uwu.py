#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:35:20 2020

@author: tomaszzurek
"""

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

df = pd.read_csv('weather_madrid_LEMD_1997_2015.csv')
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

sse = []
# for k in range(1, 16):
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=100)
pred_y = kmeans.fit(X_train)
sse.append(kmeans.inertia_)
print(pred_y.cluster_centers_)

predictions = pred_y.predict(X_test)
lst = []
y_test = list(y_test)
for i in range(len(y_test)):
    print(str(y_test[i]) + ' ' + str(predictions[i]))

# plt.style.use("fivethirtyeight")
# plt.plot(range(1, 16), sse)
# plt.xticks(range(1, 16))
# plt.xlabel("Number of Clusters")
# plt.ylabel("SSE")
# plt.show()

# https://realpython.com/k-means-clustering-python/
# The elbow method, wedlog tej metody wybralem 3 klastry
