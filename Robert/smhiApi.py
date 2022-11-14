from smhi_open_data import SMHIOpenDataClient, Parameter


# # Get 10 stations
client = SMHIOpenDataClient()

# Get all stations
stations = client.get_stations()

# Get closest station
closest_station = client.get_closest_station(
    latitude=59.5972,
    longitude=16.6001)

# Get available parameters
parameters = client.list_parameters()

# # Get available parameters at station
parameters_station = client.get_station_parameters(station_id=96350)

# Get temperature observations from available stations from past hour
listFromSMHI = observations = client.get_latest_observations(parameter=Parameter.TemperaturePast1h)

#as = listFromSMHI["parameter_id"]

my_item = next((item for item in listFromSMHI if item['station'] =="96350"), None)

print(my_item)





#TemperaturePast1h = 1               # Lufttemperatur                        Momentanvärde, 1 gång/tim
#TemperaturePast24h = 2              # Lufttemperatur                        Medelvärde 1 dygn, 1 gång/dygn, kl 00
#WindDirection = 3                   # Vindriktning                          Medelvärde 10 min, 1 gång/tim
# WindSpeed = 4                       # Vindhastighet	                        Medelvärde 10 min, 1 gång/tim
#PrecipPast24hAt06 = 5               # Nederbördsmängd                       Summa 1 dygn, 1 gång/dygn, kl 06
#Humidity = 6                        # Relativ Luftfuktighet	                Momentanvärde, 1 gång/tim
#     PrecipPast1h = 7                    # Nederbördsmängd                       Summa 1 timme, 1 gång/tim
#SnowDepthPast24h = 8                # Snödjup                               Momentanvärde, 1 gång/dygn, kl 06
#Pressure = 9                        # Lufttryck reducerat havsytans nivå    Vid havsytans nivå, momentanvärde, 1 gång/tim
#     SunLast1h = 10                      # Solskenstid                           Summa 1 timme, 1 gång/tim
#     RadiaGlob = 11                      # Global Irradians (svenska stationer)  Medelvärde 1 timme, 1 gång/tim
#Visibility = 12                     # Sikt                                  Momentanvärde, 1 gång/tim
#     CurrentWeather = 13                 # Rådande väder                         Momentanvärde, 1 gång/tim resp 8 gånger/dygn
#     PrecipPast15m = 14                  # Nederbördsmängd                       Summa 15 min, 4 gånger/tim
#     PrecipMaxPast15m = 15               # Nederbördsintensitet                  Max under 15 min, 4 gånger/tim
#CloudCover = 16                     # Total molnmängd                       Momentanvärde, 1 gång/tim
#PrecipPast12h = 17                  # Nederbörd                             2 gånger/dygn, kl 06 och 18
#PrecipPast24hAt18 = 18              # Nederbörd                             1 gång/dygn, kl 18
#TemperatureMinPast24h = 19          # Lufttemperatur                        Min, 1 gång per dygn
#TemperatureMaxPast24h = 20          # Lufttemperatur                        Max, 1 gång per dygn
#     WindSpeedTown = 21                  # Byvind                                Max, 1 gång/tim
#TemperatureMeanPastMonth = 22       # Lufttemperatur                        Medel, 1 gång per månad
#PrecipPastMonth = 23                # Nederbördsmängd                       Summa, 1 gång per månad
#     LongwaveIrradians = 24              # Långvågs-Irradians                    Långvågsstrålning, medel 1 timme, varje timme
#     WindSpeedMaxMeanPast3h = 25         # Max av MedelVindhastighet             Maximum av medelvärde 10 min, under 3 timmar, ...
#TemperatureMinPast12h = 26          # Lufttemperatur                        Min, 2 gånger per dygn, kl 06 och 18
#TemperatureMaxPast12h = 27	        # Lufttemperatur                        Max, 2 gånger per dygn, kl 06 och 18
#     CloudLayerLowest = 28               # Molnbas                               Lägsta molnlager, momentanvärde, 1 gång/tim
#     CloudAmountLowest = 29              # Molnmängd                             Lägsta molnlager, momentanvärde, 1 gång/tim
#     CloudLayerOther = 30                # Molnbas                               Andra molnlager, momentanvärde, 1 gång/tim
#     CloudAmountOther = 31               # Molnmängd                             Andra molnlager, momentanvärde, 1 gång/tim
#     CloudLayer3rd = 32                  # Molnbas                               Tredje molnlager, momentanvärde, 1 gång/tim
#     CloudAmount3rd = 33                 # Molnmängd                             Tredje molnlager, momentanvärde, 1 gång/tim
#     CloudLayer4th = 34                  # Molnbas                               Fjärde molnlager, momentanvärde, 1 gång/tim
#     CloudAmount4th = 35                 # Molnmängd                             Fjärde molnlager, momentanvärde, 1 gång/tim
#     CloudStorageLowest = 36             # Molnbas                               Lägsta molnbas, momentanvärde, 1 gång/tim
#     CloudStorageLowestMin = 37          # Molnbas                               Lägsta molnbas, min under 15 min, 1 gång/tim
#     PrecipIntensityMaxMeanPast15m = 38  # Nederbördsintensitet                  Max av medel under 15 min, 4 gånger/tim
#TemperatureDew = 39                 # Daggpunktstemperatur                  Momentanvärde, 1 gång/tim
#GroundCondition = 40                # Markens tillstånd                     Momentanvärde, 1 gång/dygn, kl 06


