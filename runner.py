import parser2
import dnac

if __name__=="__main__":
    authToken= dnac.getAuth("dnacdev","D3v93T@wK!","https://sandboxdnac2.cisco.com/api/system/v1/auth/token")
    dat= dnac.getDevices("https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device", authToken)
    parser2.read(dat)