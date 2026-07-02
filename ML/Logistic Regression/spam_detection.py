import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("c:/Users/irfan/Desktop/Python/ML/Logistic Regression/spam_detection_dataset.csv")

print(len(data.iloc[:, 0]), "rows and", len(data.columns), "columns in the dataset.")

data = data.drop(columns=["message"])
print(data.head())

data['label'] = data['label'].map({'ham': 0, 'spam': 1})
print(f"data after mapping labels:\n{data.head()}")

X_train = data.iloc[:, 1:].to_numpy()
Y_train = data.iloc[:, 0].to_numpy()


print(f"X_train shape: {X_train.shape}, Y_train shape: {Y_train.shape}")

lr = LogisticRegression(max_iter=10000)
lr.fit(X_train, Y_train)

print(f"Training accuracy: {lr.score(X_train, Y_train):.4f}")
