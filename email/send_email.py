import smtplib

gmail_sender='youngwonks123@gmail.com'
gmail_passwd='wonks123'
TO='rtseng99@yahoo.com'
SUBJECT='Hello'
TEXT='Hi'

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(gmail_sender,gmail_passwd)
BODY='\r\n'.join(['TO:%s'%TO,
                  'From:%s'%gmail_sender,
                  'Subject:%s'%SUBJECT,
                  '',TEXT])
try:
    server.sendmail(gmail_sender,[TO],BODY)
    print('email sent')
except:
    print('error sending mail')
server.quit()
