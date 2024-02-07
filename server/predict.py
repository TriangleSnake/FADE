from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

model = joblib.load('asserts/model.pkl')
assert isinstance(model, RandomForestClassifier)

'''
profile pic,
nums/length username,
fullname words,
nums/length fullname,
name==username,
description length,
external URL,
private,
#posts,
#followers,
#follows
'''

result = model.predict()