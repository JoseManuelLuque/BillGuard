from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
import sqlite3

class AddSubscription(QDialog):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/AddSubscription.ui", self)
        
        # Conectar el botón de guardar a la función save_subscription
        self.btnSave.clicked.connect(self.save_subscription)
        
    def save_subscription(self):
        nombre_servicio = self.inputNombreServicio.text()
        costo_mensual = self.inputCostoMensual.text()
        fecha_inicio = self.inputFechaInicio.text()
        fecha_renovacion = self.inputFechaRenovacion.text()
        estado = self.comboEstado.currentText()
        
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
        
        # Insertar la nueva suscripción en la base de datos
        cursor.execute("""
            INSERT INTO suscripciones (usuario_id, nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado))
        
        conn.commit()
        conn.close()
        
        QMessageBox.information(self, "Éxito", "Suscripción agregada exitosamente")
        self.close()
        self.main_app.main_window.load_suscripciones()