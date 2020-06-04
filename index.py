#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb
cgitb.enable() # Enable debugging
print("<h1>Below is the execution output of the script</h1>")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######

import requests
import dnac

#if __name__=="__main__":
 
print("<h3>Printing Token...</h3>")
token = dnac.getAuth("dnacdev","D3v93T@wK!","https://sandboxdnac2.cisco.com/api/system/v1/auth/token")
print("<h3>Token</h3><br><br>{}".format(token) )
print("<h3>Token printed</h3>")

