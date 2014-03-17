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

#SPECIAL ATTENTION: In order to control 2 motor independently, different channels have to be applied for different motors.

#here is rBot motor class
class rMotor:
#init to define all pins for motor control, these gpio pins have been tested
    def __init__(self):
        self.AENBL_Pin=15;
        self.APHASE_Pin=14;
        self.BENBL_Pin=23;
        self.BPHASE_Pin=18;
        self.MODE_Pin=24;                                        #in PWM mode, MODE pin is high(1)
        self.A_CHANNEL=0;                                        #motor control channel A  
        self.B_CHANNEL=1;                                        #motor control channel B
        self.FWD=0;                                              #forward direction
        self.BWD=1;                                              #backward direction
        RPIO.setwarnings(False);                                 #disable warning..
        
        print "GPIO pin defined!";
        print "AENBL_pin=GPIO"+str(self.AENBL_Pin)+"\n"+"APHASE_pin=GPIO"+str(self.APHASE_Pin);
        print "BENBL_pin=GPIO"+str(self.BENBL_Pin)+"\n"+"BPHASE_pin=GPIO"+str(self.BPHASE_Pin);
               
#initialize motor, set all 4pins output and start with 0,means direction fwd
    def initMotor(self):
        RPIO.setup(self.MODE_Pin,RPIO.OUT,initial=RPIO.HIGH);    #select PWM Mode;
        PWM.setup();                                             #initialize channel 0 and 1 for motor A and B
        PWM.init_channel(self.A_CHANNEL);
        PWM.init_channel(self.B_CHANNEL);

        RPIO.setup(self.APHASE_Pin,RPIO.OUT,initial=RPIO.LOW);   #default A to fwd direction
        PWM.add_channel_pulse(self.A_CHANNEL,self.AENBL_Pin,0,0);#default A to channel 0 and speed 0

        RPIO.setup(self.BPHASE_Pin,RPIO.OUT,initial=RPIO.LOW);   #default B to fwd direction
        PWM.add_channel_pulse(self.B_CHANNEL,self.BENBL_Pin,0,0);#default B to channel 1 and speed 0
        
#set digital value for pwm, min 0,max 2000;
    def setMotor(self,channel,speed):
        if(channel=='A'):
            print "set channel A PWM to "+str(speed);
            PWM.add_channel_pulse(self.A_CHANNEL,self.AENBL_Pin,0,speed);
        if(channel=='B'):
            print "set channel B PWM to "+str(speed);
            PWM.add_channel_pulse(self.B_CHANNEL,self.BENBL_Pin,0,speed);

#set direction
    def setDirection(self,channel,direction):                    #direction 0:fwd, 1:bwd
        if(channel=='A'):
            print "set channel A direction to "+str(direction);
            RPIO.output(self.APHASE_Pin,direction);
        if(channel=='B'):
            print "set channel B direction to "+str(direction);
            RPIO.output(self.BPHASE_Pin,direction);

#stop motor
    def stopMotor(self,channel):
        if(channel=='A'):
            print "stop channel A"
            self.setDirection('A',0);
            PWM.add_channel_pulse(self.A_CHANNEL,self.AENBL_Pin,0,0);
#            PWM.clear_channel_gpio(0,self.AENBL_Pin)l;
        if(channel=='B'):
            print "stop channel B"
            self.setDirection('B',0);
            PWM.add_channel_pulse(self.B_CHANNEL,self.BENBL_Pin,0,0);


# #adjust speed and direction, direction "F" or "B", speed from 1 to 10
#     def spdControl(self,LD,LS,RD,RS): #LD= Left Direction, LS=Left Speed,same for RD, RS
        
#         return self;


# #driving control, for the vehicle, all command i want is turn degree and speed
#     def vehContrl(self,heading,speed):#heading from -90 to 90, speed 1-10)
        
#         return self;

# #180 turn 0 turnning radius, left or right
#     def turnAround(self,direction):
        
#         return self;


#this is the test case#
motor1=rMotor();
motor1.initMotor();
motor1.setDirection('A',motor1.FWD);
for i in range(0,20):
    print "fwd counting on "+str(i);
    motor1.setMotor('A',i*100);
    time.sleep(0.5);
print "stop servo"
motor1.stopMotor('A');
motor1.setDirection('A',motor1.BWD);
for i in range(1,20):
    print "bwd counting on "+str(i);
#    motor1.setMotor('A',0);
    motor1.setMotor('A',2000-i*100);
    time.sleep(0.5);
print "stop"
motor1.stopMotor('A');
motor1.setDirection('B',motor1.FWD);
for i in range(0,20):
    print "fwd counting on "+str(i);
    motor1.setMotor('B',i*100);
    time.sleep(0.5);
print "stop servo"
motor1.stopMotor('B');
motor1.setDirection('B',motor1.BWD);
for i in range(1,20):
    print "bwd counting on "+str(i);
#    motor1.setMotor('B',0);
    motor1.setMotor('B',2000-i*100);
    time.sleep(0.5);
print "stop"
motor1.stopMotor('B');
time.sleep(50);
