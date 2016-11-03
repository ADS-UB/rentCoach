import pandas as pd

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