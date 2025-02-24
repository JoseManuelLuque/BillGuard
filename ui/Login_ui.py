# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 471)
        Login.setMinimumSize(QSize(400, 471))
        Login.setStyleSheet(u"/* Estilo general del fondo */\n"
"QWidget#Login {\n"
"    background-color: #F5F5F5;\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo \"Iniciar Sesi\u00f3n\" */\n"
"QLabel#Loginlabel {\n"
"    background-color: #85BB65;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Estilo de los labels */\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Estilo de los campos de entrada */\n"
"QLineEdit {\n"
"    border: 2px solid #85BB65;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #6FA24C;\n"
"}\n"
"\n"
"/* Estilo de los botones */\n"
"QPushButton {\n"
"    background-color: #85BB65;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6FA24C;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:"
                        " #5C8E3E;\n"
"}")
        self.verticalLayoutWidget = QWidget(Login)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 401, 502))
        self.ColumnaPrincipal = QVBoxLayout(self.verticalLayoutWidget)
        self.ColumnaPrincipal.setSpacing(16)
        self.ColumnaPrincipal.setObjectName(u"ColumnaPrincipal")
        self.ColumnaPrincipal.setContentsMargins(16, 16, 16, 16)
        self.Loginlabel = QLabel(self.verticalLayoutWidget)
        self.Loginlabel.setObjectName(u"Loginlabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Loginlabel.sizePolicy().hasHeightForWidth())
        self.Loginlabel.setSizePolicy(sizePolicy)
        self.Loginlabel.setFrameShape(QFrame.Shape.Box)
        self.Loginlabel.setFrameShadow(QFrame.Shadow.Plain)
        self.Loginlabel.setLineWidth(2)
        self.Loginlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ColumnaPrincipal.addWidget(self.Loginlabel)

        self.Campos = QVBoxLayout()
        self.Campos.setObjectName(u"Campos")
        self.UsuarioLabell = QLabel(self.verticalLayoutWidget)
        self.UsuarioLabell.setObjectName(u"UsuarioLabell")
        sizePolicy.setHeightForWidth(self.UsuarioLabell.sizePolicy().hasHeightForWidth())
        self.UsuarioLabell.setSizePolicy(sizePolicy)

        self.Campos.addWidget(self.UsuarioLabell)

        self.EmailEdit = QLineEdit(self.verticalLayoutWidget)
        self.EmailEdit.setObjectName(u"EmailEdit")

        self.Campos.addWidget(self.EmailEdit)

        self.ContrasnaLabel = QLabel(self.verticalLayoutWidget)
        self.ContrasnaLabel.setObjectName(u"ContrasnaLabel")
        sizePolicy.setHeightForWidth(self.ContrasnaLabel.sizePolicy().hasHeightForWidth())
        self.ContrasnaLabel.setSizePolicy(sizePolicy)
        self.ContrasnaLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.Campos.addWidget(self.ContrasnaLabel)

        self.PasswordEdit = QLineEdit(self.verticalLayoutWidget)
        self.PasswordEdit.setObjectName(u"PasswordEdit")

        self.Campos.addWidget(self.PasswordEdit)


        self.ColumnaPrincipal.addLayout(self.Campos)

        self.Botones = QHBoxLayout()
        self.Botones.setObjectName(u"Botones")
        self.LoginButon = QPushButton(self.verticalLayoutWidget)
        self.LoginButon.setObjectName(u"LoginButon")

        self.Botones.addWidget(self.LoginButon)

        self.RegisterButtom = QPushButton(self.verticalLayoutWidget)
        self.RegisterButtom.setObjectName(u"RegisterButtom")

        self.Botones.addWidget(self.RegisterButtom)


        self.ColumnaPrincipal.addLayout(self.Botones)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.Loginlabel.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n", None))
        self.UsuarioLabell.setText(QCoreApplication.translate("Login", u"Email", None))
        self.ContrasnaLabel.setText(QCoreApplication.translate("Login", u"Conrase\u00f1a", None))
        self.LoginButon.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n", None))
        self.RegisterButtom.setText(QCoreApplication.translate("Login", u"Registrarse", None))
    # retranslateUi

