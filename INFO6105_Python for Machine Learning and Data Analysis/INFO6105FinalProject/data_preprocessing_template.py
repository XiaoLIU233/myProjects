# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
#创建包含自变量的矩阵
X = dataset.iloc[:,:-1].values
#创建包含因变量的矩阵
Y = dataset.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.preprocessing import Imputer  
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# 分类数据
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:,0] = labelEncoder_X.fit_transform(X[:,0])
# 虚拟加密
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelEncoder_y = LabelEncoder()
Y = labelEncoder_y.fit_transform(Y)

# 划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# Feature Scaling 特征缩放
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
#"""from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)"""