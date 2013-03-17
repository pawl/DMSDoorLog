import serial
import datetime
import smtplib

doorCount = 0


TO = 'email@here.com'
GMAIL_USER = 'email@here.com'
GMAIL_PASS = 'secret'

SUBJECT = 'Door Open Alert'
TEXT = 'The front door has been open for longer than 15 minutes after midnight and before 10AM.'

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
        if doorCount > 1800:
                d = datetime.datetime.now()
                if d.hour in range(0, 10):
                        send_email()
                doorCount = 0
