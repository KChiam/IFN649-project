import serial
import paho.mqtt.client as mqtt

# MQTT parameters
ADD = "52.64.82.226"
PORT = 1883
subscribe_topic = "hotstick_command"


# setup BT
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))


def on_message(client, userdata, message):
    received_message = str(message.payload.decode("utf-8"))
    print(received_message)
    ser = serial.Serial("/dev/rfcomm0",9600)
    ser.write(message.payload)

# MQTT connection and subscription setup
client = mqtt.Client()
client.connect(ADD, PORT, 60)
client.on_message= on_message
client.subscribe(subscribe_topic)

