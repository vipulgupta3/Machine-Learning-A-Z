# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 3].values
np.set_printoptions(threshold=np.nan)
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN", strategy='mean',axis=0)
imputer=imputer.fit(X[: ,1:3])
X[: ,1:3]=imputer.transform(X[: ,1:3])

