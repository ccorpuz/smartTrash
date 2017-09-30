import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json
import uuid

#pin initialization
coverPin = 15
TRIG = 5 
ECHO = 6

#GPIO initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(coverPin,GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Set the variables for connecting to the iot service
broker = ""
topic = "iot-2/evt/status/fmt/json"
username = "use-token-auth"
password = "Change this to your auth token" #auth-token
organization = "Change this to your organization id" #org_id
deviceType = "Change this to your device type"

topic = "iot-2/evt/status/fmt/json"
macAddress = "Change this to your device id" #deviceid
#Creating the client connection
#Set clientID and broker
clientID = "d:" + organization + ":" + deviceType + ":" + macAddress
broker = organization + ".messaging.internetofthings.ibmcloud.com"
mqttc = mqtt.Client(clientID)

if username is not "":
 mqttc.username_pw_set(username, password=password)

mqttc.connect(host=broker, port=1883, keepalive=60)


#Publishing to IBM Internet of Things Foundation
mqttc.loop_start()

#check ultrasonic sensor level
def check_ultra():
	print "Distance Measurement In Progress"
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)
	time.sleep(2)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
		
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	print "Distance:",distance,"cm"
	GPIO.cleanup()
	return distance

def check_lid():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(coverPin,GPIO.IN)
    openVal = GPIO.input(coverPin)
    return openVal
    
while mqttc.loop() == 0:

 msg = json.JSONEncoder().encode({"d":{"openVal":check_lid(),"distance":check_ultra()}})
 
 mqttc.publish(topic, payload=msg, qos=0, retain=False)
 print "Message sent"

 time.sleep(5)
 pass
