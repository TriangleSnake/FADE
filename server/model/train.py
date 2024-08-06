import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

data = np.genfromtxt('server/model/train.csv', delimiter=',', skip_header=1)

x_train = data[:,:-1]
y_train = data[:,-1]

data = np.genfromtxt('server/model/test.csv', delimiter=',', skip_header=1)

x_test = data[:,:-1]
y_test = data[:,-1]

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_val_scaled = scaler.transform(x_val)
x_test_scaled = scaler.transform(x_test)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(x_train_scaled, y_train)

print("Train accuracy: ", rf_model.score(x_test_scaled, y_test))

joblib.dump(rf_model, 'server/model/rf.pkl')
joblib.dump(scaler, 'server/model/scaler.pkl')