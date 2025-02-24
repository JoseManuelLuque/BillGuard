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
        self.inputNombre.setPlaceholderText(QCoreApplication.translate("AddPaymentMethod", u"Nombre", None))
        self.labelTipo.setText(QCoreApplication.translate("AddPaymentMethod", u"Tipo:", None))
        self.comboTipo.setItemText(0, QCoreApplication.translate("AddPaymentMethod", u"Cuenta bancaria", None))
        self.comboTipo.setItemText(1, QCoreApplication.translate("AddPaymentMethod", u"Tarjeta de cr\u00e9dito", None))
        self.comboTipo.setItemText(2, QCoreApplication.translate("AddPaymentMethod", u"Tarjeta de d\u00e9bito", None))

        self.labelNumero.setText(QCoreApplication.translate("AddPaymentMethod", u"N\u00famero:", None))
        self.inputNumero.setPlaceholderText(QCoreApplication.translate("AddPaymentMethod", u"N\u00famero", None))
        self.labelFechaVencimiento.setText(QCoreApplication.translate("AddPaymentMethod", u"Fecha de Vencimiento:", None))
        self.inputFechaVencimiento.setDisplayFormat(QCoreApplication.translate("AddPaymentMethod", u"dd/MM/yyyy", None))
        self.btnSave.setText(QCoreApplication.translate("AddPaymentMethod", u"Guardar", None))
    # retranslateUi

