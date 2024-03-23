import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QApplication, QStackedWidget, QMessageBox, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication, QIcon
import sqlite3
import bcrypt
import subprocess
import re
import smtplib
from email.mime.text import MIMEText

conn = sqlite3.connect("eduhub.db")
cursor = conn.cursor()
cursor.execute("""Create  table if not exists Users (
                pid INT  NOT NULL,
                email TEXT NOT NULL ,
                username TEXT NOT NULL,
                branch TEXT NOT NULL,
                gender TEXT NOT NULL,            
                password TEXT NOT NULL,
                active BOOL  NOT NULL DEFAULT False,
                PRIMARY KEY (pid,email))""")
conn.close()

class Signup_page(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("signuppage.ui",self)        
        self.signup_button.clicked.connect(self.signupfunction)
        self.messagebox=QMessageBox()
        
        
        global otp
        otp = None
        
        

    def signupfunction(self):
        try:
            import os
            pid = self.pid_entry_2.text()
            
            pid_entry_data = pid
            os.environ['PID_ENTRY_DATA'] =pid_entry_data
            
            email = self.email_entry_2.text()
            name = self.name_entry_2.text()
            gender = self.gender_entry_2.currentText()
            branch = self.branch_entry_2.currentText()
            password = self.password_entry_2.text()
            confirm_password = self.confirm_password_entry_2.text()
            
            
            os.environ['EMAIL_ENTRY'] =email
            os.environ['NAME_ENTRY'] =name
            
            import random
            
            
            
            print(pid)
            if len(email)==0 and len(password)==0 and  len(pid)==0 and len(name)==0:
                self.password_error_message_2.setText("Please enter the password.")
                self.email_error_message_2.setText("Please enter your email Id.")
                self.pid_error_message_2.setText("Please enter your pid.")
                self.name_error_message_2.setText("Please enter your name.")
                return
            
            if len(name)==0:
                self.name_error_message_2.setText("Please enter your name.")
                return
                
            if password != confirm_password:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.password_error_message_2.setText("Password do not match.")
                return
                
            if len(email) == 0 and len(password)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.password_error_message_2.setText("Please enter the password.")
                self.email_error_message_2.setText("Please enter your email Id.")
                return
                
            if  len(email) == 0 and len(pid)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.pid_error_message_2.setText("Please enter pid.")
                self.email_error_message_2.setText("Please enter your email Id.")
                return
                
            if  len(password) == 0 and len(pid)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.password_error_message_2.setText("Please enter password.")
                self.email_error_message_2.setText("Please enter your email Id.")
                return
                
            if len(password)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.password_error_message_2.setText("Please enter the password.")
                return
            
            if len(name)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.name_error_message_2.setText("Please enter your name.")
                return
                
            if len(email)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.email_error_message_2.setText("Please enter your email id.")
                return
                
            if len(pid)==0:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.pid_error_message_2.setText("Please enter your pid.")
                return
            
            
            if '@student.sfit.ac.in' not in email:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.email_error_message_2.setText("Invalid Email format")
                return
                
            if  len(password) < 8:
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("")
                self.password_error_message_2.setText("Password:Atleast 8 characters.")
                return
            
            if not (re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?]', password) and re.search(r'\d', password)):
                self.email_error_message_2.setText("")
                self.name_error_message_2.setText("")
                self.pid_error_message_2.setText("")
                self.password_error_message_2.setText("Password: At least one special character and one numerical value.")
                return
            
            self.email_error_message_2.setText("")
            self.name_error_message_2.setText("")
            self.pid_error_message_2.setText("")
            self.password_error_message_2.setText("")
            
            
            active=True
            conn = sqlite3.connect("eduhub.db")
            cursor = conn.cursor()
            
            if (name != '' and password !=  ''  and confirm_password != '' and pid != '' and email != '' and branch != '' and gender != ''):
                cursor.execute('SELECT pid, email FROM Users WHERE pid=? OR email=?', (pid, email))
            data=cursor.fetchone()
            
            

            def send_email(self):
                global otp
                otp = str(random.randint(1000, 9999))
                print("Generated OTP:", otp)
                
                self.subject = 'Eduhub: Your One-Time Password (OTP) Verification Code'
                self.body = f"Dear {name},\n\n" \
                            "You are receiving this email because you have requested to verify your identity or perform a specific action on our platform. Please use the following One-Time Password (OTP) to complete the verification process:\n\n" \
                            f"Your OTP: {otp}\n\n" \
                            "Please enter this OTP on the verification page to proceed. Please note that this OTP is valid for a single use and will expire after a short period of time for security reasons.\n\n" \
                            "If you did not request this OTP or have any concerns regarding your account security, please contact our support team immediately.\n\n" \
                            "Thank you for using our service.\n\n" \
                            f"Best regards,\nEdu-Hub"
                self.sender_admin = 'Eduhub9702@gmail.com'
                self.recipents = [self.sender_admin , email]
                self.passkey = 'egpb lxuk duqt cxee'
                
                msg = MIMEText(self.body)
                msg['Subject'] = self.subject
                msg['From'] = self.sender_admin
                msg['To'] = ', '.join(self.recipents)
                
                with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp_server:
                    smtp_server.login(self.sender_admin, self.passkey)
                    smtp_server.sendmail(self.sender_admin, self.recipents, msg.as_string())
                print("Mail sent")
                
                
                
            
            
            try:
                if data is not None:  # Check if data exists
                    self.messagebox.setText("User already exists!")
                    self.messagebox.setWindowTitle("Error")
                    self.messagebox.exec()
                elif password != confirm_password:
                    self.messagebox.setText("Passwords do not match!")
                    self.messagebox.setWindowTitle("Error!")
                    self.messagebox.exec()
                else:
                    send_email(self)
                    os.environ['OTP_ENTRY'] = otp
                    
                    self.messagebox.setText("OTP sent!")
                    self.messagebox.setWindowTitle("Success")
                    self.messagebox.exec()
                    process = subprocess.Popen(["python", "gmail_otp.py"])
                    process.wait()
                    otp_new=os.environ.get('OTP_NEW')
                    otp_entry=os.environ.get('OTP_ENTRY_DATA')
                    if otp_entry == otp:
                        print(f"Entered OTP: {otp_entry}")
                        self.messagebox.setText("OTP Confirmed!")
                        self.messagebox.setWindowTitle("Success")
                        self.messagebox.exec()
                        # Encode and hash the password
                        encoded_password = password.encode('utf-8')
                        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

                        # Assuming `pid`, `email`, `name`, `branch`, `gender`, and `active` are defined somewhere
                        cursor.execute('INSERT INTO Users VALUES(?,?,?,?,?,?,?)', [pid, email, name, branch, gender, hashed_password, active])
                        conn.commit()
                        conn.close()

                        self.messagebox.setText("Logged in Successfully!")
                        self.messagebox.setWindowTitle("Success")
                        self.messagebox.exec()
                        
                        
                        #getting to Homepage
                        self.close()
                        # Run main.py to start the homepage
                        subprocess.Popen(["python", "main.py"])
                        sys.exit()
                    elif otp_entry == otp_new:
                        print(f"Resended OTP: {otp_entry}")
                        """self.messagebox.setText("OTP Confirmed!")
                        self.messagebox.setWindowTitle("Success")
                        self.messagebox.exec()"""
                        # Encode and hash the password
                        encoded_password = password.encode('utf-8')
                        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

                        # Assuming `pid`, `email`, `name`, `branch`, `gender`, and `active` are defined somewhere
                        cursor.execute('INSERT INTO Users VALUES(?,?,?,?,?,?,?)', [pid, email, name, branch, gender, hashed_password, active])
                        conn.commit()
                        conn.close()

                        self.messagebox.setText("Logged in Successfully!")
                        self.messagebox.setWindowTitle("Success")
                        self.messagebox.exec()
                        
                        
                        #getting to Homepage
                        self.close()
                        # Run main.py to start the homepage
                        subprocess.Popen(["python", "main.py"])
                        sys.exit()
                        
                    else:
                        self.messagebox.setText("OTP Incorrect!")
                        self.messagebox.setWindowTitle("Error")
                        self.messagebox.exec()
                    
                    
            except Exception as e:
                print(f"Error in signupfunction: {e}")

        except Exception as e:
            print(f"Error in SIgnupfunction: {e}")
    

class Loginpage(QDialog):
    def __init__(self):
        super(Loginpage, self).__init__()
        loadUi("loginpage.ui",self)
        
        
        self.login.clicked.connect(self.loginfunction)
        self.messagebox=QMessageBox()
        self.new_sign_in.clicked.connect(self.gotosignup)
        

        
        
    
        
        
    
    def gotosignup(self):
        signup = Signup_page()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


    def loginfunction(self):
        try:
            import os
            global pid 
            pid = self.pid_entry.text()
            
            pid_entry_data = pid
            os.environ['PID_ENTRY_DATA'] =pid_entry_data
            
            email = self.email_entry.text()
            password = self.password_entry.text()
            print(pid)
            if len(email)==0 and len(password)==0 and  len(pid)==0:
                self.password_error_message.setText("Please enter the password.")
                self.email_error_message.setText("Please enter your email Id.")
                self.pid_error_message.setText("Please enter your pid.")
                return
                
            if len(email) == 0 and len(password)==0:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.password_error_message.setText("Please enter the password.")
                self.email_error_message.setText("Please enter your email Id.")
                return
                
            if  len(email) == 0 and len(pid)==0:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.pid_error_message.setText("Please enter pid.")
                self.email_error_message.setText("Please enter your email Id.")
                return
                
            if  len(password) == 0 and len(pid)==0:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.password_error_message.setText("Please enter password.")
                self.email_error_message.setText("Please enter your email Id.")
                return
            
            if '@student.sfit.ac.in' not in email:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.email_error_message.setText("Invalid Email format")
                return
                
            if len(password)==0:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.password_error_message.setText("Please enter the password.")
                return
                
            if len(email)==0:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.email_error_message.setText("Please enter your email id.")
                return
                
            if len(pid)==0:
                self.email_error_message.setText("")
                self.pid_error_message.setText("")
                self.password_error_message.setText("")
                self.pid_error_message.setText("Please enter your pid.")
                return
            
            
            self.email_error_message.setText("")
            self.pid_error_message.setText("")
            self.password_error_message.setText("")
            
            conn = sqlite3.connect("eduhub.db")
            cur = conn.cursor()
            cur.execute('SELECT password FROM Users WHERE pid=? and email=?', (pid, email))
            result = cur.fetchone()
            conn.close()  # Remember to close the connection after use
            print(result)

            if result:  # Check if result is not None
                hashed_password = result[0]  # Access the hashed password
                passw_bytes = password.encode('utf-8')  # Encode password to bytes
                print(passw_bytes)

                if bcrypt.checkpw(passw_bytes, hashed_password):
                    self.messagebox.setText("Logged in Successfully!")
                    self.messagebox.setWindowTitle("Success")
                    self.messagebox.exec()
                    
                    
                    #getting to Homepage
                    self.close()
                    # Run main.py to start the homepage
                    subprocess.Popen(["python", "main.py"])
                    sys.exit()
                    
                else:
                    print("Error")
                    self.messagebox.setText("Invalid Details!.")
                    self.messagebox.setWindowTitle("Error")
                    self.messagebox.exec()
            else:
                self.messagebox.setText("User not Found!.")
                self.messagebox.setWindowTitle("Error")
                self.messagebox.exec()
                print("User not found")  # Add some handling for when user is not found

        except Exception as e:
            print(f"Error in loginfunction: {e}")
            


        
#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Edu-hub")
    app_icon = QIcon("icon\Edu_logo-removebg-preview.png") 
    app.setWindowIcon(app_icon)
    login = Loginpage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(login)
    screen_geometry = QGuiApplication.primaryScreen().geometry()
    widget.setGeometry(
        (screen_geometry.width() - widget.width()) // 2,
        (screen_geometry.height() - widget.height()-300) // 2,
        widget.width(),
        widget.height()
    )
    widget.setFixedWidth(540)
    widget.setFixedHeight(760)
    
    widget.show()
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")