# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
"""
https://myaccount.google.com/lesssecureappsS
"""

mesaj = MIMEMultipart()  # Mail yapımızı oluşturuyoruz.

mesaj["From"] =  "your mail adress" # Kimden 

mesaj["To"] = "the one you want to send an email" # Kime 

mesaj["Subject"] = "Mail Subject"  # Konusu


# İçeriği
yazi = """

Hello, Im sending this with Python    


"""  


message_body =  MIMEText(yazi,"plain")  # Mailimin gövdesi bu sınıfla

mesaj.attach(message_body) # Mailimizin gövdesini mail yapıma ekledim



try:
    mail =  smtplib.SMTP("smtp.gmail.com",587)  # SMTP objemizi oluşturdum ve gmail smtp server'ına bağlandım.

    mail.ehlo() # SMTP serverına kendimi tanıttım.
 
    mail.starttls() # Adresimin ve Parolamın şifrelenmesi için gerekli

    mail.login("gmail_address","gmail_password") # SMTP server'ına giriş yapıyoruz. Kendi mail adresim ve parolam

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())  # Mailimizi gönderiyoruz.
    print("Mail has sent successfuly....")
    mail.close()  #For disconnect to Smtp server

except:
    sys.stderr.write("Mail göndermesi başarısız oldu...") # If there is a connection problem.
    sys.stderr.flush()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    