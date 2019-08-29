# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import pandas as pd
import numpy as np
import random as rnd

#visualisation
import seaborn as sns
import matplotlib.pyplot as plt 
"%matplotlib inline"

#machine learning algos
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier




#acquire train and test data using pandas
train_df = pd.read_csv('Data/train.csv')
test_df = pd.read_csv('Data/test.csv')
#combine the two data sets to run certain operations at once
combine = [train_df, test_df]


print(train_df.info())





















