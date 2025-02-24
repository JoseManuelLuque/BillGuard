from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
import sqlite3
import json

class RegisterApp(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/Register.ui", self)
        
        # Conectar los botones a funciones
        self.BackButon.clicked.connect(self.go_to_login)
        self.RegisterButtom.clicked.connect(self.register)
        
    def go_to_login(self):
        self.main_app.stack.setCurrentWidget(self.main_app.login_window)

    def register(self):
        usuario = self.UsuarioEdit.text()
        email = self.EmailEdit.text()
        contrasena = self.PasswordEdit.text()
        repetir_contrasena = self.RepeatPasswordEdit.text()
        
        if contrasena != repetir_contrasena:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            return
        
        try:
            # Registrar el usuario en Firebase
            user = self.main_app.auth.create_user_with_email_and_password(email, contrasena)
            
            # Registrar el usuario en la base de datos SQLite
            conn = sqlite3.connect('billguard.db')
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nombre, email, contraseña_hash)
                VALUES (?, ?, ?)
            """, (usuario, email, contrasena))
            conn.commit()
            conn.close()
            
            QMessageBox.information(self, "Éxito", "Usuario registrado exitosamente")
            print(f"Usuario: {usuario}, Email: {email}")
            self.go_to_login()
        except Exception as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            QMessageBox.warning(self, "Error", f"Error al registrar usuario: {error}")