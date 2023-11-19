import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
svm_regressor = SVR(kernel='linear', C=1)

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
svm_regressor.fit(X_train, y_train)
y_pred = svm_regressor.predict(X_test)
residuals = y_test - y_pred

mse = mean_squared_error(y_test, y_pred)
mean_train_target = np.mean(y_train)
baseline_predictions = np.full_like(y_test, mean_train_target)
baseline_mse = mean_squared_error(y_test, baseline_predictions)
print(f'Mean Squared Error: {mse:.2f}')
print(f'Baseline Mean Squared Error: {baseline_mse:.2f}')
print(f'Model reduction in MSE: {100.0 * mse / baseline_mse:.2f}%')
# Mean Squared Error: 3441.14
# Baseline Mean Squared Error: 6118.74
# Model reduction in MSE: 56.24%

plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red', linewidth=2)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('SVR: Actual vs. Predicted Values')
plt.savefig("svn_prediction.png")

plt.figure(figsize=(6, 6))
plt.scatter(range(len(residuals)), residuals)
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot for SVR Model')
plt.savefig("svn_residuals.png")
