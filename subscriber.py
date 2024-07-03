import paho.mqtt.client as mqtt

# Callback function for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect, subscriptions will be renewed.
        client.subscribe("home/temperature")
    else:
        print(f"Connection failed with code {rc}")

# Callback function for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the Mosquitto broker
client.connect("localhost", 1883, 60)

# Start the loop to process network traffic, dispatch callbacks, and handle reconnecting.
client.loop_forever()

