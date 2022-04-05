import imghdr
import smtplib
from email.message import EmailMessage

def send_email():
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("sender@gmail", "password")
        email = EmailMessage()
        email["From"] = "sender@gmail"
        email['To'] = "reciever@gmail"
        email["subject"] = "Alarm"
        email.set_content("A move was detected, Please be careful")
       
        with open("image.png", "rb") as image:
                image_data = image.read()
                image_type = imghdr.what(image.name)
                image_name = image.name
        email.add_attachment(image_data, maintype = "image", subtype = image_type, filename = image_name )

        server.send_message(email)
