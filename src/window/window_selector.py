from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout
from GoWindow.views.base import BaseWindow
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel, 
    QVBoxLayout,
    QPushButton,
)

class SelectButtonWindow(BaseWindow):  # Make sure this inherits from QWidget or the appropriate base class
    def __init__(self, action, text: str, title: str):
        super().__init__(action, title, bg_color="#304463")
        self.text = text
        self.selected_button = None  # Variable to store the clicked button's name
        
        self.title_label = QLabel(self.text)
        self.title_label.setFont(QFont('Times', 18))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setContentsMargins(0, 20, 0, 20)
        
        # Create buttons
        self.button1 = QPushButton("Bently")
        self.button1.setProperty('value','bently')
        self.button2 = QPushButton("Baker")
        self.button2.setProperty('value','baker')
        self.button3 = QPushButton("Bhet")
        self.button3.setProperty('value','bhet')
        
        # Define button styles
        for button in [self.button1, self.button2, self.button3]:
            button.setStyleSheet("""
                QPushButton { background-color: white; color: #1A2130; padding: 10px 20px; border: none; border-radius: 15px; font-size: 16px; min-width: 150px; }
                QPushButton:hover { background-color: #4CAF50; color: white; }
            """)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)  # Add title label to layout
        layout.addWidget(self.button1)  # Add button 1 to layout
        layout.addWidget(self.button2)  # Add button 2 to layout
        layout.addWidget(self.button3)  # Add button 3 to layout
        
        # Connect buttons to actions
        self.button1.clicked.connect(self.button_action)
        self.button2.clicked.connect(self.button_action)
        self.button3.clicked.connect(self.button_action)
        
        self.setLayout(layout)

    def get_selected_button(self):
        return self.value
    
    def button_action(self):
        sender = self.sender()

        if sender:
            self.value = sender.property('value')
            self.action()

class SelectTextWindow2(BaseWindow):  # Make sure this inherits from QWidget or the appropriate base class
    def __init__(self, action, text: str, title: str):
        super().__init__(action, title, bg_color="#304463")
        self.text = text
        self.selected_button = None  # Variable to store the clicked button's name
        
        self.title_label = QLabel(self.text)
        self.title_label.setFont(QFont('Times', 18))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setContentsMargins(0, 20, 0, 20)
        
        # Create buttons
        self.button1 = QPushButton("Pefin")
        self.button1.setProperty('value','pefin')
        self.button2 = QPushButton("Protesto")
        self.button2.setProperty('value','protesto')
        
        # Define button styles
        for button in [self.button1, self.button2]:
            button.setStyleSheet("""
                QPushButton { background-color: white; color: #1A2130; padding: 10px 20px; border: none; border-radius: 15px; font-size: 16px; min-width: 150px; }
                QPushButton:hover { background-color: #4CAF50; color: white; }
            """)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)  # Add title label to layout
        layout.addWidget(self.button1)  # Add button 1 to layout
        layout.addWidget(self.button2)  # Add button 2 to layout
        
        # Connect buttons to actions
        self.button1.clicked.connect(self.button_action)
        self.button2.clicked.connect(self.button_action)
        
        self.setLayout(layout)

    def get_selected_button(self):
        return self.value
    
    def button_action(self):
        sender = self.sender()

        if sender:
            self.value = sender.property('value')
            self.action()
if __name__ == '__main__':
    ...