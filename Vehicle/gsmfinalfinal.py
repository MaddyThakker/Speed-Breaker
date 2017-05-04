import serial
import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BOARD)

with open('output.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT'+'\r')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGF=1'+'\r')  # Select Message format as Text mode
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGS="+91XXXXXXXXXX"'+'\r') # any country code
rcv = port.read(10)
print rcv
time.sleep(1)

port.write(data+'\r')  # Message
rcv = port.read(10)
print rcv

port.write("\x1A") # Enable to send SMS
for i in range(10):
    rcv = port.read(10)
    print rcv
