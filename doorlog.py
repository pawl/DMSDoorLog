import serial
import datetime
import smtplib
from subprocess import call

doorCount = 0


TO = 'to@email.com'
GMAIL_USER = 'your@email.com'
GMAIL_PASS = 'secret'

SUBJECT = 'Door Open Alert'
TEXT = 'The front door has been open for longer than 30 minutes after midnight and before 10AM.'

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
        if message:
                if message[0] == '0':
                        doorCount = 0
                if message[0] == '1':
                        doorCount += 1
        else:
                print ("Disconnected")
        if (doorCount == 600) or (doorCount == 1200) or (doorCount == 1800) or (doorCount == 2400) or (doorCount == 3000):
                d = datetime.datetime.now()
                if d.hour in range(0, 10):
                        call(["mplayer", "shutdoor.mp3"])
        elif doorCount > 3600:
                send_email()
                doorCount = 0
