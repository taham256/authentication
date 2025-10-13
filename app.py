import smtplib
import os
import random
import time

otp_store = {}
class Login_System:
    def __init__(self):
        self.official_email = os.getenv('OFFICIAL_EMAIL')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        if not  self.official_email or not self.smtp_password:
            raise ValueError("oops! missing email or password in environment variable")
    def sign_in(self,user_name,user_email):
        self.otp = random.randint(1000,9999)
        otp_store[user_email] = {"otp":self.otp,
                                 "time":time.time()}
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
             server.starttls()
             server.login(self.official_email, self.smtp_password)
             server.sendmail(self.official_email, user_email,
                            f"Subject:for login\n\nHI {user_name} your OTP is {self.otp}."
                            f"Please keep it secret🤫.")
             server.quit()
             return True
        except Exception as e:
             print(f"Error: {e}")
             return False
    def enter_otp(self,user_email,given_otp):
        otp_data = otp_store.get(user_email)
        current_time = time.time()
        expire_time = current_time - otp_data["time"]
        if given_otp == otp_data["otp"] and expire_time < 300 :
            print("Verified")
        elif expire_time > 300:
            print("OTP has expired")
        else:
            print("oops! wrong otp, try again")



ls = Login_System()
ls.sign_in("taham","taham216@proton.me")
