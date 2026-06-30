import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("c:/Users/irfan/Desktop/Python/ML/Linear Regression/manufacturing.csv")

print(data.columns)

X_train = data.iloc[:500, :-1].to_numpy(dtype=float)
Y_train = data.iloc[:500, -1].to_numpy(dtype=float)

X_test = data.iloc[500:, :-1].to_numpy(dtype=float)
Y_test = data.iloc[500:, -1].to_numpy(dtype=float)

pdata = PolynomialFeatures(degree=10, include_bias=False)
X_train_poly = pdata.fit_transform(X_train)
X_test_poly = pdata.transform(X_test)

# fig,ax = plt.subplots(1,len(X_train[0,:]),sharey=True,figsize=(12,3))
# for i in range(len(ax)):
#     ax[i].scatter(X_train[:,i],Y_train, label = 'target')
#     ax[i].set_xlabel(data.columns[i])
# plt.show()    

X = np.c_[X_train[:,0],(-1)*X_train[:,0]**2 ,X_train[:,1], X_train[:,2], (-1)*X_train[:,3]**2, (-1)*X_train[:,3]**2]

lr = LinearRegression()
lr.fit(X_train_poly, Y_train)

Y_predict = lr.predict(X_test_poly)
cost = np.mean((Y_test - Y_predict) ** 2)

plt.scatter(X_test_poly[:,0], Y_test, marker='x', c='r', label="Actual Value"); plt.title("Testing Data");
plt.plot(X_test_poly[:,0],Y_predict, label="Predicted Value"); plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.show()


print(f"Cost of the model: {cost}")