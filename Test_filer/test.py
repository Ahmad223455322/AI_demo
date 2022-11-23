import paho.mqtt.client as mqtt #import the client1
import time

import pymongo



client_1 = pymongo.MongoClient("mongodb://localhost:27017/")

min_databas = client_1["databas"]

collation = min_databas["room_stat"]


mylist = [
  { "_id": 1,  "address": "Highway 37","tempratur":"22","Luftfuktighet":60,"VHC":"bra","PIR":"True","CO2":"1","KWH":"134","Vattenförbrukning":"2"},
  { "_id": 2,  "address": "Lowstreet 27","tempratur":"11","Luftfuktighet":60,"VHC":"bra","PIR":"True","CO2":"1","KWH":"134","Vattenförbrukning":"10"},
  { "_id": 3,  "address": "Apple st 652","tempratur":"14","Luftfuktighet":60,"VHC":"bra","PIR":"False","CO2":"1","KWH":"155","Vattenförbrukning":"5"},
  { "_id": 4,  "address": "Mountain 21","tempratur":"11","Luftfuktighet":30,"VHC":"bra","PIR":"True","CO2":"1","KWH":"124","Vattenförbrukning":"5"},
  { "_id": 5,  "address": "Valley 345","tempratur":"25","Luftfuktighet":30,"VHC":"bra","PIR":"False","CO2":"1","KWH":"156","Vattenförbrukning":"22"},
  { "_id": 6,  "address": "Ocean blvd 2","tempratur":"20","Luftfuktighet":30,"VHC":"bra","PIR":"False","CO2":"1","KWH":"132","Vattenförbrukning":"7"},
  { "_id": 7,  "address": "Green Grass 1","tempratur":"23","Luftfuktighet":10,"VHC":"bra","PIR":"True","CO2":"1","KWH":"122","Vattenförbrukning":"44"},
  { "_id": 8,  "address": "Sky st 331","tempratur":"11","Luftfuktighet":10,"VHC":"bra","PIR":"False","CO2":"1","KWH":"112","Vattenförbrukning":"3"},
  { "_id": 9,  "address": "One way 98","tempratur":"13","Luftfuktighet":20,"VHC":"bra","PIR":"True","CO2":"1","KWH":"121","Vattenförbrukning":"6"},
  { "_id": 10, "address": "Yellow Garden 2","tempratur":"17","Luftfuktighet":20,"VHC":"bra","PIR":"False","CO2":"1","KWH":"433","Vattenförbrukning":"55"},
  { "_id": 11, "address": "Park Lane 38","tempratur":"18","Luftfuktighet":25,"VHC":"bra","PIR":"False","CO2":"1","KWH":"344","Vattenförbrukning":"7"},
  { "_id": 12, "address": "Central st 954","tempratur":"19","Luftfuktighet":25,"VHC":"bra","PIR":"True","CO2":"1","KWH":"132","Vattenförbrukning":"22"},
  { "_id": 13, "address": "Main Road 989","tempratur":"20","Luftfuktighet":15,"VHC":"bra","PIR":"True","CO2":"1","KWH":"111","Vattenförbrukning":"8"},
  { "_id": 14, "address": "Sideway 1633","tempratur":"21","Luftfuktighet":23,"VHC":"bra","PIR":"True","CO2":"1","KWH":"145","Vattenförbrukning":"3"}
]

############

def on_message(client, userdata, message):
    

    # print("message received " ,str(message.payload.decode("utf-8")))
    min_databas['databas']
    collation =  min_databas["room_stat"]
    mydata = {"Data från Sensorn":str(message.payload.decode("utf-8"))}
    collation.insert_one(mydata)
    print('Data saved!')


    # print("message topic=",message.topic)

    # print("message qos=",message.qos)

    # print("message retain flag=",message.retain)
  

########################################

broker_address="eu1.cloud.thethings.network"

#broker_address="iot.eclipse.org"



client = mqtt.Client("MQTT") #create new instance

client.on_message=on_message #attach function to callback



client.connect(broker_address) #connect to broker

client.loop_start() #start the loop



client.subscribe("#")

time.sleep(2) # wait

client.loop_stop() #stop the loop


# for x in collation.find():
#   print(x)























# import paho.mqtt.client as mqttclient
# import time


# connected = False
# messagerecieved = False

# def on_connect(client,userdata,flags,rc):
#     if rc == 0:
#         print("client is connected")
#         global connected
#         connected = True
#     else:
#         print("client is not connected")    




# def on_messag(client,userdata,message):
#     print("Message recived"+ str(message.payload))
#     print("Topic"+str(message.topic))
 


# broker_address="eu1.cloud.thethings.network"
# port = 1883
# user ="ap-addiva-01@ttn"
# password ="NNSXS.YCG3Y43HFVAAFXJ243XAKP55ZCWOBNA65KIPBOY.LW366SHGZUIDHLEF4GWJV5N7XOW6HFBKDTYYKJGXLFWVWLAEDCJQ"


# clinet = mqttclient.Client("mqtt-password-key-1665404901931")
# clinet.username_pw_set(user,password=password)
# clinet.on_connect = on_connect
# clinet.connect(broker_address,port=port)
# clinet.loop_start()
# clinet.subscribe("ap-addiva-01@ttn/devices/eui-a81758fffe075b66")

# while connected != True:
#     time.sleep(0.2)


# while messagerecieved != True:
#     time.sleep(0.2)

# clinet.loop_stop()      
