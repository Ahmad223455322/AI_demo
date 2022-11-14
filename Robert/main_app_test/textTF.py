import requests
import pandas as pd

data = """
<REQUEST>
      <LOGIN authenticationkey="8c981e556ca74fa7b2128c113e4eeb8c" />
      <QUERY objecttype="WeatherStation" schemaversion="1">
            <FILTER>
                  <EQ name="Name" value="Vallby" />
            </FILTER>            
            <INCLUDE>Name</INCLUDE>
            <INCLUDE>Measurement.Air.Temp</INCLUDE>
            <INCLUDE>Measurement.MeasureTime</INCLUDE>
            <INCLUDE>Measurement.Air.RelativeHumidity</INCLUDE>
            <INCLUDE>Measurement.Precipitation.AmountName</INCLUDE>
            <INCLUDE>Measurement.Precipitation.Amount</INCLUDE>
      </QUERY>
</REQUEST>
"""
data = data.encode('utf8')
response = requests.post('https://api.trafikinfo.trafikverket.se/v2/data.json', data=data, headers={'Content-Type': 'text/xml'}).json()

results = response.get('RESPONSE')
nestedDict = results.get("RESULT")
nestedList = nestedDict[0].get("WeatherStation")
measurement = nestedList[0]
stationData = measurement.get("Measurement")
measureTime = stationData.get("MeasureTime")
airInformation = stationData.get("Air")
airTemperature = airInformation.get("Temp")
airRelativeHumidity = airInformation.get("RelativeHumidity")
precipitation = stationData.get("Precipitation")
donwfall = precipitation.get("Amount")
donwfallType = precipitation.get("AmountName")
stationName = measurement.get("Name")

print(stationName,measureTime,airTemperature,airRelativeHumidity,donwfall,donwfallType)