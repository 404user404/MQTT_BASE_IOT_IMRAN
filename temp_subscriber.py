import paho.mqtt.client as mqtt

# MQTT broker address and port
broker = "test.mosquitto.org"
port = 1883

# Callback when a message is received from MQTT broker
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# Create a client instance
client = mqtt.Client("temperature-display")

# Assign callback function when a message is received
client.on_message = on_message

# Connect to broker
client.connect(broker, port)

# Subscribe to MQTT topic
client.subscribe("home/temperature")

# Loop to maintain network connection and process incoming messages
client.loop_forever()
