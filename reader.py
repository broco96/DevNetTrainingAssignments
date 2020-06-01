import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
from ruamel import yaml

if __name__=="__main__":
    with open('data/db.json','r') as dat:
        js=json.load(dat)
    
    for key in js:
        print(key)
        print('paid: ',js[key]['paid'])
        print('due: ',js[key]['due'])
        
    tree=ET.parse('data/db.xml')
    root=tree.getroot()

    for k in root.iter():
        print(k.tag+': '+k.text)
    
    with open('data/db.yml','r') as dat:
        yl=yaml.safe_load(dat)

    for key in yl:
        print(key)
        print('paid: ',yl[key]['paid'])
        print('due: ',yl[key]['due'])