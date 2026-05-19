import sys
import random
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore, QtWidgets

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yapılacaklar Listesi (To-Do)")
        self.resize(400, 500)
        self.setStyleSheet("background-color: #121212;") 

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        
        self.title_label = QtWidgets.QLabel("Yapılacaklar Listesi", self)
        self.title_label.setStyleSheet("color: #ffffff; font-size: 24px; font-weight: bold; background: transparent;")
        self.main_layout.addWidget(self.title_label)

        
        self.input_layout = QtWidgets.QHBoxLayout()
        self.input_layout.setSpacing(10)

        self.task_input = QtWidgets.QLineEdit(self)
        self.task_input.setPlaceholderText("Yeni bir görev ekleyin...")
        self.task_input.setFixedHeight(40)
        self.task_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #2d2d2d;
                border-radius: 6px;
                padding-left: 10px;
                background-color: #1e1e1e;
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #2ecc71;
            }
        """)
        self.task_input.returnPressed.connect(self.add_task)
        self.input_layout.addWidget(self.task_input)

        self.add_button = QtWidgets.QPushButton("Ekle", self)
        self.add_button.setFixedWidth(70)
        self.add_button.setFixedHeight(40)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }
            QPushButton:pressed {
                background-color: #27ae60;
            }
        """)
        self.add_button.clicked.connect(self.add_task)
        self.input_layout.addWidget(self.add_button)

        self.main_layout.addLayout(self.input_layout)

        
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setStyleSheet("background: transparent;")
        
        self.list_container = QWidget()
        self.list_container.setStyleSheet("background: transparent;")
        self.list_layout = QtWidgets.QVBoxLayout(self.list_container)
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_layout.setSpacing(8)
        
        self.list_layout.addStretch()
        
        self.scroll_area.setWidget(self.list_container)
        self.main_layout.addWidget(self.scroll_area)

    def add_task_widget(self, text):
        task_widget = QWidget()
        task_widget.setFixedHeight(45)
        task_widget.setStyleSheet("background-color: #1e1e1e; border: 1px solid #2d2d2d; border-radius: 6px;")
        
        item_layout = QtWidgets.QHBoxLayout(task_widget)
        item_layout.setContentsMargins(15, 0, 10, 0) # Sol marjı yazı için biraz genişlettim
        item_layout.setSpacing(10)

        
        label = QtWidgets.QLabel(text, task_widget)
        label.setStyleSheet("border: none; background: transparent; color: #ffffff; font-size: 14px;")
        item_layout.addWidget(label, 1)

       
        delete_btn = QtWidgets.QPushButton("✕", task_widget)
        delete_btn.setFixedWidth(30)
        delete_btn.setStyleSheet("""
            QPushButton {
                border: none; 
                background: transparent; 
                color: #666666; 
                font-weight: bold; 
                font-size: 14px;
            }
            QPushButton:hover {
                color: #e74c3c;
            }
        """)
        delete_btn.clicked.connect(lambda: self.delete_task(task_widget))
        item_layout.addWidget(delete_btn)

        self.list_layout.insertWidget(self.list_layout.count() - 1, task_widget)

    def add_task(self):
        text = self.task_input.text().strip()
        if text:
            self.add_task_widget(text)
            self.task_input.clear()

    def delete_task(self, widget):
        self.list_layout.removeWidget(widget)
        widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())
