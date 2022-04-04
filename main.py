import smtplib
from email.message import EmailMessage



def send_email():


        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("testing.email.1van4o@gmail.com", "edno2345678")
        email = EmailMessage()
        email["From"] = "testing.email.1van4o@gmail.com"
        email['To'] = "ivan2007ny@gmail.com"
        email["subject"] = "Alarm"
        email.set_content("moving shit detected")
        server.send_message(email)
