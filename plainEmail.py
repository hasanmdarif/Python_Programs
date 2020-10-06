# This code lets you to send an email through code via gmail.

import smtplib

sender_email = input("Please type your email and hit enter: ")
password = input("Please type your password and hit enter: ")
receiver_email = input("Please type the receivers' email and hit enter: ")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:       #587 is port
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)

    subject = "This is my first time at Hacktober fest"
    body = "Hi, I want to contribute to Open Source from today. It is already exciting!"
    msg = f'Subject: {subject}\n\n\n{body}'
    
    smtp.sendmail(sender_email, receiver_email, msg)