import time
import random
import paho.mqtt.client as mqtt

# MQTT broker address and port
broker = "test.mosquitto.org"
port = 1883

# Create a client instance
client = mqtt.Client("temperature-sensor")

# Connect to broker
client.connect(broker, port)

while True:
    # Simulate temperature reading
    temperature = random.uniform(20.0, 30.0)
    
    # Publish temperature to MQTT topic
    client.publish("home/temperature", temperature)
    
    print(f"Temperature published: {temperature}")
    
    # Wait for some time before publishing next reading (e.g., every 5 seconds)
    time.sleep(5)

# Disconnect MQTT client
client.disconnect()
