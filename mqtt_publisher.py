import paho.mqtt.client as mqtt
import random
import time

# Define the MQTT client
client = mqtt.Client()

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}\n")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the Mosquitto broker
client.connect("localhost", 1883, 60)

# Start the loop
client.loop_start()

temperature_topic = "home/temperature"
humidity_topic = "home/humidity"

# Publish messages
try:

    while True:
        # Simulate temperature reading
        temperature = random.uniform(20.0, 30.0)
        humidity = round(random.uniform(30.0, 60.0), 4)
        
        # Publish temperature to MQTT topic
        client.publish(temperature_topic, temperature)
        print(f"Temperature published: {temperature}")

        # Publish humidity to MQTT topic
        client.publish(humidity_topic, temperature)
        print(f"Humidity published: {temperature}")
        
        # Wait for some time before publishing next reading (e.g., every 5 seconds)
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
