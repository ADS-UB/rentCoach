from twisted.enterprise import adbapi   
import time  
from httplib2 import Http
from simplejson import loads, dumps
import base64
import simplejson as json
from bson import json_util
import urllib

http_obj = Http()
url = "https://api.idealista.com/3.5/es/search"
apikey= urllib.parse.quote_plus('kn5fkovg91u9cuzo68pdiiwylgw878o1')
secret= urllib.parse.quote_plus('AK8NlpBSDmoV')
auth = apikey + ':' + secret
body = {'grant_type':'client_credentials&scope=write'}
headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Authorization' : 'Basic ' + str(base64.encode(auth.encode()))}
#Autenticacion en texto claro :( cambiar por token
resp, content = http_obj.request(url,method='POST',headers=headers, body=urllib.parse.urlencode(body))
print(content)
