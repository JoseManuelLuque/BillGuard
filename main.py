import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import pyrebase
from firebase_config import firebase_config
from screens.Login import LoginApp
from screens.Register import RegisterApp
from screens.MainWindow import MainWindow
from database import initialize_database

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # Inicializar Firebase
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.auth = self.firebase.auth()
        
        # Inicializar la base de datos
        initialize_database()
        
        # Cargar las ventanas
        self.login_window = LoginApp(self)
        self.register_window = RegisterApp(self)
        self.main_window = MainWindow(self)
        
        # Agregar las ventanas al stack
        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.register_window)
        self.stack.addWidget(self.main_window)
        
        # Mostrar la ventana de inicio de sesión
        self.stack.setCurrentWidget(self.login_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())