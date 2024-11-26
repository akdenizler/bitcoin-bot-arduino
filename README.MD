Here’s the updated **README.md** without the Arduino sketch section, as the Arduino script is uploaded along with the Python script:

---

## **Bitcoin Price Monitor with Arduino**

### **Overview**
This project monitors the Bitcoin price in real-time using the Binance API and communicates with an Arduino to visually indicate the price movement. If the Bitcoin price goes up, one LED will light up; if the price goes down, another LED will light up. The LEDs are connected to the Arduino pins and react based on the price changes.

### **Requirements**
- **Hardware:**
  - Arduino Uno (or compatible board)
  - 2 LEDs (one for price increase, one for price decrease)
  - 2 resistors (220Ω recommended for each LED)
  - Jumper wires
  - USB cable to connect Arduino to the computer

- **Software:**
  - Python 3.x
  - Libraries: `requests`, `pyserial`
  - Arduino IDE
  - An active internet connection to fetch live Bitcoin prices via the Binance API.

### **Connections for Arduino:**
1. **LED 1 (Price Up)**
   - **Pin 11**: Anode (positive leg of the LED)
   - **Ground**: Cathode (negative leg through a 220Ω resistor)

2. **LED 2 (Price Down)**
   - **Pin 10**: Anode (positive leg of the LED)
   - **Ground**: Cathode (negative leg through a 220Ω resistor)

Ensure the **Arduino is powered** and connected via USB to your computer.

### **Python Script:**
The Python script fetches the current Bitcoin price from the Binance API and compares it with the previous price. If the price increases, it sends a signal to the Arduino to light up the first LED (Price Up). If the price decreases, it lights up the second LED (Price Down).

The script runs in a loop and updates the price every 10 seconds.

### **Installation Instructions:**

#### 1. **Install Python Dependencies:**
Make sure you have Python 3.x installed. Then, install the necessary Python libraries:
```bash
pip install requests pyserial
```

#### 2. **Configure Arduino and Python Scripts:**
- Upload the provided Arduino sketch to your board using the Arduino IDE. This sketch handles the communication with the Python script and controls the LEDs.
- In the Python script, edit the **arduino_port** variable to match the port of your Arduino device:
  - On **macOS/Linux**, it might look like `/dev/cu.usbserial-XXXX`.
  - On **Windows**, it might be `COM3` or similar.

#### 3. **Run the Python Script:**
Run the script to start monitoring Bitcoin prices:
```bash
python bitcoin_led_control.py
```

The script will continuously fetch the current Bitcoin price and send signals to the Arduino based on whether the price is going up, down, or remains unchanged.

### **Explanation of Python Script:**
1. **Bitcoin Price Fetching:**
   - The script uses the Binance API to fetch the current Bitcoin price (BTC/USDT).
   - The `bitcoin_price_fetcher()` function handles the API request and returns the price.

2. **Arduino Communication:**
   - The Python script sends a signal (`u` or `d`) to the Arduino via serial communication to indicate price changes.
   - Arduino lights up the corresponding LED based on the signal received.

3. **Continuous Monitoring:**
   - The script runs in an infinite loop, fetching the price every 10 seconds, and updates the LEDs accordingly.

### **Troubleshooting:**
- **LEDs not lighting up:** Ensure that the Arduino is correctly connected and the LEDs are wired to the correct pins (10 and 11).
- **Arduino not responding:** Double-check the port settings in the Python script (`arduino_port`).
- **Error in fetching Bitcoin price:** The script retries fetching the price if an error occurs. Ensure your computer is connected to the internet.

### **License:**
This project is open source. Feel free to use, modify, and distribute it.

---# bitcoin-bot-arduino
