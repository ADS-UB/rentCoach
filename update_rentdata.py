from twisted.enterprise import adbapi   
import time  
from httplib2 import Http
from simplejson import loads, dumps
import base64
from bson import json_util
import urllib
import unidecode
import csv
import json
import csv
#import MySQLdb

def get_oauth_token():
    http_obj = Http()
    url = "https://api.idealista.com/oauth/token"
    apikey= urllib.parse.quote_plus('kn5fkovg91u9cuzo68pdiiwylgw878o1')
    secret= urllib.parse.quote_plus('AK8NlpBSDmoV')
    auth ='ZmN2OWgybXAxcmRsZnJiZWl1aDV1bXo1b2Vya2pwaXk6YjU1T0pVVTF1UUQz' #'a241Zmtvdmc5MXU5Y3V6bzY4cGRpaXd5bGd3ODc4bzE6QUs4TmxwQlNEbW9W'#apikey + ':' + secret
    body = {'grant_type':'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Authorization' : 'Basic ' + auth}
    resp, content = http_obj.request(url,method='POST',headers=headers, body=urllib.parse.urlencode(body))
    return json.loads(content.decode('utf-8'))["access_token"]

def search_api(token, page):
    http_obj = Http()
    #token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0NzY5MDY1NTAsInNjb3BlIjpbInJlYWQiXSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QVUJMSUMiXSwianRpIjoiMGM0NTc5ZDQtZWFmMi00ZTAxLWJmNGYtNTQzZDBhMWMzZGVmIiwiY2xpZW50X2lkIjoia241Zmtvdmc5MXU5Y3V6bzY4cGRpaXd5bGd3ODc4bzEifQ.SduicVE561Y23O9_IicHqZ2SrxpBiIPbMl8HMdyQcE4"
    url = "http://api.idealista.com/3.5/es/search?center=41.402165058,2.171332648&country=es&maxItems=5000&distance=40000&propertyType=homes&operation=rent&numPage=" + str(page)
    headers = {'Authorization' : 'Bearer ' + token}
    resp, content = http_obj.request(url,method='POST',headers=headers)
    return json.loads(content.decode('utf-8'))

def save_check(dic, key):
    if key not in dic:
        return "NaN"
    return dic[key]
    
def from_json_to_csv(values):
    #with open('raw_update_rentdata.txt') as data_file:
    #    print(unidecode.unidecode(data_file.read())) 
    #    values = json.loads(unidecode.unidecode(data_file.read()))
        
    f = csv.writer(open("update_rentdata.csv", "a"))

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["propertyCode", "thumbnail", "numPhotos", "floor", "price", "propertyType", "operation", "size", "exterior", "rooms", "bathrooms", "address", "province", "municipality","district", "country", "neighborhood", "latitude", "longitude", "showAddress", "url", "distance","hasVideo", "newDevelopment", "tenantNumber", "tenantGender", "hasLift", "isSmokingAllowed","priceByArea"])
    

    for element in values["elementList"]:
        f.writerow([save_check(element, "propertyCode"), save_check(element, "thumbnail"), save_check(element, "numPhotos"), save_check(element, "floor"), save_check(element, "price"), save_check(element, "propertyType"), save_check(element, "operation"), save_check(element, "size"), save_check(element, "exterior"), save_check(element, "rooms"), save_check(element, "bathrooms"), save_check(element, "address"), save_check(element, "province"), save_check(element, "municipality"), save_check(element, "district"), save_check(element, "country"), save_check(element, "neighborhood"), save_check(element, "latitude"), save_check(element, "longitude"), save_check(element, "showAddress"), save_check(element, "url"), save_check(element, "distance"), save_check(element, "hasVideo"), save_check(element, "newDevelopment"), save_check(element, "tenantNumber"), save_check(element, "tenantGender"), save_check(element, "hasLift"), save_check(element, "isSmokingAllowed"), save_check(element, "priceByArea")])

def from_csv_to_db(filename):
    mydb = MySQLdb.connect(host='192.185.92.181',
        user='rentcoac_adsteam',
        passwd='LlB7Rq1CMP]z',
        db='rentcoac_ads')
    cursor = mydb.cursor()

    csv_data = csv.reader(file(filename + '.csv'))
    for row in csv_data:

        cursor.execute('INSERT INTO testcsv(names, \
              classes, mark )' \
              'VALUES("%s", "%s", "%s")', 
              row)
    #close the connection to the database.
    mydb.commit()
    cursor.close()
    
token = get_oauth_token()
print(token)
content = search_api(token, 1)
numPage = content["totalPages"]
from_json_to_csv(content)
for page in range(2,numPage):
    content = search_api(token, page)
    print(content)
    from_json_to_csv(content)

#mapping_db(search_api(""))
#print(get_oauth_token())
