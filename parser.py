import json

if __name__=="__main__":
    with open('data/dnac_devices.json','r') as dat:
        js=json.load(dat)
#id, type, family, softwareType, managementIpAddress    
    for el in js['response']:
        print('---------------------------------')
        print('id: ',el['id'])
        print('type: ',el['type'])
        print('family: ',el['family'])
        print('softwareType: ',el['softwareType'])
        print('managementIpAddress: ',el['managementIpAddress'])