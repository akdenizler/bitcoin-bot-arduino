void setup() {
  // Initialize the LED pins as outputs
  pinMode(9, OUTPUT);  // LED 1 for price up
  pinMode(10, OUTPUT); // LED 2 for price down

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if data is available on the serial port
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command from the serial port

    if (command == 'u') {         // If the command is 'u', price went UP
      digitalWrite(11, HIGH);      // Turn on LED 1
      digitalWrite(10, LOW);      // Turn off LED 2
    } else if (command == 'd') {  // If the command is 'd', price went DOWN
      digitalWrite(11, LOW);       // Turn off LED 1
      digitalWrite(10, HIGH);     // Turn on LED 2
    } else {
      // If an unknown command, turn off both LEDs
      digitalWrite(11, LOW);
      digitalWrite(10, LOW);
    }
  }
}
