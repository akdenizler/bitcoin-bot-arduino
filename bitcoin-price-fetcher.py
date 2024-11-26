import requests 
import serial
import time 
import json

arduino_port = '/dev/cu.usbserial-110'
baud_rate = 9600

"""
Bitcoin price API endpoint
"""
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

"""
Connect to Arduino
"""
arduino = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # wait for Arduino to initialize

"""
Function to fetch Bitcoin price
""" 
def bitcoin_price_fetcher():
    try:
        data = requests.get(key)   
        data = data.json() 
        return float(data["price"])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None 
    
previous_price = bitcoin_price_fetcher()
if previous_price is None:
    print("Error fetching initial price. Shutting down...")
    arduino.close
    exit()

print(f"Initial Bitcoin price: ${previous_price}")

try:
    while True:
        current_price = bitcoin_price_fetcher()
        """
        In case of a price fetch failure
        """
        if current_price is None:
            print("Error fetching current price. Retrying...")
            time.sleep(10)
            continue

        print(f"current Bitcoin price${current_price}")

        """
        Output to Arduino to communicate price increase/decrese
        """
        if current_price > previous_price:
            print("Price up! Pinging Arduino...")
            arduino.write(b'u')

        elif current_price < previous_price:
            print("Price down! Pinging Arduino...")
            arduino.write(b'd')
        
        else:
            print("Price unchanged.")
        """
        Update initial price
        """
        previous_price = current_price
        time.sleep(10)  


except KeyboardInterrupt:
    print("Aborting process.")
    arduino.close()