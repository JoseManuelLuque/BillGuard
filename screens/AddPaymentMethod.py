from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QDate
import sqlite3

class AddPaymentMethod(QDialog):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/AddPaymentMethod.ui", self)
        
        # Conectar el botón de guardar a la función save_payment_method
        self.btnSave.clicked.connect(self.save_payment_method)
        
    def save_payment_method(self):
        nombre = self.inputNombre.text()
        tipo = self.comboTipo.currentText()
        numero = self.inputNumero.text()
        fecha_vencimiento = self.inputFechaVencimiento.date().toString("dd/MM/yyyy")
        
        user_email = self.main_app.auth.current_user['email']
        conn = sqlite3.connect('billguard.db')
        cursor = conn.cursor()
        
        # Obtener el ID del usuario
        cursor.execute("SELECT id FROM usuarios WHERE email=?", (user_email,))
        result = cursor.fetchone()
        if result is None:
            QMessageBox.warning(self, "Error", "No se encontró el usuario en la base de datos")
            return
        
        user_id = result[0]
        
        # Insertar el nuevo método de pago en la base de datos
        cursor.execute("""
            INSERT INTO metodos_pago (usuario_id, nombre, tipo, numero, fecha_vencimiento)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, nombre, tipo, numero, fecha_vencimiento))
        
        conn.commit()
        conn.close()
        
        QMessageBox.information(self, "Éxito", "Método de pago agregado exitosamente")
        self.close()
        self.main_app.main_window.load_payment_methods()