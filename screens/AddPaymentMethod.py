from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QDate
import sqlite3

class AddPaymentMethod(QDialog):
    def __init__(self, main_app, metodo_pago_id=None):
        super().__init__()
        self.main_app = main_app
        self.metodo_pago_id = metodo_pago_id
        
        # Cargar el archivo .ui generado en Qt Designer
        uic.loadUi("ui/AddPaymentMethod.ui", self)
        
        # Configurar la fecha de vencimiento por defecto
        self.set_default_date()
        
        # Si se proporciona un ID de método de pago, cargar los datos del método de pago
        if self.metodo_pago_id:
            self.load_payment_method_data()
        
        # Conectar el botón de guardar a la función save_payment_method
        self.btnSave.clicked.connect(self.save_payment_method)
        
        # Conectar los campos de entrada a la función de verificación
        self.inputNombre.textChanged.connect(self.check_required_fields)
        self.comboTipo.currentIndexChanged.connect(self.check_required_fields)
        self.inputNumero.textChanged.connect(self.check_required_fields)
        self.inputFechaVencimiento.dateChanged.connect(self.check_required_fields)
        
        # Deshabilitar el botón de guardar por defecto
        self.btnSave.setEnabled(False)
        
    def set_default_date(self):
        # Obtener la fecha actual
        current_date = QDate.currentDate()
        
        # Configurar la fecha de vencimiento como la fecha actual
        self.inputFechaVencimiento.setDate(current_date)
        
        # Configurar el formato de la fecha a DD/MM/AAAA
        self.inputFechaVencimiento.setDisplayFormat("dd/MM/yyyy")
        
    def load_payment_method_data(self):
        conn = sqlite3.connect('billguard.db')
        cursor = conn.cursor()
        
        # Obtener los datos del método de pago
        cursor.execute("SELECT nombre, tipo, numero, fecha_vencimiento FROM metodos_pago WHERE id=?", (self.metodo_pago_id,))
        result = cursor.fetchone()
        if result:
            nombre, tipo, numero, fecha_vencimiento = result
            self.inputNombre.setText(nombre)
            self.comboTipo.setCurrentText(tipo)
            self.inputNumero.setText(numero)
            self.inputFechaVencimiento.setDate(QDate.fromString(fecha_vencimiento, "dd/MM/yyyy"))
        
        conn.close()
        
    def check_required_fields(self):
        if (self.inputNombre.text() and
            self.comboTipo.currentText() and
            self.inputNumero.text() and
            self.inputFechaVencimiento.date().isValid()):
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setEnabled(False)
        
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
        
        if self.metodo_pago_id:
            # Actualizar el método de pago existente
            cursor.execute("""
                UPDATE metodos_pago
                SET nombre=?, tipo=?, numero=?, fecha_vencimiento=?
                WHERE id=? AND usuario_id=?
            """, (nombre, tipo, numero, fecha_vencimiento, self.metodo_pago_id, user_id))
        else:
            # Insertar el nuevo método de pago en la base de datos
            cursor.execute("""
                INSERT INTO metodos_pago (usuario_id, nombre, tipo, numero, fecha_vencimiento)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, nombre, tipo, numero, fecha_vencimiento))
        
        conn.commit()
        conn.close()
        
        QMessageBox.information(self, "Éxito", "Método de pago guardado exitosamente")
        self.close()
        self.main_app.main_window.load_payment_methods()