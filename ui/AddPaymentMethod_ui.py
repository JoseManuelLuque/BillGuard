# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddPaymentMethod.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddPaymentMethod(object):
    def setupUi(self, AddPaymentMethod):
        if not AddPaymentMethod.objectName():
            AddPaymentMethod.setObjectName(u"AddPaymentMethod")
        AddPaymentMethod.resize(400, 300)
        AddPaymentMethod.setStyleSheet(u"/* Estilo general del fondo */\n"
"QWidget {\n"
"    background-color: #F5F5F5; /* Fondo claro */\n"
"    color: #333333; /* Texto en gris oscuro */\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Estilo de los botones */\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* Verde oscuro */\n"
"    color: #FFFFFF; /* Texto en blanco */\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 14px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Verde m\u00e1s claro al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C; /* Verde m\u00e1s oscuro al presionar */\n"
"}\n"
"\n"
"/* Estilo de los labels */\n"
"QLabel {\n"
"    color: #333333; /* Texto en gris oscuro */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Estilo de los campos de entrada */\n"
"QLineEdit, QDateEdit, QComboBox {\n"
"    "
                        "padding: 5px;\n"
"    border: 1px solid #4CAF50; /* Borde verde oscuro */\n"
"    border-radius: 4px;\n"
"    background-color: #FFFFFF; /* Fondo blanco */\n"
"    color: #333333; /* Texto en gris oscuro */\n"
"}\n"
"\n"
"QLineEdit:focus, QDateEdit:focus, QComboBox:focus {\n"
"    border: 1px solid #45a049; /* Borde verde m\u00e1s claro al enfocar */\n"
"}\n"
"\n"
"/* Estilo de las tablas */\n"
"QTableWidget, QListWidget {\n"
"    border: 1px solid #4CAF50; /* Borde verde oscuro */\n"
"    border-radius: 4px;\n"
"    background-color: #FFFFFF; /* Fondo blanco */\n"
"    color: #333333; /* Texto en gris oscuro */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #4CAF50; /* Fondo verde oscuro */\n"
"    color: #FFFFFF; /* Texto en blanco */\n"
"    padding: 4px;\n"
"    border: 1px solid #3E3E3E; /* Borde oscuro */\n"
"}\n"
"\n"
"/* Estilo de los elementos seleccionados en las tablas */\n"
"QTableWidget::item:selected, QListWidget::item:selected {\n"
"    background-color: #4"
                        "5a049; /* Fondo verde m\u00e1s claro */\n"
"    color: #FFFFFF; /* Texto en blanco */\n"
"}")
        self.verticalLayout = QVBoxLayout(AddPaymentMethod)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutNombre = QHBoxLayout()
        self.horizontalLayoutNombre.setObjectName(u"horizontalLayoutNombre")
        self.labelNombre = QLabel(AddPaymentMethod)
        self.labelNombre.setObjectName(u"labelNombre")

        self.horizontalLayoutNombre.addWidget(self.labelNombre)

        self.inputNombre = QLineEdit(AddPaymentMethod)
        self.inputNombre.setObjectName(u"inputNombre")

        self.horizontalLayoutNombre.addWidget(self.inputNombre)


        self.verticalLayout.addLayout(self.horizontalLayoutNombre)

        self.horizontalLayoutTipo = QHBoxLayout()
        self.horizontalLayoutTipo.setObjectName(u"horizontalLayoutTipo")
        self.labelTipo = QLabel(AddPaymentMethod)
        self.labelTipo.setObjectName(u"labelTipo")

        self.horizontalLayoutTipo.addWidget(self.labelTipo)

        self.comboTipo = QComboBox(AddPaymentMethod)
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.setObjectName(u"comboTipo")

        self.horizontalLayoutTipo.addWidget(self.comboTipo)


        self.verticalLayout.addLayout(self.horizontalLayoutTipo)

        self.horizontalLayoutNumero = QHBoxLayout()
        self.horizontalLayoutNumero.setObjectName(u"horizontalLayoutNumero")
        self.labelNumero = QLabel(AddPaymentMethod)
        self.labelNumero.setObjectName(u"labelNumero")

        self.horizontalLayoutNumero.addWidget(self.labelNumero)

        self.inputNumero = QLineEdit(AddPaymentMethod)
        self.inputNumero.setObjectName(u"inputNumero")

        self.horizontalLayoutNumero.addWidget(self.inputNumero)


        self.verticalLayout.addLayout(self.horizontalLayoutNumero)

        self.horizontalLayoutFechaVencimiento = QHBoxLayout()
        self.horizontalLayoutFechaVencimiento.setObjectName(u"horizontalLayoutFechaVencimiento")
        self.labelFechaVencimiento = QLabel(AddPaymentMethod)
        self.labelFechaVencimiento.setObjectName(u"labelFechaVencimiento")

        self.horizontalLayoutFechaVencimiento.addWidget(self.labelFechaVencimiento)

        self.inputFechaVencimiento = QDateEdit(AddPaymentMethod)
        self.inputFechaVencimiento.setObjectName(u"inputFechaVencimiento")
        self.inputFechaVencimiento.setCalendarPopup(True)

        self.horizontalLayoutFechaVencimiento.addWidget(self.inputFechaVencimiento)


        self.verticalLayout.addLayout(self.horizontalLayoutFechaVencimiento)

        self.btnSave = QPushButton(AddPaymentMethod)
        self.btnSave.setObjectName(u"btnSave")

        self.verticalLayout.addWidget(self.btnSave)


        self.retranslateUi(AddPaymentMethod)

        QMetaObject.connectSlotsByName(AddPaymentMethod)
    # setupUi

    def retranslateUi(self, AddPaymentMethod):
        AddPaymentMethod.setWindowTitle(QCoreApplication.translate("AddPaymentMethod", u"Agregar M\u00e9todo de Pago", None))
        self.labelNombre.setText(QCoreApplication.translate("AddPaymentMethod", u"Nombre:", None))
        self.inputNombre.setPlaceholderText(QCoreApplication.translate("AddPaymentMethod", u"Nombre del M\u00e9todo de Pago", None))
        self.labelTipo.setText(QCoreApplication.translate("AddPaymentMethod", u"Tipo:", None))
        self.comboTipo.setItemText(0, QCoreApplication.translate("AddPaymentMethod", u"Cuenta Bancaria", None))
        self.comboTipo.setItemText(1, QCoreApplication.translate("AddPaymentMethod", u"Tarjeta de D\u00e9bito", None))
        self.comboTipo.setItemText(2, QCoreApplication.translate("AddPaymentMethod", u"Tarjeta de Cr\u00e9dito", None))

        self.labelNumero.setText(QCoreApplication.translate("AddPaymentMethod", u"N\u00famero:", None))
        self.inputNumero.setPlaceholderText(QCoreApplication.translate("AddPaymentMethod", u"N\u00famero del M\u00e9todo de Pago", None))
        self.labelFechaVencimiento.setText(QCoreApplication.translate("AddPaymentMethod", u"Fecha de Vencimiento:", None))
        self.inputFechaVencimiento.setDisplayFormat(QCoreApplication.translate("AddPaymentMethod", u"dd/MM/yyyy", None))
        self.btnSave.setText(QCoreApplication.translate("AddPaymentMethod", u"Guardar", None))
    # retranslateUi

