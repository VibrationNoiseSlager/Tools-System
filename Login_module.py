# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_module.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Confirm_password_recovery(object):
    def setupUi(self, Confirm_password_recovery):
        if not Confirm_password_recovery.objectName():
            Confirm_password_recovery.setObjectName(u"Confirm_password_recovery")
        Confirm_password_recovery.resize(400, 392)
        font = QFont()
        font.setPointSize(14)
        Confirm_password_recovery.setFont(font)
        self.Login = QPushButton(Confirm_password_recovery)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(120, 290, 91, 31))
        self.Login.setFont(font)
        self.Password_recovery = QPushButton(Confirm_password_recovery)
        self.Password_recovery.setObjectName(u"Password_recovery")
        self.Password_recovery.setGeometry(QRect(120, 330, 91, 31))
        self.Password_recovery.setFont(font)
        self.label_1_1 = QLabel(Confirm_password_recovery)
        self.label_1_1.setObjectName(u"label_1_1")
        self.label_1_1.setGeometry(QRect(70, 170, 51, 31))
        self.label_1_1.setFont(font)
        self.label_1_1.setTextFormat(Qt.TextFormat.RichText)
        self.label_1_1.setMargin(0)
        self.label_1_1.setIndent(0)
        self.label_1_2 = QLabel(Confirm_password_recovery)
        self.label_1_2.setObjectName(u"label_1_2")
        self.label_1_2.setGeometry(QRect(70, 220, 51, 21))
        self.label_1_2.setFont(font)
        self.label_1_2.setMargin(0)
        self.EmployeeID = QLineEdit(Confirm_password_recovery)
        self.EmployeeID.setObjectName(u"EmployeeID")
        self.EmployeeID.setGeometry(QRect(120, 170, 211, 31))
        self.Password = QLineEdit(Confirm_password_recovery)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(120, 220, 211, 31))
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(Confirm_password_recovery)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 261, 81))
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.Exit = QPushButton(Confirm_password_recovery)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(230, 290, 91, 31))
        self.Exit.setFont(font)
        self.Change_password = QPushButton(Confirm_password_recovery)
        self.Change_password.setObjectName(u"Change_password")
        self.Change_password.setGeometry(QRect(230, 330, 91, 31))
        self.Change_password.setFont(font)

        self.retranslateUi(Confirm_password_recovery)

        QMetaObject.connectSlotsByName(Confirm_password_recovery)
    # setupUi

    def retranslateUi(self, Confirm_password_recovery):
        Confirm_password_recovery.setWindowTitle(QCoreApplication.translate("Confirm_password_recovery", u"Form", None))
        self.Login.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u767b\u5f55", None))
        self.Password_recovery.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u5bc6\u7801\u627e\u56de", None))
        self.label_1_1.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u5de5\u53f7\uff1a", None))
        self.label_1_2.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u5bc6\u7801\uff1a", None))
        self.label.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u822a\u7a7a\u5200\u5177\u6570\u636e\u5e93\u7cfb\u7edf", None))
        self.Exit.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u9000\u51fa", None))
        self.Change_password.setText(QCoreApplication.translate("Confirm_password_recovery", u"\u4fee\u6539\u5bc6\u7801", None))
    # retranslateUi

