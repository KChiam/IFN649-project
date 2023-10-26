import serial
import paho.mqtt.client as mqtt

# MQTT parameters
ADD = "52.64.82.226"
PORT = 1883
publish_topic = "hotstick_temp"


# setup BT
ser = serial.Serial("/dev/rfcomm1", 9600)
ser.write(str.encode('Start\r\n'))

# MQTT connection and subscription setup
client = mqtt.Client()
client.connect(ADD, PORT, 60)
client.publish(publish_topic)


# Temp data - receive from Tier 1 via Bluetooth and sends to Tier 3 via MQTT publish
while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        print(cookedserial)
        client.publish(publish_topic, cookedserial)
        print("The postwoman did their job, successfully sent: {cookedserial}")