# [{'parameter_id': 1, 'timestamp': 1668067200000, 'value': -3.5, 'station': '188790'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.6, 'station': '97280'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.7, 'station': '167710'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.6, 'station': '159880'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 5.4, 'station': '92410'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.1, 'station': '84340'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.6, 'station': '98040'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 1.9, 'station': '151280'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.0, 'station': '84900'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 0.0, 'station': '132110'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -1.8, 'station': '161940'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.2, 'station': '105260'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.5, 'station': '5032'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 5.4, 'station': '127130'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.3, 'station': '157870'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -3.7, 'station': '123460'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.4, 'station': '94390'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 2.0, 'station': '116490'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -0.8, 'station': '123060'}, {'parameter_id': 1, 'timestamp': 
# 1668067200000, 'value': 6.5, 'station': '115220'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.7, 'station': '107440'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.2, 'station': '97370'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.6, 'station': '96190'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 11.1, 'station': '52240'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.8, 'station': '107140'}, {'parameter_id': 1, 
# 'timestamp': 1668067200000, 'value': 8.1, 'station': '96040'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 0.7, 'station': '23059'}, {'parameter_id': 
# 1, 'timestamp': 1668067200000, 'value': -1.8, 'station': '148040'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.9, 'station': '78550'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -1.8, 'station': '134410'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.3, 'station': '155790'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.2, 'station': '76420'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.7, 'station': '89230'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 6.4, 'station': '20044'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -2.5, 'station': '145130'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.1, 'station': '147560'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.1, 'station': '103100'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -2.5, 'station': '144310'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.6, 'station': '180760'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.6, 'station': '107420'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.2, 
# 'station': '84520'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.4, 'station': '71420'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.2, 'station': '14'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.5, 'station': '72420'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.6, 'station': '15'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.0, 'station': '16'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.6, 'station': '74180'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 11.1, 'station': '62260'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -1.0, 'station': '135460'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.4, 'station': '62410'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 4.6, 'station': '114410'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.1, 'station': '64020'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -2.0, 'station': '163960'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.0, 'station': '87140'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.6, 'station': '62040'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -3.2, 'station': '155970'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -6.1, 'station': '155960'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -0.1, 'station': '138390'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 11.0, 'station': '68560'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 2.8, 'station': '140460'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.4, 'station': '75520'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -1.5, 'station': '146050'}, {'parameter_id': 
# 1, 'timestamp': 1668067200000, 'value': 10.1, 'station': '11044'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -0.2, 'station': '125440'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.2, 'station': '83190'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.4, 'station': '63160'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.7, 'station': '6057'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.4, 'station': '53530'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.2, 'station': '170860'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 0.3, 'station': '136410'}, 
# {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 1.9, 'station': '139260'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.8, 'station': '4'}, 
# {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.2, 'station': '74460'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.4, 'station': '66420'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.5, 'station': '192840'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.3, 'station': '84310'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 10.8, 'station': '65090'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.6, 'station': '93220'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.6, 'station': '188850'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.1, 'station': '106160'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.5, 'station': '85460'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.4, 'station': '94190'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.6, 'station': '12000'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -5.2, 'station': '180940'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 6.6, 'station': '95540'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 2.4, 'station': '124300'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.7, 'station': '86420'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 0.1, 'station': '133500'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.8, 'station': '65510'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.3, 'station': '82360'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 0.4, 'station': '136090'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 7.9, 'station': '117430'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 8.4, 'station': '85390'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -4.8, 'station': '167990'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.9, 'station': '11039'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': 9.7, 'station': '11039'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -0.1, 'station': '21041'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value': -3.0, 'station': '171790'}, {'parameter_id': 1, 'timestamp': 1668067200000, 'value'

