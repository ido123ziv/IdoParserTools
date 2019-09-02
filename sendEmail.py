import smtplib
import ssl
from datetime import *
from message import Message

port = 465
password = "password"

context = ssl.create_default_context()
sender_email = "sender@gmail.com"
receiver_email = "reciever@comm-it.com"

def sendMessage(message):
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender_email,password)
        s = "\r\n".join(["From: sender@gmail.com",
                  	 "To: reciever@comm-it.com",
                         f"Subject: {message.subject}",
                         "",
                         message.msg])
        server.sendmail(sender_email,receiver_email,s)
