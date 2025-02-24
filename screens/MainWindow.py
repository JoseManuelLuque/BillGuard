from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox
from PyQt6 import uic
import sqlite3
from screens.AddSubscription import AddSubscription
from screens.AddPaymentMethod import AddPaymentMethod

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
        
        # Conectar los botones de agregar, eliminar y modificar suscripción a funciones
        self.btnAgregarSuscripcion.clicked.connect(self.add_subscription)
        self.btnEliminarSuscripcion.clicked.connect(self.delete_subscription)
        self.btnModificarSuscripcion.clicked.connect(self.modify_subscription)
        
        # Conectar los botones de agregar y eliminar método de pago a funciones
        self.btnAgregarMetodoPago.clicked.connect(self.add_payment_method)
        self.btnEliminarMetodoPago.clicked.connect(self.delete_payment_method)
        
        # Deshabilitar los botones de eliminar y modificar por defecto
        self.btnEliminarSuscripcion.setEnabled(False)
        self.btnModificarSuscripcion.setEnabled(False)
        self.btnEliminarMetodoPago.setEnabled(False)
        
        # Conectar la selección de la lista a la función de habilitar botones
        self.listSuscripciones.itemSelectionChanged.connect(self.enable_subscription_buttons)
        self.listMetodosPago.itemSelectionChanged.connect(self.enable_payment_method_buttons)
        
        # Cargar las suscripciones y métodos de pago del usuario
        self.load_suscripciones()
        self.load_payment_methods()
        
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
        cursor.execute("SELECT id, nombre_servicio, costo_mensual, fecha_renovacion FROM suscripciones WHERE usuario_id=?", (user_id,))
        suscripciones = cursor.fetchall()
        
        # Limpiar la lista de suscripciones
        self.listSuscripciones.clear()
        
        # Agregar las suscripciones a la lista
        for suscripcion in suscripciones:
            suscripcion_id, nombre_servicio, costo_mensual, fecha_renovacion = suscripcion
            self.listSuscripciones.addItem(f"{suscripcion_id} - {nombre_servicio} - {costo_mensual}€ - Renovación: {fecha_renovacion}")
        
        conn.close()
        
    def load_payment_methods(self):
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
        
        # Obtener los métodos de pago del usuario
        cursor.execute("SELECT id, nombre, tipo, numero, fecha_vencimiento FROM metodos_pago WHERE usuario_id=?", (user_id,))
        metodos_pago = cursor.fetchall()
        
        # Limpiar la lista de métodos de pago
        self.listMetodosPago.clear()
        
        # Agregar los métodos de pago a la lista
        for metodo_pago in metodos_pago:
            metodo_pago_id, nombre, tipo, numero, fecha_vencimiento = metodo_pago
            self.listMetodosPago.addItem(f"{metodo_pago_id} - {nombre} - {tipo} - {numero} - Vencimiento: {fecha_vencimiento}")
        
        conn.close()
        
    def enable_subscription_buttons(self):
        if self.listSuscripciones.selectedItems():
            self.btnEliminarSuscripcion.setEnabled(True)
            self.btnModificarSuscripcion.setEnabled(True)
        else:
            self.btnEliminarSuscripcion.setEnabled(False)
            self.btnModificarSuscripcion.setEnabled(False)
        
    def enable_payment_method_buttons(self):
        if self.listMetodosPago.selectedItems():
            self.btnEliminarMetodoPago.setEnabled(True)
        else:
            self.btnEliminarMetodoPago.setEnabled(False)
        
    def add_subscription(self):
        self.add_subscription_window = AddSubscription(self.main_app)
        self.add_subscription_window.exec()
        
    def delete_subscription(self):
        selected_item = self.listSuscripciones.currentItem()
        if selected_item:
            suscripcion_id = selected_item.text().split(" - ")[0]
            conn = sqlite3.connect('billguard.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM suscripciones WHERE id=?", (suscripcion_id,))
            conn.commit()
            conn.close()
            self.load_suscripciones()
            QMessageBox.information(self, "Éxito", "Suscripción eliminada exitosamente")
        
    def modify_subscription(self):
        selected_item = self.listSuscripciones.currentItem()
        if selected_item:
            suscripcion_id = selected_item.text().split(" - ")[0]
            self.modify_subscription_window = AddSubscription(self.main_app, suscripcion_id)
            self.modify_subscription_window.exec()
        
    def add_payment_method(self):
        self.add_payment_method_window = AddPaymentMethod(self.main_app)
        self.add_payment_method_window.exec()
        
    def delete_payment_method(self):
        selected_item = self.listMetodosPago.currentItem()
        if selected_item:
            metodo_pago_id = selected_item.text().split(" - ")[0]
            conn = sqlite3.connect('billguard.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM metodos_pago WHERE id=?", (metodo_pago_id,))
            conn.commit()
            conn.close()
            self.load_payment_methods()
            QMessageBox.information(self, "Éxito", "Método de pago eliminado exitosamente")
        
    def show_suscripciones(self):
        self.stackedWidget.setCurrentWidget(self.pageSuscripciones)
        
    def show_historial_pagos(self):
        self.stackedWidget.setCurrentWidget(self.pageHistorialPagos)
        
    def show_metodos_pago(self):
        self.stackedWidget.setCurrentWidget(self.pageMetodosPago)
        
    def show_notificaciones(self):
        self.stackedWidget.setCurrentWidget(self.pageNotificaciones)