#!/usr/bin/env python

import RPIO


#use pin 16/18 from GPIO

#need 4 pins as gpio for pololu board.

#AENBL: Right Motor PWM
#APHASE Right Motor Direction
#BENBL: Left Motor PWM
#BPHASE Left Motor Direction


#here is rBot motor class
class rMotor:

#initialize motor, ask for AENBL,APHASE,BENBL,BPHASE pin
    def initMotor(self,AENBL,APHASE,BENBL,BPHASE):
        self.AENBL=AENBL;
        self.APHASE=APHASE;
        self.BENBL=BENBL;
        self.BPHASE=BPHASE;
        
        return self;

#set gpio for motor before start, set all 4pins are 0
    def setMotor(self):

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


        
