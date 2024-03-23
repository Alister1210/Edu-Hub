import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QPushButton, QFileDialog, QMessageBox, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class SoldProductsViewer(QWidget):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setMinimumSize(800, 600)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def load_data(self):
        conn = sqlite3.connect('eduhub.db')  
        cur = conn.cursor()
        cur.execute(f"SELECT image, product_name, product_price, description FROM {self.table_name}")
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        headers = ["Image", "Name", "Price", "Description"]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                if j == 0:  # Image column
                    pixmap = QPixmap()
                    pixmap.loadFromData(col)  # Load image data into QPixmap
                    scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
                    item = QTableWidgetItem()
                    item.setData(Qt.DecorationRole, scaled_pixmap)
                    
                else:
                    item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)


        conn.close()

if __name__ == '__main__':
    app = QApplication([])
    
    import os
    global pid_entry_data
    pid_entry_data = os.environ.get('PID_ENTRY_DATA')
    table_name = f"sold_products_{pid_entry_data}"
    window = SoldProductsViewer(table_name)
    window.load_data()
    window.setWindowTitle('Product Sold')
    # Increase the font size
    font = window.tableWidget.font()
    font.setPointSize(12)
    window.tableWidget.setFont(font)

    # Apply dark theme
    window.setStyleSheet("""
        QTableWidget {
            background-color: #333;
            color: white;
            alternate-background-color: #444;
            selection-background-color: #666;
        }
        QHeaderView::section {
            background-color: #555;
            color: white;
        }
    """)
    window.show()
    app.exec_()
