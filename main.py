
from email.mime.text import MIMEText
import smtplib
import subprocess

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QTableView, QApplication, QVBoxLayout, QWidget, QHeaderView
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QLineEdit, QTextEdit
import sys, os
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from PyQt5 import QtCore
import sqlite3
from EduHub_home import Ui_MainWindow
from sold_products_viewer import SoldProductsViewer
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
import webbrowser
import traceback


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagebox=QMessageBox()
        
        self.setWindowTitle("Eduhub")
        app_icon = QIcon("icon\Edu_logo-removebg-preview.png") 
        self.setWindowIcon(app_icon)
        
        import os
        global pid_entry_data
        pid_entry_data = os.environ.get('PID_ENTRY_DATA')
        #print("Data from pid_entry in the previous file:", pid_entry_data)
        
        self.ui.Books_btn.setChecked(True)


        self.ui.Books_btn.clicked.connect(lambda : self.prd_type(0))
        self.ui.Calculator.clicked.connect(lambda : self.prd_type(1))
        self.ui.Others.clicked.connect(lambda : self.prd_type(2))
        
        self.ui.prod_1_btn.clicked.connect(lambda: self.prod_descrip_page(1))
        self.ui.prod_2_btn.clicked.connect(lambda: self.prod_descrip_page(2))
        self.ui.prod_3_btn.clicked.connect(lambda: self.prod_descrip_page(3))
        self.ui.prod_4_btn.clicked.connect(lambda: self.prod_descrip_page(4))
        self.ui.prod_5_btn.clicked.connect(lambda: self.prod_descrip_page(5))
        self.ui.prod_6_btn.clicked.connect(lambda: self.prod_descrip_page(6))
        self.ui.prod_7_btn.clicked.connect(lambda: self.prod_descrip_page(7))
        self.ui.prod_21_btn.clicked.connect(lambda: self.prod_descrip_page(8))
        self.ui.prod_22_btn.clicked.connect(lambda: self.prod_descrip_page(9))
        self.ui.prod_23_btn.clicked.connect(lambda: self.prod_descrip_page(10))
        self.ui.prod_24_btn.clicked.connect(lambda: self.prod_descrip_page(11))
        self.ui.prod_25_btn.clicked.connect(lambda: self.prod_descrip_page(12))
        self.ui.prod_26_btn.clicked.connect(lambda: self.prod_descrip_page(13))
        self.ui.prod_27_btn.clicked.connect(lambda: self.prod_descrip_page(14))
        self.ui.prod_41_btn.clicked.connect(lambda: self.prod_descrip_page(15))
        self.ui.prod_42_btn.clicked.connect(lambda: self.prod_descrip_page(16))
        self.ui.prod_43_btn.clicked.connect(lambda: self.prod_descrip_page(17))
        self.ui.prod_44_btn.clicked.connect(lambda: self.prod_descrip_page(18))
        self.ui.prod_45_btn.clicked.connect(lambda: self.prod_descrip_page(19))
        self.ui.prod_46_btn.clicked.connect(lambda: self.prod_descrip_page(20))

        self.ui.back_btn_1.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_2.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_3.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_4.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_5.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_6.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_7.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_8.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_9.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_10.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_11.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_12.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_13.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_14.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_15.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_16.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_17.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_18.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_19.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_20.clicked.connect(self.on_back_btn_toggled)
        
        
        
        
        

        
        conn = sqlite3.connect("eduhub.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Products (
                    image_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    image BLOB,
                    product_name TEXT,
                    product_price INT,
                    description TEXT,
                    type TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users(pid)
                )""")
        
        
        table_name = f"sold_products_{pid_entry_data}"
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                        image_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        image BLOB,
                        product_name TEXT,
                        product_price INT,
                        description TEXT,
                        type TEXT,
                        FOREIGN KEY (user_id) REFERENCES Users(pid)
                    );""")
        buy_table_name= f"buy_products_{pid_entry_data}"
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {buy_table_name} (
                        buy_id INTEGER PRIMARY KEY,
                        image_id INTEGER ,
                        user_id INTEGER,
                        image BLOB,
                        product_name TEXT,
                        product_price INT,
                        description TEXT,
                        type TEXT,
                        FOREIGN KEY (image_id) REFERENCES Products(image_id)
                        FOREIGN KEY (user_id) REFERENCES Users(pid)
                    );""")
        conn.commit()
        
        conn.close()
        
        
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        #self.ui.scrollArea.setAttribute(Qt.WA_TranslucentBackground)
        
        
    
        self.ui.instagram.clicked.connect(self.open_instagram)
        self.ui.youtube.clicked.connect(self.open_youtube)
        self.ui.twitter.clicked.connect(self.open_twitter)
        self.ui.facebook.clicked.connect(self.open_facebook)

        self.ui.prod_1_btn.clicked.connect(self.on_prod_1_btn_toggled)
        self.ui.prod_2_btn.clicked.connect(self.on_prod_2_btn_toggled)

        self.ui.back_btn_1.clicked.connect(self.on_back_btn_toggled)
        self.ui.back_btn_2.clicked.connect(self.on_back_btn_toggled)


        # Access the Upload_Image_btn button from the generated class
        self.Upload_Image_btn = self.ui.Upload_Image_btn
        self.Upload_Image_btn.clicked.connect(self.upload_image_clicked)
        
        self.set_product_information()        
        self.books_button = self.ui.Books_btn
        self.books_button.clicked.connect(self.set_product_information)
        
        """self.calc_button = self.ui.Calculator
        self.calc_button.clicked.connect(self.set_calculator_product_information)
        
        self.other_button = self.ui.Others
        self.other_button.clicked.connect(self.set_other_product_information)"""
        
        
        
        self.history = self.ui.pushButton_2
        self.history.clicked.connect(self.show_history_clicked)
        
        
        self.ui.label_15.setText(pid_entry_data)

        
        #Accessing labels from sellpage
        self.product_save = self.ui.pushButton_5
        self.product_save.clicked.connect(self.confirm_sale_clicked)
        
        self.logout_button_1 = self.ui.logout_btn_1
        self.logout_button_1.clicked.connect(self.logout)
        
        self.logout_button_2 = self.ui.logout_btn_2
        self.logout_button_2.clicked.connect(self.logout)
        
        
        self.conn = sqlite3.connect('eduhub.db')

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
    

        
        table_name = f"sold_products_{pid_entry_data}"
        sold_products = self.ui.tableView_2
        self.load_data_into_tableview(sold_products, table_name)
        
        table_name_buy = f"buy_products_{pid_entry_data}"
        buy_products = self.ui.tableView
        self.load_data_into_buy(buy_products, table_name_buy)
        
        for i in range(1, 20):
            try:
                buy_button = getattr(self.ui, f"buy_btn_{i}")
                buy_button.clicked.connect(lambda _, index=i: self.product_sold(index))
                
                print(f"Connected pushButton_{i}")
            except Exception as e:
                print(f"Error connecting pushButton_{i}: {e}")
                
        
                
                
       
        
        




    def open_instagram(self):
        webbrowser.open_new(url="https://www.instagram.com/edu_hub.001/")

    def open_youtube(self):
        webbrowser.open_new(url="https://youtube.com/@EduHub-jo2cf?si=oFlNiGPt_xNnT1n4")

    def open_twitter(self):
        webbrowser.open_new(url="https://twitter.com/?lang=en")

    def open_facebook(self):
        webbrowser.open_new(url="https://www.facebook.com/people/Edu-Hub/pfbid02Yn2WGCG1Gh8nQSXt6WUw2BrJv6NtzxD4rYinf7gGKwNYpRKbMr88FXCe7Kf6AxR1l/")
        
    def prd_type(self , i):
        self.ui.stackedWidget1.setCurrentIndex(i)
    
    #Product description back button
    def on_back_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)    

    #prod description page change code
    def prod_descrip_page(self , i):
        ind = i + 4
        self.ui.stackedWidget.setCurrentIndex(ind)



    
        
        
    

    def product_sold(self, i):
        print(f"Product sold by button {i}:")
        
        try:
            conn = sqlite3.connect("eduhub.db")
            cur = conn.cursor()
            buy_table_name = f"buy_products_{pid_entry_data}"
            
            product_name = getattr(self.ui, f"prod_{i}_des_name").text()
            product_price = getattr(self.ui, f"prod_{i}_des_price").text()
            description = getattr(self.ui, f"prod_{i}_des_description").text()
            prod_type = getattr(self.ui, f"prod_{i}_des_relevance").text()
            b_image = getattr(self.ui, f"prod_{i}_des_img")
            seller_id = getattr(self.ui, f"prod_{i}_des_sellerid").text()
            buy_image = b_image.pixmap()
            if buy_image is not None:
                image = buy_image.toImage()
                image_bytes = QByteArray()
                buffer = QBuffer(image_bytes)
                buffer.open(QIODevice.WriteOnly)
                image.save(buffer, "PNG")  # Change "PNG" to the appropriate format if needed
                image_data = bytes(image_bytes)
            else:
                raise ValueError("No image found")

            cur.execute(f"INSERT INTO {buy_table_name} (user_id, image, product_name, product_price, description, type) VALUES (?, ?, ?, ?, ?, ?)",
                        (pid_entry_data, image_data, product_name, product_price, description, prod_type))
            try:
                # Execute the DELETE statement
                # Assuming you're using Python and SQLite3
                print("Deleting row with values:", seller_id, product_name, product_price, prod_type)
                cur.execute("DELETE FROM Products WHERE user_id = ? AND product_name = ? AND type = ?", (seller_id, product_name, prod_type))

                # Commit the transaction
                conn.commit()
                print("Row deleted successfully.")
            except sqlite3.Error as e:
                # Handle any errors
                print("Error in product sold:")
                traceback.print_exc()
            conn.commit()
            

            self.messagebox.setText("Thank you for your purchase, you will be redirected to the Chat room of the seller")
            self.messagebox.setWindowTitle("Success")
            self.messagebox.exec()
            
            cur.execute("SELECT email, username FROM Users WHERE pid = ?", (seller_id, ));
            result = cur.fetchone()
            email, name = result
            print(email,name)
            cur.execute("SELECT email, username, branch FROM Users WHERE pid = ?", (pid_entry_data, ));
            result_2 = cur.fetchone()
            buyer_email, buyer_name, buyer_branch = result_2
            print(buyer_email,buyer_name,buyer_branch)
            
            conn.close()
            
            subject = f"Your Product '{product_name}' Has Been Sold"
            body = f"Dear {name},\n\n" \
            f"We are pleased to inform you that your product '{product_name}' has been sold to Mr '{buyer_name} from '{buyer_branch}'!\n\n" \
            f"For further procedure please contact the Buyer whose email info is : '{buyer_email}'.\n\n" \
            "Thank you for using our platform.\n\n" \
            "Best regards,\n" \
            "Eduhub"
            
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
                
                print("Email sent for purchase")
            
            #table_name = f"sold_products_{pid_entry_data}"
            #sold_products = self.ui.tableView_2
            #self.load_data_into_tableview(sold_products, table_name)
            
            table_name_buy = f"buy_products_{pid_entry_data}"
            buy_products = self.ui.tableView
            self.load_data_into_buy(buy_products, table_name_buy)
                
            self.on_home_btn_2_toggled()
            
            print(f"Buy button {i} clicked, redirect to chat room")
            
            
            subprocess.Popen(["python", "server.py"])
            subprocess.Popen(["python", "client.py"])
            subprocess.Popen(["python", "client.py"])
            subprocess.call(["python", "-c", "from _main_ import set_book_product_information; set_book_product_information()"])
            subprocess.call(["python", "-c", "from _main_ import on_home_btn_toggled; on_home_btn_toggled()"])
            
            

        except Exception as e:
            print("Error:", e)
            self.messagebox.setText("An error occurred while processing your purchase. Please try again later.")
            self.messagebox.setWindowTitle("Error")
            self.messagebox.exec()
        
    def confirm_sale_clicked(self):
        self.product_name = self.ui.sell_prod_name.text()
        self.product_price = self.ui.sell_prod_name_2.text()
        self.product_description = self.ui.textEdit_2.toPlainText()
        self.product_type = self.ui.comboBox.currentText()
        print(self.product_description)

        try:
            conn = sqlite3.connect("eduhub.db")
            cur = conn.cursor()
            table_name = f"sold_products_{pid_entry_data}"
            cur.execute("SELECT MAX(image_id) FROM Products")
            image_id = cur.fetchone()[0]
            print("Highest image ID in main.py file:", image_id)
            cur.execute("UPDATE Products SET product_name = ?, product_price = ?, description = ?, type = ? WHERE image_id = ? AND user_id = ?", (self.product_name, self.product_price, self.product_description, self.product_type, image_id, pid_entry_data))
            conn.commit()
            
            cur.execute(f"SELECT MAX(image_id) FROM {table_name}")
            image_id2 = cur.fetchone()[0]
            print("Highest image ID in main.py file:", image_id)
            
            cur.execute(f"UPDATE {table_name} SET product_name = ?, product_price = ?, description = ?, type = ? WHERE image_id = ? AND user_id = ?", (self.product_name, self.product_price, self.product_description, self.product_type, image_id2, pid_entry_data))
            conn.commit()
            conn.close()
            self.ui.sell_prod_name.setText("")
            self.ui.sell_prod_name_2.setText("")
            self.ui.textEdit_2.setText("")
            self.ui.comboBox.setCurrentText("Type")
            self.ui.label_13.setText("Select Product Image")
            
            QMessageBox.information(self, "Success", "Sale confirmed.")
            table_name = f"sold_products_{pid_entry_data}"
            sold_products = self.ui.tableView_2
            self.load_data_into_tableview(sold_products, table_name)
            
            table_name_buy = f"buy_products_{pid_entry_data}"
            buy_products = self.ui.tableView
            self.load_data_into_buy(buy_products, table_name_buy)
            
        except Exception as e:
                    print(f"Error in confirm_sale_clicked: {e}")


        
   
        
        
    
    def upload_image_clicked(self):
        # Implement your functionality here when the button is clicked
        print("Upload Image button clicked")
        process =subprocess.Popen(["python", "drop_file.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)        
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print("Subprocess completed successfully.")
            table_name = f"sold_products_{pid_entry_data}"
            conn = sqlite3.connect("eduhub.db")
            cur = conn.cursor()
            cur.execute(f"SELECT image FROM {table_name} ORDER BY image_id DESC LIMIT 1")
            result = cur.fetchone()
            conn.close()
            if result:
                image = result[0]
                pixmap = QPixmap()
                pixmap.loadFromData(image)
                scaled_pixmap = pixmap.scaled(300, 360, Qt.KeepAspectRatio)
                self.ui.label_13.setPixmap(scaled_pixmap)
                self.ui.label_13.adjustSize()
                
            # Your remaining code here
        else:
            print("Subprocess failed with error:", stderr.decode())

        
        
        
        
        
    def show_history_clicked(self):
        print("History button clicked")
        subprocess.Popen(["python", "sold_products_viewer.py"])
        
        
    def load_data_into_buy(self, table_view, table_name):
        conn = sqlite3.connect('eduhub.db')
        cur = conn.cursor()
        cur.execute(f"SELECT product_name, product_price, description FROM {table_name}")
        rows = cur.fetchall()
        conn.close()

        headers = ["Name", "Price", "Description"]
        model = QStandardItemModel(len(rows), len(headers))
        model.setHorizontalHeaderLabels(headers)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QStandardItem(str(col))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                model.setItem(i, j, item)
                
        self.setStyleSheet ("""
            #headers {
                background:transparent;
            }
        """)

        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def load_data_into_tableview(self, table_view_2, table_name):
        conn = sqlite3.connect('eduhub.db')
        cur = conn.cursor()
        cur.execute(f"SELECT product_name, product_price, description FROM {table_name}")
        rows = cur.fetchall()
        conn.close()

        headers = ["Name", "Price", "Description"]
        model = QStandardItemModel(len(rows), len(headers))
        model.setHorizontalHeaderLabels(headers)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QStandardItem(str(col))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                model.setItem(i, j, item)

        table_view_2.setModel(model)
        table_view_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
        
    def logout(self):
        # Update the 'active' column to False in the User table for the current user
        conn = sqlite3.connect('eduhub.db')
        cur = conn.cursor()
        cur.execute("UPDATE Users SET active = ? WHERE pid = ?", (False, pid_entry_data))
        conn.commit()
        conn.close()

        # Navigate back to the registration page
        self.close()
        # Run main.py to start the homepage
        subprocess.Popen(["python", "registration.py"])
        sys.exit()
        

    
    def set_product_information(self):
        try:
            
            conn = sqlite3.connect('eduhub.db')
            
            
            #Start of Database se fetch query
            #Buy products books widgets and btns           
            prod_wid_books = [
                        (self.ui.prod_1_1 , self.ui.prod_1_2 , self.ui.prod_1_btn) , (self.ui.prod_2_1 , self.ui.prod_2_2 , self.ui.prod_2_btn) , 
                        (self.ui.prod_3_1 , self.ui.prod_3_2 , self.ui.prod_3_btn) , (self.ui.prod_4_1 , self.ui.prod_4_2 , self.ui.prod_4_btn) ,
                        (self.ui.prod_5_1 , self.ui.prod_5_2 , self.ui.prod_5_btn) , (self.ui.prod_6_1 , self.ui.prod_6_2 , self.ui.prod_6_btn) ,
                        (self.ui.prod_7_1 , self.ui.prod_7_2 , self.ui.prod_7_btn) , (self.ui.prod_8_1 , self.ui.prod_8_2 , self.ui.prod_8_btn) ,
                        (self.ui.prod_9_1 , self.ui.prod_9_2 , self.ui.prod_9_btn) , (self.ui.prod_10_1 , self.ui.prod_10_2 , self.ui.prod_10_btn) ,
                        (self.ui.prod_11_1 , self.ui.prod_11_2 , self.ui.prod_11_btn) , (self.ui.prod_12_1 , self.ui.prod_12_2 , self.ui.prod_12_btn) ,
                        (self.ui.prod_13_1 , self.ui.prod_13_2 , self.ui.prod_13_btn) , (self.ui.prod_14_1 , self.ui.prod_14_2 , self.ui.prod_14_btn) ,
                        (self.ui.prod_15_1 , self.ui.prod_15_2 , self.ui.prod_15_btn) , (self.ui.prod_16_1 , self.ui.prod_16_2 , self.ui.prod_16_btn) ,
                        (self.ui.prod_17_1 , self.ui.prod_17_2 , self.ui.prod_17_btn) , (self.ui.prod_18_1 , self.ui.prod_18_2 , self.ui.prod_18_btn) ,
                        (self.ui.prod_19_1 , self.ui.prod_19_2 , self.ui.prod_19_btn) , (self.ui.prod_20_1 , self.ui.prod_20_2 , self.ui.prod_20_btn) ,             
                    ]
            
            #buy product category wise books fields
            widgets_books = [
                    (self.ui.prod_1_name  , self.ui.prod_1_price  , self.ui.prod_1_img  ) , 
                    (self.ui.prod_2_name  , self.ui.prod_2_price  , self.ui.prod_2_img  ) ,
                    (self.ui.prod_3_name  , self.ui.prod_3_price  , self.ui.prod_3_img  ) ,
                    (self.ui.prod_4_name  , self.ui.prod_4_price  , self.ui.prod_4_img  ) ,
                    (self.ui.prod_5_name  , self.ui.prod_5_price  , self.ui.prod_5_img  ) , 
                    (self.ui.prod_6_name  , self.ui.prod_6_price  , self.ui.prod_6_img  ) ,
                    (self.ui.prod_7_name  , self.ui.prod_7_price  , self.ui.prod_7_img  ) ,
                    (self.ui.prod_8_name  , self.ui.prod_8_price  , self.ui.prod_8_img  ) ,
                    (self.ui.prod_9_name  , self.ui.prod_9_price  , self.ui.prod_9_img  ) ,
                    (self.ui.prod_10_name , self.ui.prod_10_price , self.ui.prod_10_img ) ,
                    (self.ui.prod_11_name , self.ui.prod_11_price , self.ui.prod_11_img ) ,
                    (self.ui.prod_12_name , self.ui.prod_12_price , self.ui.prod_12_img ) ,
                    (self.ui.prod_13_name , self.ui.prod_13_price , self.ui.prod_13_img ) ,
                    (self.ui.prod_14_name , self.ui.prod_14_price , self.ui.prod_14_img ) ,
                    (self.ui.prod_15_name , self.ui.prod_15_price , self.ui.prod_15_img ) ,
                    (self.ui.prod_16_name , self.ui.prod_16_price , self.ui.prod_16_img ) ,
                    (self.ui.prod_17_name , self.ui.prod_17_price , self.ui.prod_17_img ) ,
                    (self.ui.prod_18_name , self.ui.prod_18_price , self.ui.prod_18_img ) ,
                    (self.ui.prod_19_name , self.ui.prod_19_price , self.ui.prod_19_img ) ,
                    (self.ui.prod_20_name , self.ui.prod_20_price , self.ui.prod_20_img ) 
                    ]
            

            prod_des_books = [
                        (self.ui.prod_1_des_name , self.ui.prod_1_des_price , self.ui.prod_1_des_img , self.ui.prod_1_des_sellerid , self.ui.prod_1_des_description , self.ui.prod_1_des_relevance ),
                        (self.ui.prod_2_des_name , self.ui.prod_2_des_price , self.ui.prod_2_des_img , self.ui.prod_2_des_sellerid , self.ui.prod_2_des_description , self.ui.prod_2_des_relevance ),
                        (self.ui.prod_3_des_name , self.ui.prod_3_des_price , self.ui.prod_3_des_img , self.ui.prod_3_des_sellerid , self.ui.prod_3_des_description , self.ui.prod_3_des_relevance ),
                        (self.ui.prod_4_des_name , self.ui.prod_4_des_price , self.ui.prod_4_des_img , self.ui.prod_4_des_sellerid , self.ui.prod_4_des_description , self.ui.prod_4_des_relevance ),
                        (self.ui.prod_5_des_name , self.ui.prod_5_des_price , self.ui.prod_5_des_img , self.ui.prod_5_des_sellerid , self.ui.prod_5_des_description , self.ui.prod_5_des_relevance ),
                        (self.ui.prod_6_des_name , self.ui.prod_6_des_price , self.ui.prod_6_des_img , self.ui.prod_6_des_sellerid , self.ui.prod_6_des_description , self.ui.prod_6_des_relevance ),
                        (self.ui.prod_7_des_name , self.ui.prod_7_des_price , self.ui.prod_7_des_img , self.ui.prod_7_des_sellerid , self.ui.prod_7_des_description , self.ui.prod_7_des_relevance )
                        ]
            



            #buy products page for loop for books
            cursor = conn.cursor()
            cursor.execute("SELECT product_name, product_price, image FROM Products WHERE type = 'Books' ORDER BY image_id DESC LIMIT 7;")
            products = cursor.fetchall()

            #To hide extra widgets
            for index, widget_tuple in enumerate(prod_wid_books):
                if index < len(products):
                    for widget in widget_tuple:
                        widget.show()
                else:
                    for widget in widget_tuple:
                        widget.hide()

            #To set value in visible widgets and fields
            for i, (name_widget, price_widget, img_widget) in enumerate(widgets_books):
                if i < len(products):
                                   
                    product = products[i]
                    name_widget.setText(product[0])
                    
                    rupee_symbol = "₹"
                    price_with_rupee = f"{rupee_symbol}{product[1]}"
                    price_widget.setText(price_with_rupee)

                    # Set image from blob data
                    image_data = product[2]
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    img_widget.setPixmap(pixmap.scaled(img_widget.size(), QtCore.Qt.KeepAspectRatio))



            #description pages for loop for books category
            rupee_symbol = "₹"

            cursor = conn.cursor()
            cursor.execute("SELECT product_name, product_price, image , user_id , description , type FROM Products WHERE type = 'Books' ORDER BY image_id DESC LIMIT 7")
            products = cursor.fetchall()

            for i, (name_widget, price_widget, img_widget, sellerid_widget, des_widget, rel_widget) in enumerate(prod_des_books):
                if i < len(products):
                    product = products[i]
                    name_widget.setText(product[0])
                    
                    price_with_rupee = f"{rupee_symbol}{product[1]}"
                    price_widget.setText(price_with_rupee)

                    selid = str(product[3])
                    sellerid_widget.setText(selid)

                    des_widget.setText(product[4])
                    rel_widget.setText(product[5])

                    # Set image from blob data
                    image_data = product[2]
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    img_widget.setPixmap(pixmap.scaled(img_widget.size(), QtCore.Qt.KeepAspectRatio))
            







            prod_wid_calc= [(self.ui.prod_21_1 , self.ui.prod_21_2 , self.ui.prod_21_btn) , (self.ui.prod_22_1 , self.ui.prod_22_2 , self.ui.prod_22_btn) , 
                            (self.ui.prod_23_1 , self.ui.prod_23_2 , self.ui.prod_23_btn) , (self.ui.prod_24_1 , self.ui.prod_24_2 , self.ui.prod_24_btn) ,
                            (self.ui.prod_25_1 , self.ui.prod_25_2 , self.ui.prod_25_btn) , (self.ui.prod_26_1 , self.ui.prod_26_2 , self.ui.prod_26_btn) ,
                            (self.ui.prod_27_1 , self.ui.prod_27_2 , self.ui.prod_27_btn) , (self.ui.prod_28_1 , self.ui.prod_28_2 , self.ui.prod_28_btn) ,
                            (self.ui.prod_29_1 , self.ui.prod_29_2 , self.ui.prod_29_btn) , (self.ui.prod_30_1 , self.ui.prod_30_2 , self.ui.prod_30_btn) ,
                            (self.ui.prod_31_1 , self.ui.prod_31_2 , self.ui.prod_31_btn) , (self.ui.prod_32_1 , self.ui.prod_32_2 , self.ui.prod_32_btn) ,
                            (self.ui.prod_33_1 , self.ui.prod_33_2 , self.ui.prod_33_btn) , (self.ui.prod_34_1 , self.ui.prod_34_2 , self.ui.prod_34_btn) ,
                            (self.ui.prod_35_1 , self.ui.prod_35_2 , self.ui.prod_35_btn) , (self.ui.prod_36_1 , self.ui.prod_36_2 , self.ui.prod_36_btn) ,
                            (self.ui.prod_37_1 , self.ui.prod_37_2 , self.ui.prod_37_btn) , (self.ui.prod_38_1 , self.ui.prod_38_2 , self.ui.prod_38_btn) ,
                            (self.ui.prod_39_1 , self.ui.prod_39_2 , self.ui.prod_39_btn) , (self.ui.prod_40_1 , self.ui.prod_40_2 , self.ui.prod_40_btn) ,             
                        ]
            
            widgets_calc = [
                    (self.ui.prod_21_name , self.ui.prod_21_price , self.ui.prod_21_img ) , 
                    (self.ui.prod_22_name , self.ui.prod_22_price , self.ui.prod_22_img ) ,
                    (self.ui.prod_23_name , self.ui.prod_23_price , self.ui.prod_23_img ) ,
                    (self.ui.prod_24_name , self.ui.prod_24_price , self.ui.prod_24_img ) ,
                    (self.ui.prod_25_name , self.ui.prod_25_price , self.ui.prod_25_img ) , 
                    (self.ui.prod_26_name , self.ui.prod_26_price , self.ui.prod_26_img ) ,
                    (self.ui.prod_27_name , self.ui.prod_27_price , self.ui.prod_27_img ) ,
                    (self.ui.prod_28_name , self.ui.prod_28_price , self.ui.prod_28_img ) ,
                    (self.ui.prod_29_name , self.ui.prod_29_price , self.ui.prod_29_img ) ,
                    (self.ui.prod_30_name , self.ui.prod_30_price , self.ui.prod_30_img ) ,
                    (self.ui.prod_31_name , self.ui.prod_31_price , self.ui.prod_31_img ) ,
                    (self.ui.prod_32_name , self.ui.prod_32_price , self.ui.prod_32_img ) ,
                    (self.ui.prod_33_name , self.ui.prod_33_price , self.ui.prod_33_img ) ,
                    (self.ui.prod_34_name , self.ui.prod_34_price , self.ui.prod_34_img ) ,
                    (self.ui.prod_35_name , self.ui.prod_35_price , self.ui.prod_35_img ) ,
                    (self.ui.prod_36_name , self.ui.prod_36_price , self.ui.prod_36_img ) ,
                    (self.ui.prod_37_name , self.ui.prod_37_price , self.ui.prod_37_img ) ,
                    (self.ui.prod_38_name , self.ui.prod_38_price , self.ui.prod_38_img ) ,
                    (self.ui.prod_39_name , self.ui.prod_39_price , self.ui.prod_39_img ) ,
                    (self.ui.prod_40_name , self.ui.prod_40_price , self.ui.prod_40_img ) 
                    ]
            
            prod_des_calc = [
                        (self.ui.prod_8_des_name , self.ui.prod_8_des_price , self.ui.prod_8_des_img , self.ui.prod_8_des_sellerid , self.ui.prod_8_des_description , self.ui.prod_8_des_relevance ),
                        (self.ui.prod_9_des_name , self.ui.prod_9_des_price , self.ui.prod_9_des_img , self.ui.prod_9_des_sellerid , self.ui.prod_9_des_description , self.ui.prod_9_des_relevance ),
                        (self.ui.prod_10_des_name, self.ui.prod_10_des_price, self.ui.prod_10_des_img, self.ui.prod_10_des_sellerid, self.ui.prod_10_des_description, self.ui.prod_10_des_relevance ),
                        (self.ui.prod_11_des_name, self.ui.prod_11_des_price, self.ui.prod_11_des_img, self.ui.prod_11_des_sellerid, self.ui.prod_11_des_description, self.ui.prod_11_des_relevance ),
                        (self.ui.prod_12_des_name, self.ui.prod_12_des_price, self.ui.prod_12_des_img, self.ui.prod_12_des_sellerid, self.ui.prod_12_des_description, self.ui.prod_12_des_relevance ),
                        (self.ui.prod_13_des_name, self.ui.prod_13_des_price, self.ui.prod_13_des_img, self.ui.prod_13_des_sellerid, self.ui.prod_13_des_description, self.ui.prod_13_des_relevance ),
                        (self.ui.prod_14_des_name, self.ui.prod_14_des_price, self.ui.prod_14_des_img, self.ui.prod_14_des_sellerid, self.ui.prod_14_des_description, self.ui.prod_14_des_relevance )
                        ]

             

            #buy products page for loop for calculator
            cursor = conn.cursor()
            cursor.execute("SELECT product_name, product_price, image FROM Products WHERE type = 'Calculator' ORDER BY image_id DESC LIMIT 7;")
            products = cursor.fetchall()

            #To hide extra widgets
            for index, widget_tuple in enumerate(prod_wid_calc):
                if index < len(products):
                    for widget in widget_tuple:
                        widget.show()
                else:
                    for widget in widget_tuple:
                        widget.hide()

            #To set value in visible widgets and fields
            for i, (name_widget, price_widget, img_widget) in enumerate(widgets_calc):
                if i < len(products):         
                    product = products[i]
                    name_widget.setText(product[0])

                    price_with_rupee = f"{rupee_symbol}{product[1]}"
                    price_widget.setText(price_with_rupee)

                    # Set image from blob data
                    image_data = product[2]
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    img_widget.setPixmap(pixmap.scaled(img_widget.size(), QtCore.Qt.KeepAspectRatio))


            #description pages for loop for books category
            rupee_symbol = "₹"

            cursor = conn.cursor()
            cursor.execute("SELECT product_name, product_price, image , user_id , description , type FROM Products WHERE type = 'Calculator' ORDER BY image_id DESC LIMIT 7")
            products = cursor.fetchall()

            for i, (name_widget, price_widget, img_widget, sellerid_widget, des_widget, rel_widget) in enumerate(prod_des_calc):
                if i < len(products):
                    product = products[i]
                    name_widget.setText(product[0])
                    
                    price_with_rupee = f"{rupee_symbol}{product[1]}"
                    price_widget.setText(price_with_rupee)

                    selid = str(product[3])
                    sellerid_widget.setText(selid)

                    des_widget.setText(product[4])
                    rel_widget.setText(product[5])

                    # Set image from blob data
                    image_data = product[2]
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    img_widget.setPixmap(pixmap.scaled(img_widget.size(), QtCore.Qt.KeepAspectRatio))
            






            
            prod_wid_other=[(self.ui.prod_41_1 , self.ui.prod_41_2 , self.ui.prod_41_btn) , (self.ui.prod_42_1 , self.ui.prod_42_2 , self.ui.prod_42_btn) , 
                            (self.ui.prod_43_1 , self.ui.prod_43_2 , self.ui.prod_43_btn) , (self.ui.prod_44_1 , self.ui.prod_44_2 , self.ui.prod_44_btn) ,
                            (self.ui.prod_45_1 , self.ui.prod_45_2 , self.ui.prod_45_btn) , (self.ui.prod_46_1 , self.ui.prod_46_2 , self.ui.prod_46_btn) ,
                            (self.ui.prod_47_1 , self.ui.prod_47_2 , self.ui.prod_47_btn) , (self.ui.prod_48_1 , self.ui.prod_48_2 , self.ui.prod_48_btn) ,
                            (self.ui.prod_49_1 , self.ui.prod_49_2 , self.ui.prod_49_btn) , (self.ui.prod_50_1 , self.ui.prod_50_2 , self.ui.prod_50_btn) ,
                            (self.ui.prod_51_1 , self.ui.prod_51_2 , self.ui.prod_51_btn) , (self.ui.prod_52_1 , self.ui.prod_52_2 , self.ui.prod_52_btn) ,
                            (self.ui.prod_53_1 , self.ui.prod_53_2 , self.ui.prod_53_btn) , (self.ui.prod_54_1 , self.ui.prod_54_2 , self.ui.prod_54_btn) ,
                            (self.ui.prod_55_1 , self.ui.prod_55_2 , self.ui.prod_55_btn) , (self.ui.prod_56_1 , self.ui.prod_56_2 , self.ui.prod_56_btn) ,
                            (self.ui.prod_57_1 , self.ui.prod_57_2 , self.ui.prod_57_btn) , (self.ui.prod_58_1 , self.ui.prod_58_2 , self.ui.prod_58_btn) ,
                            (self.ui.prod_59_1 , self.ui.prod_59_2 , self.ui.prod_59_btn) , (self.ui.prod_60_1 , self.ui.prod_60_2 , self.ui.prod_60_btn) ,             
                        ]
            
            widgets_others = [
                    (self.ui.prod_41_name , self.ui.prod_41_price , self.ui.prod_41_img ) , 
                    (self.ui.prod_42_name , self.ui.prod_42_price , self.ui.prod_42_img ) ,
                    (self.ui.prod_43_name , self.ui.prod_43_price , self.ui.prod_43_img ) ,
                    (self.ui.prod_44_name , self.ui.prod_44_price , self.ui.prod_44_img ) ,
                    (self.ui.prod_45_name , self.ui.prod_45_price , self.ui.prod_45_img ) , 
                    (self.ui.prod_46_name , self.ui.prod_46_price , self.ui.prod_46_img ) ,
                    (self.ui.prod_47_name , self.ui.prod_47_price , self.ui.prod_47_img ) ,
                    (self.ui.prod_48_name , self.ui.prod_48_price , self.ui.prod_48_img ) ,
                    (self.ui.prod_49_name , self.ui.prod_49_price , self.ui.prod_49_img ) ,
                    (self.ui.prod_50_name , self.ui.prod_50_price , self.ui.prod_50_img ) ,
                    (self.ui.prod_51_name , self.ui.prod_51_price , self.ui.prod_51_img ) ,
                    (self.ui.prod_52_name , self.ui.prod_52_price , self.ui.prod_52_img ) ,
                    (self.ui.prod_53_name , self.ui.prod_53_price , self.ui.prod_53_img ) ,
                    (self.ui.prod_54_name , self.ui.prod_54_price , self.ui.prod_54_img ) ,
                    (self.ui.prod_55_name , self.ui.prod_55_price , self.ui.prod_55_img ) ,
                    (self.ui.prod_56_name , self.ui.prod_56_price , self.ui.prod_56_img ) ,
                    (self.ui.prod_57_name , self.ui.prod_57_price , self.ui.prod_57_img ) ,
                    (self.ui.prod_58_name , self.ui.prod_58_price , self.ui.prod_58_img ) ,
                    (self.ui.prod_59_name , self.ui.prod_59_price , self.ui.prod_59_img ) ,
                    (self.ui.prod_60_name , self.ui.prod_60_price , self.ui.prod_60_img ) 
                    ]
            
            prod_des_others = [
                        (self.ui.prod_15_des_name, self.ui.prod_15_des_price, self.ui.prod_15_des_img, self.ui.prod_15_des_sellerid, self.ui.prod_15_des_description, self.ui.prod_15_des_relevance ),
                        (self.ui.prod_16_des_name, self.ui.prod_16_des_price, self.ui.prod_16_des_img, self.ui.prod_16_des_sellerid, self.ui.prod_16_des_description, self.ui.prod_16_des_relevance ),
                        (self.ui.prod_17_des_name, self.ui.prod_17_des_price, self.ui.prod_17_des_img, self.ui.prod_17_des_sellerid, self.ui.prod_17_des_description, self.ui.prod_17_des_relevance ),
                        (self.ui.prod_18_des_name, self.ui.prod_18_des_price, self.ui.prod_18_des_img, self.ui.prod_18_des_sellerid, self.ui.prod_18_des_description, self.ui.prod_18_des_relevance ),
                        (self.ui.prod_19_des_name, self.ui.prod_19_des_price, self.ui.prod_19_des_img, self.ui.prod_19_des_sellerid, self.ui.prod_19_des_description, self.ui.prod_19_des_relevance ),
                        (self.ui.prod_20_des_name, self.ui.prod_20_des_price, self.ui.prod_20_des_img, self.ui.prod_20_des_sellerid, self.ui.prod_20_des_description, self.ui.prod_20_des_relevance ),
                        ]            


            
            #buy products page for loop for others
            cursor = conn.cursor()
            cursor.execute("SELECT product_name, product_price, image FROM Products WHERE type = 'Others' ORDER BY image_id DESC LIMIT 5;")
            products = cursor.fetchall()
            
            #To hide extra widgets
            for index, widget_tuple in enumerate(prod_wid_other):
                if index < len(products):
                    for widget in widget_tuple:
                        widget.show()
                else:
                    for widget in widget_tuple:
                        widget.hide()

            #To set value in visible widgets and fields
            for i, (name_widget, price_widget, img_widget) in enumerate(widgets_others):
                if i < len(products):
                                   
                    product = products[i]
                    name_widget.setText(product[0])

                    price_with_rupee = f"{rupee_symbol}{product[1]}"
                    price_widget.setText(price_with_rupee)

                    # Set image from blob data
                    image_data = product[2]
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    img_widget.setPixmap(pixmap.scaled(img_widget.size(), QtCore.Qt.KeepAspectRatio))



            #description pages for loop for books category
            cursor = conn.cursor()
            cursor.execute("SELECT product_name, product_price, image , user_id , description , type FROM Products WHERE type = 'Others' ORDER BY image_id DESC LIMIT 6")
            products = cursor.fetchall()

            for i, (name_widget, price_widget, img_widget, sellerid_widget, des_widget, rel_widget) in enumerate(prod_des_others):
                if i < len(products):
                    product = products[i]
                    name_widget.setText(product[0])

                    rupee_symbol = "₹"
                    price_with_rupee = f"{rupee_symbol}{product[1]}"
                    price_widget.setText(price_with_rupee)

                    selid = str(product[3])
                    sellerid_widget.setText(selid)

                    des_widget.setText(product[4])
                    rel_widget.setText(product[5])

                    # Set image from blob data
                    image_data = product[2]
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    img_widget.setPixmap(pixmap.scaled(img_widget.size(), QtCore.Qt.KeepAspectRatio))

        
            
        except sqlite3.Error as e:
            print("Error fetching product information:", e)

#End of Database se fetch for books query    
        

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
    


    def on_back_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_buy_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.set_product_information()

    def on_buy_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.set_product_information()

    def on_sell_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_sell_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        

    def on_chat_room_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_chat_room_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
    def on_menu_btn_toggled(self):
        self.ui.stackedWidget.setMinimumWidth(873)
    
    def on_prod_1_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_prod_2_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


