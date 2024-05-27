
from dotenv import load_dotenv, find_dotenv
import os
import serial
import time
from pymongo import MongoClient
from datetime import datetime
load_dotenv(find_dotenv())

connection_string = f"mongodb+srv://thangdo190702:Ancutbokho01@mongodbjourney.k1hpt6g.mongodb.net/retryWrites=true&w=majority&appName=MongoDBjourney"
client = MongoClient(connection_string)
password = os.environ.get("MONGODB_PWD")

db = client['sensors']
sensor_collection = db["sensor_data"]

arduino = serial.Serial("COM6", 9600)

while True:
    arduino_data = arduino.readline().decode('utf-8', errors='replace').strip()
    temperature, humidity, irStatus = arduino_data.split(', ')
    temperature = float(temperature.split(': ')[1].split("°")[0])
    humidity = float(humidity.split(': ')[1].split("%")[0])
    irStatus = irStatus.split(': ')[1]

    dht11_data = {
        'timestamp': datetime.now(),
        'temperature': temperature,
        'humidity': humidity
    }
    sensor_collection.insert_one(dht11_data)

    ir_status_data = {
        'timestamp': datetime.now(),
        'status': irStatus
    }
    sensor_collection.ir_status.insert_one(ir_status_data)

    print(f'Saved data: Temperature {temperature}°C, Humidity {humidity}%, LED status: {irStatus}')
    time.sleep(5)

