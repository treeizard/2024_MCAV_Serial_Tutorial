void setup() {
  // This is the Baud Rate: The Baud rate represents the number of signal changes or symbols transmitted per second.   
  Serial.begin(9600);
}

void loop() {
  // Check if Serial is available
  if (Serial.available() > 0) {
    // If available Read Serial Data until the end of sentence
    String data = Serial.readStringUntil('\n');

    // Print the Data Read
    Serial.print("You sent me: ");
    Serial.println(data);
   
  }
}
