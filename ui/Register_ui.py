# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(400, 471)
        Register.setMinimumSize(QSize(400, 471))
        Register.setStyleSheet(u"/* Estilo general del fondo */\n"
"QWidget#Register {\n"
"    background-color: #F5F5F5;\n"
"}\n"
"\n"
"/* Estilo del t\u00edtulo \"Registrarse\" */\n"
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
"    background-color: #5C8"
                        "E3E;\n"
"}")
        self.ColumnaPrincipal = QVBoxLayout(Register)
        self.ColumnaPrincipal.setSpacing(16)
        self.ColumnaPrincipal.setObjectName(u"ColumnaPrincipal")
        self.ColumnaPrincipal.setContentsMargins(16, 16, 16, 16)
        self.Loginlabel = QLabel(Register)
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
        self.UsuarioLabell = QLabel(Register)
        self.UsuarioLabell.setObjectName(u"UsuarioLabell")
        sizePolicy.setHeightForWidth(self.UsuarioLabell.sizePolicy().hasHeightForWidth())
        self.UsuarioLabell.setSizePolicy(sizePolicy)

        self.Campos.addWidget(self.UsuarioLabell)

        self.UsuarioEdit = QLineEdit(Register)
        self.UsuarioEdit.setObjectName(u"UsuarioEdit")

        self.Campos.addWidget(self.UsuarioEdit)

        self.EmailLabel = QLabel(Register)
        self.EmailLabel.setObjectName(u"EmailLabel")
        sizePolicy.setHeightForWidth(self.EmailLabel.sizePolicy().hasHeightForWidth())
        self.EmailLabel.setSizePolicy(sizePolicy)

        self.Campos.addWidget(self.EmailLabel)

        self.EmailEdit = QLineEdit(Register)
        self.EmailEdit.setObjectName(u"EmailEdit")

        self.Campos.addWidget(self.EmailEdit)

        self.ContrasnaLabel = QLabel(Register)
        self.ContrasnaLabel.setObjectName(u"ContrasnaLabel")
        sizePolicy.setHeightForWidth(self.ContrasnaLabel.sizePolicy().hasHeightForWidth())
        self.ContrasnaLabel.setSizePolicy(sizePolicy)
        self.ContrasnaLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.Campos.addWidget(self.ContrasnaLabel)

        self.PasswordEdit = QLineEdit(Register)
        self.PasswordEdit.setObjectName(u"PasswordEdit")

        self.Campos.addWidget(self.PasswordEdit)

        self.RepeatPassword = QLabel(Register)
        self.RepeatPassword.setObjectName(u"RepeatPassword")
        sizePolicy.setHeightForWidth(self.RepeatPassword.sizePolicy().hasHeightForWidth())
        self.RepeatPassword.setSizePolicy(sizePolicy)
        self.RepeatPassword.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.Campos.addWidget(self.RepeatPassword)

        self.RepeatPasswordEdit = QLineEdit(Register)
        self.RepeatPasswordEdit.setObjectName(u"RepeatPasswordEdit")

        self.Campos.addWidget(self.RepeatPasswordEdit)


        self.ColumnaPrincipal.addLayout(self.Campos)

        self.Botones = QHBoxLayout()
        self.Botones.setObjectName(u"Botones")
        self.BackButon = QPushButton(Register)
        self.BackButon.setObjectName(u"BackButon")

        self.Botones.addWidget(self.BackButon)

        self.RegisterButtom = QPushButton(Register)
        self.RegisterButtom.setObjectName(u"RegisterButtom")

        self.Botones.addWidget(self.RegisterButtom)


        self.ColumnaPrincipal.addLayout(self.Botones)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Form", None))
        self.Loginlabel.setText(QCoreApplication.translate("Register", u"Registrarse", None))
        self.UsuarioLabell.setText(QCoreApplication.translate("Register", u"Usuario", None))
        self.EmailLabel.setText(QCoreApplication.translate("Register", u"Email", None))
        self.ContrasnaLabel.setText(QCoreApplication.translate("Register", u"Conrase\u00f1a", None))
        self.RepeatPassword.setText(QCoreApplication.translate("Register", u"Repetir Conrase\u00f1a", None))
        self.BackButon.setText(QCoreApplication.translate("Register", u"Volver", None))
        self.RegisterButtom.setText(QCoreApplication.translate("Register", u"Registrarse", None))
    # retranslateUi

