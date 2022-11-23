import paho.mqtt.client as mqttclient
import time


def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("client is connected")
        global connected
        connected = True
    else:
        print("connection failed")    
 

connected = False
broker_address="eu1.cloud.thethings.network"
port = 1883
user ="ap-addiva-01@ttn"
password = "NNSXS.YCG3Y43HFVAAFXJ243XAKP55ZCWOBNA65KIPBOY.LW366SHGZUIDHLEF4GWJV5N7XOW6HFBKDTYYKJGXLFWVWLAEDCJQ"




clinet = mqttclient.Client()
clinet.username_pw_set(user,password=password)
clinet.on_connect = on_connect
clinet.connect(broker_address,port=port)
clinet.loop_start()

while connected != True:
    time.sleep(0.2)
clinet.publish("mqtt-password-key-1665404870267")
clinet.loop_stop()