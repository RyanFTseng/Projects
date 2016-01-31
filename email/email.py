import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(youngwonks123@gmail.com,wonks123)
BODY='\r\n'.join(['TO:%S'%TO,
                  'From:%s'%,youngwonks123@gmail.com
                  'Subject:%s'%SUBJECT,
                  ",TEXT])
try:
    server.sendmail(gmail_sender,[TO],BODY)
    print('email sent')
except:
    print('error sending mail')
server.quit()
