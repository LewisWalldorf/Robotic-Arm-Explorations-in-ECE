#Import machine commands, pin and ADC function, and time
import machine
from machine import Pin, ADC
import utime
 
#Variables establish connection to joystick
VRx = ADC(Pin(26))
VRy = ADC(Pin(27))
button = Pin(28,Pin.IN, Pin.PULL_UP)

#Accesses downloaded script containing servo controls
from servo import Servo

#Variables defining each servo and their coresponding GPIO Pin
servo_1 = Servo(0)
servo_2 = Servo(1)
servo_3 = Servo(2)

#Establishes an infinite loop 
while True:
    xValue = VRx.read_u16()        #Reads the 16-bit integer for joystick position on x-axis and store value to variable "xValue"
    yValue = VRy.read_u16()        #Reads the 16-bit integer for joystick position on y-axis and store value to variable "yValue"
    buttonValue = button.value()   #Stores button status
    print(str(xValue) + ", " + str(yValue) + "-- " + str(buttonValue))    #Prints string text of x and y postition of joystick and the status of the button
    xStatus = "middle"             #Set default status for x
    yStatus = "middle"             #Set default status for x
    buttonStatus = "not pressed"   #Set default status for button
    servo_3.move(0)                #Unpressed button position will be 0
    
    #Repeated if statments which determine angle of servos based on postition of joysitck
    
    if xValue <= 600:              #Sets the servo that controls the base rotation to 180 degrees and stores joystick direction as string value
        xStatus = "left"
        servo_1.move(180)
    elif xValue >= 60000:          #Sets the servo that controls the base rotation to 0 degrees and stores joystick direction as string value
        xStatus = "right"
        servo_1.move(0)
    if yValue <= 600:              #Sets the servo that controls the arm elevation to 180 degrees and stores joystick direction as string value
        yStatus = "up"
        servo_2.move(180)
    elif yValue >= 60000:          #Sets the servo that controls the arm elevation to 0 degrees and stores joystick direction as string value
        yStatus = "down"
        servo_2.move(0)
    if buttonValue == 0:           #Checks if the button is pressed and stores button status as string value
        buttonStatus = "pressed"
        servo_3.move(180)
    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)     #Prints the current state of the joystick based on read values
    utime.sleep(0.5)      #time before function is repeated
