import pandas as pd
import numpy as np

def calcular(neighborhood):
    data=pd.read_csv('version1.csv')
    data=data.drop(['Unnamed: 0'],axis=1)
    m=data[data['neighborhood']==neighborhood].mean()
    return m.price
