import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sqlite3
from EduHub_home import Ui_MainWindow
from main import MainWindow


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)
class AppDemo(QWidget):
    import os
    global pid_entry_data
    pid_entry_data = os.environ.get('PID_ENTRY_DATA')
    #print("Data from pid_entry in the previous file:", pid_entry_data)
    
    
    def __init__(self):
        super().__init__()
        self.resize(500, 400)  # Adjusted the height for better visibility
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()
        

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        # Add a button for opening the file explorer
        self.selectFileButton = QPushButton("Browse Image")
        self.selectFileButton.clicked.connect(self.open_file_dialog)
        mainLayout.addWidget(self.selectFileButton)
        
        
        
        self.saveToDbButton = QPushButton("Select Image")
        self.saveToDbButton.clicked.connect(self.save_to_database)
        mainLayout.addWidget(self.saveToDbButton)
        self.setLayout(mainLayout)

    def set_image(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.photoViewer.setPixmap(pixmap)
        with open(file_path, 'rb') as f:
            self.image_data = f.read()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Browse Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)", options=options)
        if file_path:
            self.set_image(file_path)
            
    def save_to_database(self):
        try:
            
            if hasattr(self, 'image_data') and pid_entry_data:
                conn = sqlite3.connect("eduhub.db")
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS Products (
                    image_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    image BLOB,
                    product_name TEXT,
                    product_price INT,
                    description TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users(pid)
                )""")
                cur.execute("INSERT INTO Products (user_id, image) VALUES (?, ?)", (pid_entry_data, self.image_data))
                conn.commit()
                
                table_name = f"sold_products_{pid_entry_data}"
                cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                                image_id INTEGER PRIMARY KEY,
                                user_id INTEGER,
                                image BLOB,
                                product_name TEXT,
                                product_price INT,
                                description TEXT,
                                FOREIGN KEY (user_id) REFERENCES Users(pid)
                            );""")
                cur.execute(f"INSERT INTO {table_name} (user_id, image) VALUES (?, ?)", (pid_entry_data, self.image_data))
                conn.commit()
                conn.close()
                
                QMessageBox.information(self, "Success", "Image saved to database successfully.")
                #cur.execute(f"SELECT image FROM {self.table_name}")
                #self.label_13.setPixmap(self.image_data)
                
                
                sys.exit()
                
            else:
                QMessageBox.warning(self, "Error", "No image selected or user ID not available.")
        except Exception as e:
            print(f"Error in save_to_database: {e}")


    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())
