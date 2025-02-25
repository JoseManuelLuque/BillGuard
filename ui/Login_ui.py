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
"/* Estilo del t\u00edtulo de las ventanas */\n"
"QLabel#LoginTitle, QLabel#RegisterT"
                        "itle {\n"
"    background-color: #4CAF50; /* Verde oscuro */\n"
"    color: #FFFFFF; /* Texto en blanco */\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Estilo de los campos de entrada */\n"
"QLineEdit, QDateEdit, QComboBox {\n"
"    padding: 10px;\n"
"    border: 1px solid #4CAF50; /* Borde verde oscuro */\n"
"    border-radius: 4px;\n"
"    background-color: #FFFFFF; /* Fondo blanco */\n"
"    color: #333333; /* Texto en gris oscuro */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus, QDateEdit:focus, QComboBox:focus {\n"
"    border: 1px solid #45a049; /* Borde verde m\u00e1s claro al enfocar */\n"
"}")
        self.ColumnaPrincipal = QVBoxLayout(Login)
        self.ColumnaPrincipal.setSpacing(16)
        self.ColumnaPrincipal.setObjectName(u"ColumnaPrincipal")
        self.ColumnaPrincipal.setContentsMargins(16, 16, 16, 16)
        self.LoginTitle = QLabel(Login)
        self.LoginTitle.setObjectName(u"LoginTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginTitle.sizePolicy().hasHeightForWidth())
        self.LoginTitle.setSizePolicy(sizePolicy)
        self.LoginTitle.setFrameShape(QFrame.Shape.Box)
        self.LoginTitle.setFrameShadow(QFrame.Shadow.Plain)
        self.LoginTitle.setLineWidth(2)
        self.LoginTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ColumnaPrincipal.addWidget(self.LoginTitle)

        self.Campos = QVBoxLayout()
        self.Campos.setObjectName(u"Campos")
        self.UsuarioLabell = QLabel(Login)
        self.UsuarioLabell.setObjectName(u"UsuarioLabell")
        sizePolicy.setHeightForWidth(self.UsuarioLabell.sizePolicy().hasHeightForWidth())
        self.UsuarioLabell.setSizePolicy(sizePolicy)

        self.Campos.addWidget(self.UsuarioLabell)

        self.EmailEdit = QLineEdit(Login)
        self.EmailEdit.setObjectName(u"EmailEdit")

        self.Campos.addWidget(self.EmailEdit)

        self.ContrasnaLabel = QLabel(Login)
        self.ContrasnaLabel.setObjectName(u"ContrasnaLabel")
        sizePolicy.setHeightForWidth(self.ContrasnaLabel.sizePolicy().hasHeightForWidth())
        self.ContrasnaLabel.setSizePolicy(sizePolicy)
        self.ContrasnaLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.Campos.addWidget(self.ContrasnaLabel)

        self.PasswordEdit = QLineEdit(Login)
        self.PasswordEdit.setObjectName(u"PasswordEdit")

        self.Campos.addWidget(self.PasswordEdit)


        self.ColumnaPrincipal.addLayout(self.Campos)

        self.Botones = QHBoxLayout()
        self.Botones.setObjectName(u"Botones")
        self.LoginButon = QPushButton(Login)
        self.LoginButon.setObjectName(u"LoginButon")

        self.Botones.addWidget(self.LoginButon)

        self.RegisterButtom = QPushButton(Login)
        self.RegisterButtom.setObjectName(u"RegisterButtom")

        self.Botones.addWidget(self.RegisterButtom)


        self.ColumnaPrincipal.addLayout(self.Botones)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.LoginTitle.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n", None))
        self.UsuarioLabell.setText(QCoreApplication.translate("Login", u"Email", None))
        self.ContrasnaLabel.setText(QCoreApplication.translate("Login", u"Conrase\u00f1a", None))
        self.LoginButon.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n", None))
        self.RegisterButtom.setText(QCoreApplication.translate("Login", u"Registrarse", None))
    # retranslateUi

