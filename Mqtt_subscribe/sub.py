import time
import paho.mqtt.subscribe as subscribe
import json
import pymongo
from datetime import datetime
import pandas as pd


# client_databas = pymongo.MongoClient("mongodb://localhost:27017/")

# min_databas = client_databas["DBsensor_data"]

# collation = min_databas["room_data"]
# mylist=[]


# def subscribe_func():

#     while True:
#         tid_nu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         m = subscribe.simple(topics="#", hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"ap-addiva-01@ttn",'password':"NNSXS.YCG3Y43HFVAAFXJ243XAKP55ZCWOBNA65KIPBOY.LW366SHGZUIDHLEF4GWJV5N7XOW6HFBKDTYYKJGXLFWVWLAEDCJQ"}, msg_count=2)
#         for a in m:
#             data_from_sensor =a.payload.decode("utf-8")
#             data_to_dict =  json.loads(data_from_sensor)

#         div_id = data_to_dict["end_device_ids"]["device_id"]
#         rums_data = data_to_dict["uplink_message"]["decoded_payload"]
#         data_to_insert_to_databas = {"Sensor_ID":div_id, "data":rums_data,"Tid":tid_nu}
#         collation.insert_one(data_to_insert_to_databas)
#         time.sleep(0)
        
#         for data in collation.find():
#             print(data)
import pandas as pd

from pymongo import MongoClient

from datetime import datetime

 

host = "mongodb://localhost"

port = 27017

db = "DBsensor_data"

collection = "room_data"

 

def _connect_mongo(host, port, db):

    conn = MongoClient(host, port)

    return conn[db]

 

def read_mongo(db, collection, query={}, host="mongodb://localhost", port=27017, username=None, password=None, no_id=False):

    # Connect to MongoDB

    db = _connect_mongo(host=host, port=port, db=db)

 

    # Make a query to the specific DB and Collection

    cursor = db[collection].find(query)

 

    # Expand the cursor and construct the DataFrame

    df =  pd.DataFrame(list(cursor))

 

    # Delete the _id

    if no_id:

        del df['_id']

 

    return df

 

_connect_mongo(host, port, db)

 

ourData = read_mongo(db, collection, query={}, host=host, port=port, username=None, password=None, no_id=False)

 
from datetime import datetime
now = datetime.now()

year = now.year

month = now.month

day = now.day

hour = now.hour

minute = now.minute

ourData.to_csv(f"sensor_data_{year}{month}{day}_{hour}{minute}.csv", sep=',', encoding='utf-8')

 