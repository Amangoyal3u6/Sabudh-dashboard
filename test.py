import pickle
import pandas as pd
import numpy

max = pickle.load(open('static/csv/max_forecast','rb'))
max = max.tolist()
print(len(max))
min = pickle.load(open('static/csv/min_forecast','rb'))
min = min.tolist()
print(len(min))
mxspd = pickle.load(open('static/csv/spd_forecast','rb'))
mxspd = mxspd.tolist()
print(len(mxspd))
df = pd.read_csv('static/csv/tempmax.csv')
df = df['date']
df = df.tolist()
print(len(df))
dd = df = pd.read_csv('static/csv/tempmax.csv')
pf = pd.DataFrame