import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# Load dataset
data = pd.read_csv("c:/Users/irfan/Desktop/Python/ML/Linear Regression/manufacturing.csv")

print("Dataset Columns:", list(data.columns))

fig,ax = plt.subplots(1,len(data.columns) - 1,figsize=(12, 6),sharey=True)

for i, col in enumerate(data.columns[:-1]):
    ax[i].scatter(data[col], data.iloc[:, -1], alpha=0.5)
    ax[i].set_title(f"{col} vs Quality Rating")
    ax[i].set_xlabel(col)
    ax[i].set_ylabel("Quality Rating")
plt.show()
# Temperature (col 0) is the only variable determining the Quality Rating (col -1).
# We use only Temperature to simplify the model and avoid high-dimensional multicollinearity.
X_raw = data.iloc[:, [0]].to_numpy(dtype=float)
Y_raw = data.iloc[:, -1].to_numpy(dtype=float)

# Split into train/test sets (first 500 for training, the rest for testing)
X_train = X_raw[:500]
Y_train = Y_raw[:500]
X_test = X_raw[500:]
Y_test = Y_raw[500:]

# 1. Scale the features to ensure numerical stability in high-degree polynomial calculation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 2. Generate polynomial features (Degree 10 models the exponential curve elegantly)
pdata = PolynomialFeatures(degree=10, include_bias=False)
X_train_poly = pdata.fit_transform(X_train_scaled)
X_test_poly = pdata.transform(X_test_scaled)

# 3. Fit the Linear Regression model
lr = LinearRegression()
lr.fit(X_train_poly, Y_train)

# 4. Predictions and metrics
Y_predict_train = lr.predict(X_train_poly)
Y_predict_test = lr.predict(X_test_poly)

train_cost = np.mean((Y_train - Y_predict_train) ** 2)
test_cost = np.mean((Y_test - Y_predict_test) ** 2)

print(f"Number of model features: {X_train_poly.shape[1]}")
print(f"Train Cost (MSE): {train_cost:.6f}")
print(f"Test Cost (MSE): {test_cost:.6f}")

# 5. Plot the testing data and predictions
# Sort by Temperature to plot a clean, smooth prediction curve rather than a jagged mesh
sort_idx = np.argsort(X_test[:, 0])
X_test_sorted = X_test[sort_idx, 0]
Y_test_sorted = Y_test[sort_idx]
Y_predict_sorted = Y_predict_test[sort_idx]

# plt.figure(figsize=(10, 6))
# plt.scatter(X_test_sorted, Y_test_sorted, marker='x', c='#e74c3c', alpha=0.7, label="Actual Value")
# plt.plot(X_test_sorted, Y_predict_sorted, c='#3498db', linewidth=2.5, label="Predicted Value")
# plt.title("Testing Data: Actual vs Predicted Quality Rating")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Quality Rating")
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()