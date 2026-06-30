import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


data = pd.read_csv("c:/Users/irfan/Desktop/Python/ML/Linear Regression/Student_Performance.csv")

data['Extracurricular Activities'] = data['Extracurricular Activities'].replace({
    'Yes': 1,
    'No': 0
})
# print(data.head())


X_train = data.iloc[:, :-1].to_numpy(dtype=float)
Y_train = data.iloc[:, -1].to_numpy(dtype=float)

scaler = StandardScaler()
X_normalized = scaler.fit_transform(X_train)

print(f"Normalized Features:\n{np.ptp(X_normalized, axis=0)}")

# fig , ax = plt.subplots(1, 5, figsize=(12, 5), sharey=True)
# for i in range(len(data.columns)-1):
#     ax[i].scatter(X_normalized[:,i], data.iloc[:, -1])
#     ax[i].set_xlabel(data.columns[i])
#     ax[i].set_ylabel('Final Grade')
# plt.show()

# sgdr = SGDRegressor(max_iter=10000)
# sgdr.fit(X_normalized, Y_train)
# print(f"number of iterations completed: {sgdr.n_iter_}, number of weight updates: {sgdr.t_}")

# print(f"Model Coefficients: {sgdr.coef_}")
# print(f"Model Intercept: {sgdr.intercept_}")

# Y_predict = sgdr.predict(X_normalized)

lr = LinearRegression()
lr.fit(X_normalized, Y_train)

Y_predict = lr.predict(X_normalized)

fig,ax=plt.subplots(1,4,figsize=(12,3),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i],Y_train, label = 'target')
    ax[i].set_xlabel(data.columns[i])
    ax[i].scatter(X_train[:,i],Y_predict,color='red', label = 'predict')
ax[0].set_ylabel("Price"); ax[0].legend();
fig.suptitle("target versus prediction using z-score normalized model")
plt.show()

def cost_calc(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

print(f"Cost of the model: {cost_calc(Y_train, Y_predict)}")