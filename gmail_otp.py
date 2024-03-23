import sys
import os, random
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QIcon

import smtplib
from email.mime.text import MIMEText

class OTPWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("otp_gui.ui", self)
        
        self.setWindowTitle("Eduhub")
        
        # Setting window icon
        app_icon = QIcon("icon\Edu_logo-removebg-preview.png")  # Replace "your_icon.png" with the path to your icon file
        self.setWindowIcon(app_icon)
        
        global otp_new
        otp_new = None
        
        
        self.messagebox = QMessageBox()
        self.resend_otp = self.pushButton_2
        self.resend_otp.clicked.connect(self.resendOTP)

        self.submit = self.pushButton
        self.submit.clicked.connect(self.submit_clicked)
        
        

        global otp
        otp = os.environ.get('OTP_ENTRY')
        global email
        email = os.environ.get('EMAIL_ENTRY')
        global name
        name = os.environ.get('NAME_ENTRY')

    def submit_clicked(self):
        otp_entry = self.lineEdit.text()
        if len(otp_entry) == 0:
            self.messagebox.setText("Enter OTP Field!")
            self.messagebox.setWindowTitle("Error")
            self.messagebox.exec()
        elif otp_entry == otp:
            print(f"Entered OTP: {otp_entry}")
            self.messagebox.setText("OTP Confirmed!")
            self.messagebox.setWindowTitle("Success")
            self.messagebox.exec()
            sys.exit()
        elif otp_entry == otp_new:
            print(f"Resended OTP: {otp_entry}")
            self.messagebox.setText("OTP Confirmed!")
            self.messagebox.setWindowTitle("Success")
            self.messagebox.exec()
            os.environ['OTP_ENTRY_DATA'] = otp_entry          
            
            sys.exit()
            
        
             
            
        else:
            self.messagebox.setText("OTP Incorrect!")
            self.messagebox.setWindowTitle("Error")
            self.messagebox.exec()

    def resendOTP(self):
        global otp_new
        otp_new = str(random.randint(1000, 9999))
        print("Generated OTP:", otp_new)
        os.environ['OTP_NEW'] = otp_new
        subject = 'Eduhub: Your One-Time Password (OTP) Verification Code'
        body = f"Dear {name},\n\n" \
               "You are receiving this email because you have requested to verify your identity or perform a specific action on our platform. Please use the following One-Time Password (OTP) to complete the verification process:\n\n" \
               f"Your OTP: {otp_new}\n\n" \
               "Please enter this OTP on the verification page to proceed. Please note that this OTP is valid for a limited time.\n\n" \
               "Thank you for using Eduhub!"
        self.sender_admin = 'Eduhub9702@gmail.com'
        self.recipents = [self.sender_admin , email]
        self.passkey = 'egpb lxuk duqt cxee'

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_admin
        msg['To'] = ', '.join(self.recipents)
           
        with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp_server:
            smtp_server.login(self.sender_admin, self.passkey)
            smtp_server.sendmail(self.sender_admin, self.recipents, msg.as_string())
            self.messagebox.setText("OTP Sent!")
            self.messagebox.setWindowTitle("Success")
            self.messagebox.exec()
            print("Email sent with OTP")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OTPWindow()
    window.show()
    sys.exit(app.exec())
