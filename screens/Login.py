from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
import json

class LoginApp(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/Login.ui", self)
        
        # Conectar los botones a funciones
        self.LoginButon.clicked.connect(self.login)
        self.RegisterButtom.clicked.connect(self.go_to_register)
        
    def login(self):
        email = self.EmailEdit.text()
        contrasena = self.PasswordEdit.text()
        
        try:
            user = self.main_app.auth.sign_in_with_email_and_password(email, contrasena)
            QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso")
            print(f"Email: {email}")
            self.main_app.main_window.load_suscripciones()
            self.main_app.stack.setCurrentWidget(self.main_app.main_window)
        except Exception as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            QMessageBox.warning(self, "Error", f"Error al iniciar sesión: {error}")

    def go_to_register(self):
        self.main_app.stack.setCurrentWidget(self.main_app.register_window)