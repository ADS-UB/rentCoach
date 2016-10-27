import numpy as np
import re
import pandas as pd
data=pd.read_csv("update_rentdata_26102016.csv",sep=",")

data=data[data['propertyCode']!='propertyCode']
# esto elimina los indices de las filas eliminadas--> hay que arreglarlo

data = data.drop(['thumbnail', 'address','url','tenantGender','tenantNumber','isSmokingAllowed','distance'], axis=1)

pattern='^\d'
data['floor']=data['floor'].fillna(value='1000')
llista=[]
for element in tuple(data['floor']):
    f=bool(re.match(pattern,element))
    if f==False:
        llista=np.append(llista,element)
#print llista
for i in np.unique(llista):
    data[data['floor']==i]='0'

tofloat=['price','priceByArea','numPhotos','size','propertyCode','rooms','floor']
for col in tofloat:
    data[col]=data[col].astype(float)

data[data['floor']==1000]=np.nan



