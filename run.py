import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("update_rentdata_26102016.csv",sep=",")

# delete lines containing header again (ev. 50 row approx.)
data = data[data['propertyCode']!='propertyCode']

# drop some features
data = data.drop(['operation','address','country','distance','tenantGender','tenantNumber','isSmokingAllowed'],axis=1)

# replace string by numbers in 'floor' column
data['floor']=data['floor'].fillna(value='1000')
data = data.replace(to_replace='bj', value='0', inplace=False, limit=None, regex=False, method='pad', axis=None)
data = data.replace(to_replace='en', value='1', inplace=False, limit=None, regex=False, method='pad', axis=None)
data = data.replace(to_replace='ss', value='-1', inplace=False, limit=None, regex=False, method='pad', axis=None)

#Converting some selected features to float
tofloat=['price','priceByArea','numPhotos','size','propertyCode','rooms']
###To be used when the floor feature is only numeric:
###tofloat=['price','priceByArea','numPhotos','size','propertyCode','rooms','floor']
for col in tofloat:
    data[col]=data[col].astype(float)

#Converting some dummy features to 0 or 1
    
def truedummy(feature,df):
    dummies_numpy = np.where(df[feature]=='True',1,0)
    df[feature]= dummies_numpy
    
to_zero_or_one=["exterior","showAddress","hasVideo","newDevelopment","hasLift"]
for col in to_zero_or_one:
    truedummy(col,data)
    ###For analytics purposes:
    ###print col
    ###print plt.hist(data[col], bins=[0,1,2])
    ###plt.show()

#Take only municipality Barcelona
data[data['municipality']=='Barcelona']

#remove outliers price
per=np.percentile(np.array(data['price']), [2.5, 97.5])
data=data[data['price']>per[0]]
data=data[data['price']<per[1]]

data.to_csv("version1.csv")
