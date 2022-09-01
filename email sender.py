from email.message import EmailMessage

"""This app2 module is not standard module, it's a custom module created by the owner. You will not find it if you search in Google
you can delete this module from this code  and for the exchange you type your password that you get from Google Account>Security>App passwords in email password"""
from app2 import password
import ssl
import smtplib


#fill your email in email_sender
email_sender = 'codewithtomi@gmail.com'
"""you can type your password here with double quota/apostrophe that you got from your Google Account>Security>App passwords
if you didn't use module app2"""
email_password = password
#fill your target email in email_receiver
email_receiver = ''

#your email subject goes here
subject = "Dont forget to subscribe"

#your email message goes here
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
