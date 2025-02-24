from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QDate
import sqlite3
from datetime import datetime, timedelta

class AddSubscription(QDialog):
    def __init__(self, main_app, suscripcion_id=None):
        super().__init__()
        self.main_app = main_app
        self.suscripcion_id = suscripcion_id
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/AddSubscription.ui", self)
        
        # Configurar las fechas por defecto
        self.set_default_dates()
        
        # Si se proporciona un ID de suscripción, cargar los datos de la suscripción
        if self.suscripcion_id:
            self.load_subscription_data()
        
        # Conectar el botón de guardar a la función save_subscription
        self.btnSave.clicked.connect(self.save_subscription)
        
    def set_default_dates(self):
        # Obtener la fecha actual
        current_date = QDate.currentDate()
        
        # Configurar la fecha de inicio como la fecha actual
        self.inputFechaInicio.setDate(current_date)
        
        # Configurar la fecha de renovación como un mes después de la fecha actual
        next_month_date = current_date.addMonths(1)
        self.inputFechaRenovacion.setDate(next_month_date)
        
        # Configurar el formato de las fechas a DD/MM/AAAA
        self.inputFechaInicio.setDisplayFormat("dd/MM/yyyy")
        self.inputFechaRenovacion.setDisplayFormat("dd/MM/yyyy")
        
    def load_subscription_data(self):
        conn = sqlite3.connect('billguard.db')
        cursor = conn.cursor()
        
        # Obtener los datos de la suscripción
        cursor.execute("SELECT nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado FROM suscripciones WHERE id=?", (self.suscripcion_id,))
        result = cursor.fetchone()
        if result:
            nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado = result
            self.inputNombreServicio.setText(nombre_servicio)
            self.inputCostoMensual.setText(str(costo_mensual))
            self.inputFechaInicio.setDate(QDate.fromString(fecha_inicio, "dd/MM/yyyy"))
            self.inputFechaRenovacion.setDate(QDate.fromString(fecha_renovacion, "dd/MM/yyyy"))
            self.comboEstado.setCurrentText(estado)
        
        conn.close()
        
    def save_subscription(self):
        nombre_servicio = self.inputNombreServicio.text()
        costo_mensual = self.inputCostoMensual.text()
        fecha_inicio = self.inputFechaInicio.date().toString("dd/MM/yyyy")
        fecha_renovacion = self.inputFechaRenovacion.date().toString("dd/MM/yyyy")
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
        
        if self.suscripcion_id:
            # Actualizar la suscripción existente
            cursor.execute("""
                UPDATE suscripciones
                SET nombre_servicio=?, costo_mensual=?, fecha_inicio=?, fecha_renovacion=?, estado=?
                WHERE id=? AND usuario_id=?
            """, (nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado, self.suscripcion_id, user_id))
        else:
            # Insertar la nueva suscripción en la base de datos
            cursor.execute("""
                INSERT INTO suscripciones (usuario_id, nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, nombre_servicio, costo_mensual, fecha_inicio, fecha_renovacion, estado))
        
        conn.commit()
        conn.close()
        
        QMessageBox.information(self, "Éxito", "Suscripción guardada exitosamente")
        self.close()
        self.main_app.main_window.load_suscripciones()