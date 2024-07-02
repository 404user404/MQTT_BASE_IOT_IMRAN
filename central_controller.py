import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883

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

client = mqtt.Client("central-controller")
client.on_message = on_message
client.connect(broker, port)

client.subscribe("home/temperature")
client.subscribe("home/humidity")

client.loop_forever()
