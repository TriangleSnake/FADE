from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib

def predict(data :list,) -> bool:
    model = joblib.load('server/model/rf.pkl')
    scaler = joblib.load('server/model/scaler.pkl')
    if data == []:
        return 1
    data =[data]
    data = np.array(data)
    data = scaler.transform(data)
    predict = model.predict(data)
    return predict
