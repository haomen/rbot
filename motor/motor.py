#!/usr/bin/env python

import RPIO

#use GPIO Pin 14,15,18,23 for motor control
#need 4 pins as gpio for pololu board.
#AENBL: Right Motor PWM        :GPIO15
#APHASE Right Motor Direction  :GPIO14
#BENBL: Left Motor PWM         :GPIO23
#BPHASE Left Motor Direction   :GPIO18

#here is rBot motor class
class rMotor:
#init to define all pins for motor control, these gpio pins have been tested
    def __init__(self):
        self.AENBL_Pin=14;
        self.APHASE_Pin=15;
        self.BENBL_Pin=18;
        self.BPHASE_Pin=23;
        print "GPIO pin defined!";
        print "AENBL_pin=GPIO"+str(self.AENBL_Pin)+"\n"+"AENBL_pin=GPIO"+str(self.APHASE_Pin);
        print "AENBL_pin=GPIO"+str(self.AENBL_Pin)+"\n"+"AENBL_pin=GPIO"+str(self.AENBL_Pin);
               
#initialize motor, set all 4pins output and start with 0,means direction fwd
    def initMotor(self):
        RPIO.setoutput(self.AENBL_PIN,RPIO.OUT,initial=RPIO.low);
        RPIO.setoutput(self.APHASE_PIN,RPIO.OUT,initial=RPIO.low);
        RPIO.setoutput(self.BENBL_PIN,RPIO.OUT,initial=RPIO.low);
        RPIO.setoutput(self.BPHASE_PIN,RPIO.OUT,initial=RPIO.low);
        
#set gpio for motor before start, set all 4pins are 0
    def setMotor(self,channel,speed):
        
    
        return self;

#adjust speed and direction, direction "F" or "B", speed from 1 to 10
    def spdControl(self,LD,LS,RD,RS): #LD= Left Direction, LS=Left Speed,same for RD, RS
        
        return self;


#driving control, for the vehicle, all command i want is turn degree and speed
    def vehContrl(self,heading,speed):#heading from -90 to 90, speed 1-10)
        
        return self;

#180 turn 0 turnning radius, left or right
    def turnAround(self,direction):
        
        return self;

motor1=rmotor();
motor
        
