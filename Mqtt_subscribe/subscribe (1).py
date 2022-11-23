import time
import paho.mqtt.subscribe as subscribe
import json
import pymongo
from datetime import datetime


client_databas = pymongo.MongoClient("mongodb://localhost:27017/")

min_databas = client_databas["DBsensor_data"]

collation = min_databas["room_data"]
mylist=[]


def subscribe_func():

    while True:
        tid_nu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        m = subscribe.simple(topics="#", hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"ap-addiva-01@ttn",'password':"NNSXS.YCG3Y43HFVAAFXJ243XAKP55ZCWOBNA65KIPBOY.LW366SHGZUIDHLEF4GWJV5N7XOW6HFBKDTYYKJGXLFWVWLAEDCJQ"}, msg_count=2)
        for a in m:
            data_from_sensor =a.payload.decode("utf-8")
            data_to_dict =  json.loads(data_from_sensor)

        div_id = data_to_dict["end_device_ids"]["device_id"]
        rums_data = data_to_dict["uplink_message"]["decoded_payload"]
        data_to_insert_to_databas = {"Sensor_ID":div_id, "data":rums_data,"Tid":tid_nu}
        collation.insert_one(data_to_insert_to_databas)
        time.sleep(0)
        
        for data in collation.find():
            print(data)
