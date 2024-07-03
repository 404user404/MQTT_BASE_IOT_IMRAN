import paho.mqtt.client as mqtt

# broker = "localhost"
# port = 1883

# Callback function for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect, subscriptions will be renewed.
        client.subscribe("home/temperature")
        client.subscribe("home/humidity")
    else:
        print(f"Connection failed with code {rc}")

# Callback when message is received
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()
    print(f"Received message '{payload}' on topic '{topic}'")
    
    if topic == "home/temperature":
        process_temperature(float(payload))
    elif topic == "home/humidity":
        process_humidity(float(payload))

def process_temperature(temperature):
    # Example logic: control heater or cooler based on temperature
    if temperature > 25.0:
        print("Turning on the cooler...")
    elif temperature < 22.0:
        print("Turning on the heater...")
    else:
        print("Temperature is within range.")

def process_humidity(humidity):
    # Example logic: alert if humidity exceeds a threshold
    if humidity > 55.0:
        print("High humidity detected. Take action.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the Mosquitto broker
client.connect("localhost", 1883, 60)

# client.subscribe("home/temperature")
# client.subscribe("home/humidity")

client.loop_forever()
