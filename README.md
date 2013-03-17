DMSDoorLog
==========

This alerts people at Dallas Makerspace when the door is left open too long when it shouldn't be.

Required Hardware:
 - Arduino 
 - Door Strike w/ sensor (http://www.kawamall.com/pd_1x_strike38s.cfm)
 - Raspberry Pi or Linux PC

On the arduino:
 - Use the Debounce example in the arduino IDE and modify it to send data via 9600 baud serial
 - Send 1 if the door is open
 - Send 0 if the door is closed


The e-mail function was taken from: http://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector/overview
