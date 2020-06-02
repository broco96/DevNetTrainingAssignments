import requests
from base64 import b64encode
import json

def getAuth(user,pswd,url):
    
    userAndPass = b64encode(bytes(user + ':' + pswd, "utf-8")).decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    payload = {}
    files = {}
    headers = {
    'Authorization': 'Basic %s' %  userAndPass
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files)
    obj=json.loads(response.text)["Token"]
    return obj

def getDevices(url,token):
    payload = {}
    headers = {'x-auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZWNlNTc5ODc1MTYxMjAwY2M1NzA2M2QiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1ZSJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTU5MTA4OTc0MywiaWF0IjoxNTkxMDg2MTQzLCJqdGkiOiJiOTM4Zjc1ZS04Nzc2LTQwYTUtYTkxYy04MDU3ODY5MWU3YzUiLCJ1c2VybmFtZSI6ImRuYWNkZXYifQ.eVFAFH8ySVd1sUlxNDAwu2CtrPwauWa1xTkv5zz6GWmIrnY1PvtIZKEm1unuFnfBEfT4v_OKnZc2jlt1JHgd1j5yzf0HvlafP3QDNo5qn5Ol2yEtj9tqXRmBel5aNfyhH1aE2S5sTsUREb-hM6MelwUdXmWHM0xwZcs19Wd84qAOsqxID-BEh5QBhgyvMgoYWJv8Y0-PTMq8KJMfqfgIHga-Q4RMhv0VZDILAG-G7-bHUSKIfFfxbfIv_RWTyvUvwXHvwDrERb49AA4HqDcdWus8yHsMmwhn0HGmoR28XWMjW02jiBgC2jY-jotk_AJHMlictc9uoe-aottIOwxQRA'}

    response = requests.request("GET", url, headers=headers, data = payload)
    obj=json.loads(response.text)["response"]
    return obj
#getDevices("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device", getAuth("dnacdev","D3v93T@wK!","https://sandboxdnac2.cisco.com/api/system/v1/auth/token"))