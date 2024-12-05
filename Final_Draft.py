import machine
from machine import Pin, ADC
import utime

VRx = ADC(Pin(26))
VRy = ADC(Pin(27))
button = Pin(28,Pin.IN, Pin.PULL_UP)

from servo import Servo

servo_1 = Servo(0)
servo_2 = Servo(1)
servo_3 = Servo(2)

while True:
    xValue = VRx.read_u16()
    yValue = VRy.read_u16()
    buttonValue = button.value()
    print(str(xValue) + ", " + str(yValue) + "-- " + str(buttonValue))
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    servo_3.move(0)
    if xValue <= 600:
        xStatus = "left"
        servo_1.move(0)
    elif xValue >= 60000:
        xStatus = "right"
        servo_1.move(180)
    if yValue <= 600:
        yStatus = "up"
        servo_2.move(0)
    elif yValue >= 60000:
        yStatus = "down"
        servo_2.move(180)
    if buttonValue == 0:
        buttonStatus = "pressed"
        servo_3.move(180)
    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    utime.sleep(1)
    
