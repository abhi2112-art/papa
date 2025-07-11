# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YSst5HTOOG_6NZWwxE45-i9nheRS5ULB
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("/content/Titanic-Dataset.csv")
data

data.isnull().sum()

X = data.drop("Cabin", axis=1)

data.isnull().sum()

data.select_dtypes(int)

data.select_dtypes(object)

data.select_dtypes(object).columns

bank = pd.get_dummies(data,columns= ["Name", "Sex", "Ticket", "Cabin", "Embarked"],drop_first=True,dtype=int)

bank

data.select_dtypes(int)

def IQR(x):
    q1=x.quantile(0.25)
    q3=x.quantile(0.75)
    iqr=q3-q1
    lf=q1-(1.5*iqr)
    uf=q3+(1.5*iqr)
    print("LF",lf)
    print("UF",uf)

IQR(data["Survived"])

data["Survived"]=np.where(data["Survived"]>2,2,data["Survived"])

IQR(data["Pclass"])

data["Pclass"]=np.where(data["Pclass"]>4,4,data["Pclass"])

IQR(data["SibSp"])

data["SibSp"]=np.where(data["SibSp"]>2.5,2.5,data["SibSp"])

IQR(data["Parch"])

IQR(data["Age"])

median_value=data['Age'].median()

data["Age"]=data["Age"].fillna(median_value)

IQR(data["Age"])

data["Age"]=np.where(data["Age"]>54,54,data["Age"])

X = pd.get_dummies(X, drop_first=True)

X = data.drop("Name", "Sex", "Ticket", "Cabin", "Embarkedt", axis=1)
y = data["Survived"]

X = pd.get_dummies(X, drop_first=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(X_train, y_train)