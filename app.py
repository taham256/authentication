import smtplib
import os
import bcrypt

class Login_System:
    def __init__(self):
        self.official_email = os.getenv('OFFICIAL_EMAIL')
        self.smtp_password = os.getenv('OFFICIAL_PASSWORD')

    def send_email(self,reciver_email,subject,message):
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(self.official_email,self.smtp_password)
            server.sendmail(self.official_email,reciver_email,
                            f"Subject: {subject}\n\n{message}")
            server.quit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def login(self,user_name,email,password):
            pass
