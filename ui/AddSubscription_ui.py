# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddSubscription.ui'
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

class Ui_AddSubscription(object):
    def setupUi(self, AddSubscription):
        if not AddSubscription.objectName():
            AddSubscription.setObjectName(u"AddSubscription")
        AddSubscription.resize(400, 300)
        AddSubscription.setStyleSheet(u"/* Estilo general del fondo */\n"
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
        self.verticalLayout = QVBoxLayout(AddSubscription)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutNombreServicio = QHBoxLayout()
        self.horizontalLayoutNombreServicio.setObjectName(u"horizontalLayoutNombreServicio")
        self.labelNombreServicio = QLabel(AddSubscription)
        self.labelNombreServicio.setObjectName(u"labelNombreServicio")

        self.horizontalLayoutNombreServicio.addWidget(self.labelNombreServicio)

        self.inputNombreServicio = QLineEdit(AddSubscription)
        self.inputNombreServicio.setObjectName(u"inputNombreServicio")

        self.horizontalLayoutNombreServicio.addWidget(self.inputNombreServicio)


        self.verticalLayout.addLayout(self.horizontalLayoutNombreServicio)

        self.horizontalLayoutCostoMensual = QHBoxLayout()
        self.horizontalLayoutCostoMensual.setObjectName(u"horizontalLayoutCostoMensual")
        self.labelCostoMensual = QLabel(AddSubscription)
        self.labelCostoMensual.setObjectName(u"labelCostoMensual")

        self.horizontalLayoutCostoMensual.addWidget(self.labelCostoMensual)

        self.inputCostoMensual = QLineEdit(AddSubscription)
        self.inputCostoMensual.setObjectName(u"inputCostoMensual")

        self.horizontalLayoutCostoMensual.addWidget(self.inputCostoMensual)


        self.verticalLayout.addLayout(self.horizontalLayoutCostoMensual)

        self.horizontalLayoutFechaInicio = QHBoxLayout()
        self.horizontalLayoutFechaInicio.setObjectName(u"horizontalLayoutFechaInicio")
        self.labelFechaInicio = QLabel(AddSubscription)
        self.labelFechaInicio.setObjectName(u"labelFechaInicio")

        self.horizontalLayoutFechaInicio.addWidget(self.labelFechaInicio)

        self.inputFechaInicio = QDateEdit(AddSubscription)
        self.inputFechaInicio.setObjectName(u"inputFechaInicio")
        self.inputFechaInicio.setCalendarPopup(True)

        self.horizontalLayoutFechaInicio.addWidget(self.inputFechaInicio)


        self.verticalLayout.addLayout(self.horizontalLayoutFechaInicio)

        self.horizontalLayoutFechaRenovacion = QHBoxLayout()
        self.horizontalLayoutFechaRenovacion.setObjectName(u"horizontalLayoutFechaRenovacion")
        self.labelFechaRenovacion = QLabel(AddSubscription)
        self.labelFechaRenovacion.setObjectName(u"labelFechaRenovacion")

        self.horizontalLayoutFechaRenovacion.addWidget(self.labelFechaRenovacion)

        self.inputFechaRenovacion = QDateEdit(AddSubscription)
        self.inputFechaRenovacion.setObjectName(u"inputFechaRenovacion")
        self.inputFechaRenovacion.setCalendarPopup(True)

        self.horizontalLayoutFechaRenovacion.addWidget(self.inputFechaRenovacion)


        self.verticalLayout.addLayout(self.horizontalLayoutFechaRenovacion)

        self.horizontalLayoutEstado = QHBoxLayout()
        self.horizontalLayoutEstado.setObjectName(u"horizontalLayoutEstado")
        self.labelEstado = QLabel(AddSubscription)
        self.labelEstado.setObjectName(u"labelEstado")

        self.horizontalLayoutEstado.addWidget(self.labelEstado)

        self.comboEstado = QComboBox(AddSubscription)
        self.comboEstado.addItem("")
        self.comboEstado.addItem("")
        self.comboEstado.addItem("")
        self.comboEstado.setObjectName(u"comboEstado")

        self.horizontalLayoutEstado.addWidget(self.comboEstado)


        self.verticalLayout.addLayout(self.horizontalLayoutEstado)

        self.horizontalLayoutMetodoPago = QHBoxLayout()
        self.horizontalLayoutMetodoPago.setObjectName(u"horizontalLayoutMetodoPago")
        self.labelMetodoPago = QLabel(AddSubscription)
        self.labelMetodoPago.setObjectName(u"labelMetodoPago")

        self.horizontalLayoutMetodoPago.addWidget(self.labelMetodoPago)

        self.comboMetodoPago = QComboBox(AddSubscription)
        self.comboMetodoPago.setObjectName(u"comboMetodoPago")

        self.horizontalLayoutMetodoPago.addWidget(self.comboMetodoPago)


        self.verticalLayout.addLayout(self.horizontalLayoutMetodoPago)

        self.btnSave = QPushButton(AddSubscription)
        self.btnSave.setObjectName(u"btnSave")

        self.verticalLayout.addWidget(self.btnSave)


        self.retranslateUi(AddSubscription)

        QMetaObject.connectSlotsByName(AddSubscription)
    # setupUi

    def retranslateUi(self, AddSubscription):
        AddSubscription.setWindowTitle(QCoreApplication.translate("AddSubscription", u"Agregar Suscripci\u00f3n", None))
        self.labelNombreServicio.setText(QCoreApplication.translate("AddSubscription", u"Nombre del Servicio:", None))
        self.inputNombreServicio.setPlaceholderText(QCoreApplication.translate("AddSubscription", u"Nombre del Servicio", None))
        self.labelCostoMensual.setText(QCoreApplication.translate("AddSubscription", u"Costo Mensual:", None))
        self.inputCostoMensual.setPlaceholderText(QCoreApplication.translate("AddSubscription", u"Costo Mensual", None))
        self.labelFechaInicio.setText(QCoreApplication.translate("AddSubscription", u"Fecha de Inicio:", None))
        self.inputFechaInicio.setDisplayFormat(QCoreApplication.translate("AddSubscription", u"dd/MM/yyyy", None))
        self.labelFechaRenovacion.setText(QCoreApplication.translate("AddSubscription", u"Fecha de Renovaci\u00f3n:", None))
        self.inputFechaRenovacion.setDisplayFormat(QCoreApplication.translate("AddSubscription", u"dd/MM/yyyy", None))
        self.labelEstado.setText(QCoreApplication.translate("AddSubscription", u"Estado:", None))
        self.comboEstado.setItemText(0, QCoreApplication.translate("AddSubscription", u"Activo", None))
        self.comboEstado.setItemText(1, QCoreApplication.translate("AddSubscription", u"Pausado", None))
        self.comboEstado.setItemText(2, QCoreApplication.translate("AddSubscription", u"Cancelado", None))

        self.labelMetodoPago.setText(QCoreApplication.translate("AddSubscription", u"M\u00e9todo de Pago:", None))
        self.btnSave.setText(QCoreApplication.translate("AddSubscription", u"Guardar", None))
    # retranslateUi

