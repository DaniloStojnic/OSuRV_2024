#!/usr/bin/env python3 

import serial
from time import sleep

try :
    ser = serial.Serial('/dev/serial0', 115200)
    prev_value = 0
    while True:
        
        data = ser.read(1)  # ucitava bajt
        value = data[0]
        if prev_value != value:
            #print(hex(value))
            if value & 0b00000010:
                print("Dugme A")
            
            if value & 0b00000100:
                print("Dugme B")
            
            if value & 0b00001000:
                print("Dugme Z")

            if value & 0b00010000:
                print("Dugme Start")

            if value & 0b00100000:
                print("Dugme Up")

            if value & 0b01000000:
                print("Dugme Down")
            
            if value & 0b10000000:
                print("Dugme Left")
                   
        prev_value = value

except Exception as e:
    print(f"ERROR: {e}")

