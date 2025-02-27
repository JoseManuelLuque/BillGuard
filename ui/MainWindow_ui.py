# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"/* Estilo general del fondo */\n"
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
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSuscripciones = QPushButton(MainWindow)
        self.btnSuscripciones.setObjectName(u"btnSuscripciones")

        self.horizontalLayout.addWidget(self.btnSuscripciones)

        self.btnHistorialPagos = QPushButton(MainWindow)
        self.btnHistorialPagos.setObjectName(u"btnHistorialPagos")

        self.horizontalLayout.addWidget(self.btnHistorialPagos)

        self.btnMetodosPago = QPushButton(MainWindow)
        self.btnMetodosPago.setObjectName(u"btnMetodosPago")

        self.horizontalLayout.addWidget(self.btnMetodosPago)

        self.btnNotificaciones = QPushButton(MainWindow)
        self.btnNotificaciones.setObjectName(u"btnNotificaciones")

        self.horizontalLayout.addWidget(self.btnNotificaciones)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(MainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageSuscripciones = QWidget()
        self.pageSuscripciones.setObjectName(u"pageSuscripciones")
        self.verticalLayout_2 = QVBoxLayout(self.pageSuscripciones)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listSuscripciones = QListWidget(self.pageSuscripciones)
        self.listSuscripciones.setObjectName(u"listSuscripciones")

        self.verticalLayout_2.addWidget(self.listSuscripciones)

        self.btnAgregarSuscripcion = QPushButton(self.pageSuscripciones)
        self.btnAgregarSuscripcion.setObjectName(u"btnAgregarSuscripcion")

        self.verticalLayout_2.addWidget(self.btnAgregarSuscripcion)

        self.btnEliminarSuscripcion = QPushButton(self.pageSuscripciones)
        self.btnEliminarSuscripcion.setObjectName(u"btnEliminarSuscripcion")

        self.verticalLayout_2.addWidget(self.btnEliminarSuscripcion)

        self.btnModificarSuscripcion = QPushButton(self.pageSuscripciones)
        self.btnModificarSuscripcion.setObjectName(u"btnModificarSuscripcion")

        self.verticalLayout_2.addWidget(self.btnModificarSuscripcion)

        self.stackedWidget.addWidget(self.pageSuscripciones)
        self.pageHistorialPagos = QWidget()
        self.pageHistorialPagos.setObjectName(u"pageHistorialPagos")
        self.stackedWidget.addWidget(self.pageHistorialPagos)
        self.pageMetodosPago = QWidget()
        self.pageMetodosPago.setObjectName(u"pageMetodosPago")
        self.verticalLayout_3 = QVBoxLayout(self.pageMetodosPago)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listMetodosPago = QListWidget(self.pageMetodosPago)
        self.listMetodosPago.setObjectName(u"listMetodosPago")

        self.verticalLayout_3.addWidget(self.listMetodosPago)

        self.btnAgregarMetodoPago = QPushButton(self.pageMetodosPago)
        self.btnAgregarMetodoPago.setObjectName(u"btnAgregarMetodoPago")

        self.verticalLayout_3.addWidget(self.btnAgregarMetodoPago)

        self.btnEliminarMetodoPago = QPushButton(self.pageMetodosPago)
        self.btnEliminarMetodoPago.setObjectName(u"btnEliminarMetodoPago")

        self.verticalLayout_3.addWidget(self.btnEliminarMetodoPago)

        self.stackedWidget.addWidget(self.pageMetodosPago)
        self.pageNotificaciones = QWidget()
        self.pageNotificaciones.setObjectName(u"pageNotificaciones")
        self.stackedWidget.addWidget(self.pageNotificaciones)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de Suscripciones", None))
        self.btnSuscripciones.setText(QCoreApplication.translate("MainWindow", u"Suscripciones", None))
        self.btnHistorialPagos.setText(QCoreApplication.translate("MainWindow", u"Historial de Pagos", None))
        self.btnMetodosPago.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todos de Pago", None))
        self.btnNotificaciones.setText(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
        self.btnAgregarSuscripcion.setText(QCoreApplication.translate("MainWindow", u"Agregar Suscripci\u00f3n", None))
        self.btnEliminarSuscripcion.setText(QCoreApplication.translate("MainWindow", u"Eliminar Suscripci\u00f3n", None))
        self.btnModificarSuscripcion.setText(QCoreApplication.translate("MainWindow", u"Modificar Suscripci\u00f3n", None))
        self.btnAgregarMetodoPago.setText(QCoreApplication.translate("MainWindow", u"Agregar M\u00e9todo de Pago", None))
        self.btnEliminarMetodoPago.setText(QCoreApplication.translate("MainWindow", u"Eliminar M\u00e9todo de Pago", None))
    # retranslateUi

