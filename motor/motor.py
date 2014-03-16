#!/usr/bin/env python

import RPIO
import time
from RPIO import PWM

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
        self.servo=PWM.Servo();#default PWM subcycle is 20ms and increment is 10us
        RPIO.setup(self.AENBL_Pin,RPIO.OUT,initial=RPIO.LOW);
        self.servo.set_servo(self.APHASE_Pin,0);
        RPIO.setup(self.BENBL_Pin,RPIO.OUT,initial=RPIO.LOW);
        self.servo.set_servo(self.BPHASE_Pin,0);
        
#set digital value for pwm, min 0,max 20000;
    def setMotor(self,channel,speed):
        if(channel=='A'):
            self.servo.set_servo(self.APHASE_Pin,speed);
        if(channel=='B'):
            self.servo.set_servo(self.BPHASE_Pin,speed);
#set direction
    def setDirection(self,channel,direction):#direction 0:fwd, 1:bwd
        if(channel=='A'):
            RPIO.output(self.AENBL_Pin,direction);
        if(channel=='B'):
            RPIO.output(self.BENBL_Pin,direction);

#stop motor
    def stopMotor(self,channel):
        if(channel=='A'):
            self.servo.stop_servo(self.APHASE_Pin);
        if(channel=='B'):
            self.servo.stop_servo(self.BPHASE_Pin);

#adjust speed and direction, direction "F" or "B", speed from 1 to 10
    def spdControl(self,LD,LS,RD,RS): #LD= Left Direction, LS=Left Speed,same for RD, RS
        
        return self;


#driving control, for the vehicle, all command i want is turn degree and speed
    def vehContrl(self,heading,speed):#heading from -90 to 90, speed 1-10)
        
        return self;

#180 turn 0 turnning radius, left or right
    def turnAround(self,direction):
        
        return self;


#this is the test case#
motor1=rMotor();
motor1.initMotor();
motor1.setDirection('B',1);
for i in range(0,20):
    print "fwd counting on "+str(i);
#    motor1.setMotor('A',0);
    motor1.setMotor('B',i*1000);

    time.sleep(1);
print "stop servo"
motor1.stopMotor('B');
motor1.setDirection('B',0);
for i in range(0,20):
    print "bwd counting on "+str(i);
#    motor1.setMotor('A',0);
    motor1.setMotor('B',i*1000);
    time.sleep(1);
print "stop"
motor1.stopMotor('B');
