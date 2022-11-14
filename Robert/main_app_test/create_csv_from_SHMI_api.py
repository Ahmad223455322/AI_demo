import requests
import json
from datetime import datetime

#/api/version/{version}/parameter/{parameter}/station/{station}/period/{period}/data.{ext}
#version = 1.0 eller latest, parameter är mätvärde (se listan), station är stationsID (96350 är Västerås), 
# perioderna är (latest-day, latest-hour, latest-months, corrected-archive), data är formatet (json, csv, xml, atom)
#

# responsekoder är 200 = request ok, 404 förmodligen producerar inte den stationen du vill åt denna typ av data, 500 betyder att något gått fel internt (hos smhi förmodligen) men kommer nog säkert åtgärdas
listOfSMHI = requests.get("https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/96350/period/latest-day/data.json")

#my_item = next((item for item in listOfSMHI if item['value'] =="96350"), None)
listOfYR = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.60&lon=16.55")


print(listOfSMHI.json())
print()
print(listOfYR)



# timestamp = 1545730073
# dt_object = datetime.fromtimestamp(timestamp)

# print("dt_object =", dt_object)
# print("type(dt_object) =", type(dt_object))