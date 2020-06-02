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
    headers = {'x-auth-token': token }

    response = requests.request("GET", url, headers=headers, data = payload)
    obj=json.loads(response.text)["response"]
    return obj
#getDevices("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device", getAuth("dnacdev","D3v93T@wK!","https://sandboxdnac2.cisco.com/api/system/v1/auth/token"))