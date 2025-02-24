from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from PyQt6 import uic
import sqlite3
from screens.AddSubscription import AddSubscription

class MainWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/MainWindow.ui", self)
        
        # Conectar los botones de navegación a funciones
        self.btnSuscripciones.clicked.connect(self.show_suscripciones)
        self.btnHistorialPagos.clicked.connect(self.show_historial_pagos)
        self.btnMetodosPago.clicked.connect(self.show_metodos_pago)
        self.btnNotificaciones.clicked.connect(self.show_notificaciones)
        
        # Conectar el botón de agregar suscripción a la función add_subscription
        self.btnAgregarSuscripcion.clicked.connect(self.add_subscription)
        
    def load_suscripciones(self):
        user_email = self.main_app.auth.current_user['email']
        conn = sqlite3.connect('billguard.db')
        cursor = conn.cursor()
        
        # Obtener el ID del usuario
        cursor.execute("SELECT id FROM usuarios WHERE email=?", (user_email,))
        result = cursor.fetchone()
        if result is None:
            print(f"No se encontró el usuario con el email: {user_email}")
            return
        
        user_id = result[0]
        
        # Obtener las suscripciones del usuario
        cursor.execute("SELECT nombre_servicio, costo_mensual, fecha_renovacion FROM suscripciones WHERE usuario_id=?", (user_id,))
        suscripciones = cursor.fetchall()
        
        # Limpiar la lista de suscripciones
        self.listSuscripciones.clear()
        
        # Agregar las suscripciones a la lista
        for suscripcion in suscripciones:
            nombre_servicio, costo_mensual, fecha_renovacion = suscripcion
            self.listSuscripciones.addItem(f"{nombre_servicio} - {costo_mensual}€ - Renovación: {fecha_renovacion}")
        
        conn.close()
        
    def add_subscription(self):
        self.add_subscription_window = AddSubscription(self.main_app)
        self.add_subscription_window.exec()
        
    def show_suscripciones(self):
        self.stackedWidget.setCurrentWidget(self.pageSuscripciones)
        
    def show_historial_pagos(self):
        self.stackedWidget.setCurrentWidget(self.pageHistorialPagos)
        
    def show_metodos_pago(self):
        self.stackedWidget.setCurrentWidget(self.pageMetodosPago)
        
    def show_notificaciones(self):
        self.stackedWidget.setCurrentWidget(self.pageNotificaciones)