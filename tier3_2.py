from paho.mqtt import client 

print("Starting Application")

broker = "localhost"
port = 1883

# Function to ensure connection established
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    mqtt_client.subscribe(subscribe_topic)
    mqtt_client.publish(publish_topic)
    print("Subscribed to topic: ", subscribe_topic, "; Will publish to topic: ", publish_topic)


# Templogic based on string received
def on_message(client, userdata, message):
    received_message = str(message.payload.decode("utf-8"))
    print(received_message)
    global notsafe_count, safe_count, publish_topic

    if received_message >= 67 and notsafe_count == 0:
        command = 'notsafe'
        notsafe_count += 1
        safe_count = 0
        client.publish(publish_topic, command)
        print(command)

    elif received_message < 67 and safe_count == 0:
        command = 'safe'
        safe_count += 1
        notsafe_count = 0
        client.publish(publish_topic, command)
        print(command)

    else:
        if received_message >= 67:
            notsafe_count += 1
        else:
            safe_count += 1
    
    print("Done")


mqtt_client = client.Client("my_client")
mqtt_client.connect = on_connect
mqtt_client.on_message = on_message

notsafe_count = 0
safe_count = 0
subscribe_topic = "hotstick_temperature"
publish_topic = "hotstick_command"
mqtt_client.loop_forever()