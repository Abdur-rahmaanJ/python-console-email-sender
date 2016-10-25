

import smtplib
import time;
import random
import platform


from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

localtime = time.asctime( time.localtime(time.time()) )
n = random.randint(0, 10)

#response = raw_input("Please enter your name: ") 

print("\n")
print("Muballigh - a python command line e-mail sender (cles)")
print("Muballigh in Arabic means someone or something who / that conveys a transmission")
print("@Author ~ Abdur-Rahmaan Janhangeer with base help from naelshiab.com \n Code from Mauritius - abdurrahmaanjanhangeer.wordpress.com ")
print("___________________ OK, let's begin : but allow unsecure apps on your e-mail settings")
print("\n")

fromaddr = raw_input("Please enter your email: ")
toaddr = raw_input("Please enter the email you are sending to: ")

subj=raw_input("Please enter your subject: ")
ebody = raw_input("Please enter your body: ")
pswd = raw_input("Please enter your pwd: ")
print("\n")

print("mail smtp and port - common mails: ")
print("gmail ~ smtp: smtp.gmail.com and port: 587")
print("yahoo ~ smtp: smtp.mail.yahoo.com and port: 465")
print("others: google it")
print("\n")
mailsmtp = raw_input("Please enter your mail smtp: ")
smtpport = raw_input("Please enter your smtp port: ")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = """ " """+subj+""" " """+" as at "+localtime


msg.attach(MIMEText(ebody, 'plain'))

server = smtplib.SMTP(mailsmtp, smtpport)

server.starttls()
server.login(fromaddr, pswd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


x = 0
while (x < 3) :
    x+=1
    print(x)
print("mail sent to "+ toaddr+" by the grace of the almighty")
  #str(int)for int to string. you can use this to add to your mail
  #python /muballigh.py