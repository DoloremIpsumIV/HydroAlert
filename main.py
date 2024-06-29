import network
import urequests as requests
import keys
from time import sleep
import dht
import machine

# Constants
DEVICE_LABEL = "name for your device" 
VARIABLE_LABEL = "variable name that you choose in Ubidots"  
DELAY = 1800  # Delay in seconds (30 minutes)

# Initialize sensors and actuators
tempSensor = dht.DHT11(machine.Pin(27))  # Initialize DHT11 sensor on GPIO 27
led = machine.Pin(0, machine.Pin.OUT)  # Initialize LED on GPIO 0

# Function to connect to WiFi
def connect():
    wlan = network.WLAN(network.STA_IF)  # Set modem to station mode
    if not wlan.isconnected():  # Check if already connected
        print('Connecting to network...')
        wlan.active(True)  # Activate network interface
        wlan.config(pm=0xa11140)  # Disable WiFi power-saving mode
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Connect using WiFi credentials
        print('Waiting for connection...', end='')
        while not wlan.isconnected() and wlan.status() >= 0:  # Wait until connected
            print('.', end='')
            sleep(1)
    ip = wlan.ifconfig()[0]  # Get IP address
    print('\nConnected on {}'.format(ip))
    return ip

# Function to build JSON payload
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except Exception as e:
        print("Error building JSON:", e)
        return None

# Function to send data to Ubidots
def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/api/v1.6/devices/" + device
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            print("No data to send")
    except Exception as e:
        print("Error sending data:", e)

# Function to flash the LED
def flash_led(times, duration):
    for _ in range(times):
        led.on()
        sleep(duration)
        led.off()
        sleep(duration)

# Main script execution
if __name__ == "__main__":
    connect()  # Connect to the WiFi

    while True:
        try:
            tempSensor.measure()  # Measure temperature and humidity
            temperature = tempSensor.temperature()  # Get temperature
            humidity = tempSensor.humidity()  # Get humidity
            print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
            
            # Send temperature data to Ubidots
            returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL, temperature)
            
            # Flash LED if temperature is 25°C or higher
            if temperature >= 25:
                flash_led(5, 0.5)  # Flash LED 5 times with 0.5 second duration

            sleep(DELAY)  # Wait for the next measurement cycle
        except Exception as error:
            print("Exception occurred:", error)
            sleep(2)  # Short delay before retrying
