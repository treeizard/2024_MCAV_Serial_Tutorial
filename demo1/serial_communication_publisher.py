import serial
import time

# Define the serial port and baud rate.

ser = serial.Serial('COM6', 9600)  # Adjust the port and baud rate according to your Arduino setup.

# Wait for the serial connection to be established.
time.sleep(2)

try:
    while True:
        # Read input from the user.
        data_to_send = input("Enter data to send to Arduino: ")

        # Send the data to Arduino.
        ser.write(data_to_send.encode())

        # Wait for a short time before sending the next data (optional).
        time.sleep(0.1)

        # Read the data that has been sent to Arduino
        line = ser.readline().decode().strip()
        line = line.replace("You sent me:", "")
        print("Arduino Received:", line)
except KeyboardInterrupt:
    # If Ctrl+C is pressed, close the serial connection.
    ser.close()