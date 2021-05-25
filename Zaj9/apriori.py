#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:16:08 2021

@author: tomaszzurek
"""
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

dane = pd.read_csv('C:\\Python\\AI\\AI\\Zaj9\\supermarket.csv')
dane = dane.replace("?", 0)
dane = dane.replace("t", 1)
dane = dane.drop("total", axis='columns')

czeste = apriori(dane, min_support=0.1, use_colnames=True)
print(czeste)
reguly = association_rules(czeste, metric="confidence", min_threshold=0.7)
print(reguly)