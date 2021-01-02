import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton 
from .Klasse import MeineKlasse

# Subclass QMainWindow to customize your application's main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        
        klasse = MeineKlasse()
        klasse.sayHello()
        
        self.setWindowTitle("My App")        
        button = QPushButton("Press Me!") # Set the central widget of the Window.
        self.setCentralWidget(button)  
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
        
app.exec_()