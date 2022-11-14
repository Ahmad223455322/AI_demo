import requests
import json
from datetime import datetime


import xml.etree.cElementTree as ET
import urllib
import urllib.request
data1= """
        
              <REQUEST>
                  <LOGIN authenticationkey="8c981e556ca74fa7b2128c113e4eeb8c"/>
                      <QUERY objecttype="WeatherStation" schemaversion="1">
                          <FILTER>
                              <EQ name="Name" value="Rotebro" />
                          </FILTER>
                          <INCLUDE>Measurement.Air.Temp</INCLUDE>
                          <INCLUDE>Measurement.MeasureTime</INCLUDE>
                      </QUERY>
              </REQUEST>
              <REQUEST>
        
"""

data2 = str.encode(data1)
req = urllib.request.Request(url='https://api.trafikinfo.trafikverket.se/v2/data.xml', data=data2,headers = {'Content-Type':'text/xml'})
#print(requests.post('https://api.trafikinfo.trafikverket.se/v2/data.json', data=data, headers={'Content-Type': 'text/xml'}).json())


response = urllib.request.urlopen(req)
the_page = response.read()

the_page = ET.fromstring(the_page)

for child in the_page:
    for a in child:
        for b in a:
            if b.tag in ["LocationSignature"]:
                print(b.text+'\n')
            if b.tag in ["AdvertisedTrainIdent"]:
                print(b.text)

#req = requests.get("https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/96350/period/latest-day/data.json", "LOGIN": "addiva", "key":"8c981e556ca74fa7b2128c113e4eeb8c")



import requests
import json
from datetime import datetime

#/api/version/{version}/parameter/{parameter}/station/{station}/period/{period}/data.{ext}
#version = 1.0 eller latest, parameter är mätvärde (se listan), station är stationsID (96350 är Västerås), 
# perioderna är (latest-day, latest-hour, latest-months, corrected-archive), data är formatet (json, csv, xml, atom)
#

# responsekoder är 200 = request ok, 404 förmodligen producerar inte den stationen du vill åt denna typ av data, 500 betyder att något gått fel internt (hos smhi förmodligen) men kommer nog säkert åtgärdas
listOfTrafikverket = requests.get("https://api.trafikinfo.trafikverket.se/v2/data.json",data2 )

#my_item = next((item for item in listOfSMHI if item['value'] =="96350"), None)


print(listOfTrafikverket.json())
