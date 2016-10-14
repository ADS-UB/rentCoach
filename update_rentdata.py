from twisted.enterprise import adbapi   
import time  
from httplib2 import Http
from simplejson import loads, dumps
import base64
import simplejson as json
from bson import json_util
import urllib

def get_oauth_token():
    http_obj = Http()
    url = "https://api.idealista.com/oauth/token"
    apikey= urllib.parse.quote_plus('kn5fkovg91u9cuzo68pdiiwylgw878o1')
    secret= urllib.parse.quote_plus('AK8NlpBSDmoV')
    auth = 'a241Zmtvdmc5MXU5Y3V6bzY4cGRpaXd5bGd3ODc4bzE6QUs4TmxwQlNEbW9W'#apikey + ':' + secret
    body = {'grant_type':'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Authorization' : 'Basic ' + auth}
    resp, content = http_obj.request(url,method='POST',headers=headers, body=urllib.parse.urlencode(body))
    return content

def search_api(token):
    http_obj = Http()
    #token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0NzY0OTY1OTcsInNjb3BlIjpbInJlYWQiXSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QVUJMSUMiXSwianRpIjoiOTg3NzI5MzQtODZmNi00ZDhkLTkzMDEtOWJlYmMwOTI3NDE2IiwiY2xpZW50X2lkIjoia241Zmtvdmc5MXU5Y3V6bzY4cGRpaXd5bGd3ODc4bzEifQ.cz1ZMFFl57p4KbtExZ5s2AF_r0DbKqL3QIh4CvZCUSk'
    url = "http://api.idealista.com/3.5/es/search?center=40.42938099999995,-3.7097526269835726&country=es&maxItems=50&numPage=1&distance=452&propertyType=bedrooms&operation=rent"
    headers = {'Authorization' : 'Bearer ' + token}
    resp, content = http_obj.request(url,method='POST',headers=headers)
    return content

def mapping_db(content):
    values = json.load(content)

print(search_api())
