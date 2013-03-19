import serial
import datetime
import smtplib
from subprocess import call

doorCount = 0


TO = 'their@email.com'
GMAIL_USER = 'your@email.com'
GMAIL_PASS = 'secret'

SUBJECT = 'Door Open Alert'
TEXT = 'The front door has been open for longer than 30 minutes after midnight and before 10AM.'

# change '/dev/ttyACM0' to the port your arduino is on
ser=serial.Serial('/dev/ttyACM0', 9600, timeout=20)

def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

while True:
    message = ser.read()
    # count how long the door is open
    # else - give an error when nothing is read from serial
    if message:
            # 0 = door closed
            if message[0] == '0':
                    doorCount = 0
            # 1 = door open
            if message[0] == '1':
                    doorCount += 1
    else:
        print ("Disconnected")

    #trigger the email if > 30 minutes
    if doorCount > 3600:
            d = datetime.datetime.now()
            if d.hour in range(0,10):
                    send_email()
                    doorCount = 0
    #sound alarm at 5,10,15,20,25 minutes
    #600 * polled ever .5 seconds = 5 minutes
    elif (doorCount > 0) and ((doorCount % 600) == 0):
                d = datetime.datetime.now()
                if d.hour in range(0, 10):
                        call(["mplayer", "shutdoor.mp3"])

