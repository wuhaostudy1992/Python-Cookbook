import serial

ser = serial.Serial('Device name varies', baudrate=9600, bytesize=8, parity='N', stopbits=1)
