# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Password_recovery_module.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 387)
        self.Password_recovery = QLabel(Form)
        self.Password_recovery.setObjectName(u"Password_recovery")
        self.Password_recovery.setGeometry(QRect(140, 30, 121, 51))
        font = QFont()
        font.setPointSize(22)
        self.Password_recovery.setFont(font)
        self.label_2_1 = QLabel(Form)
        self.label_2_1.setObjectName(u"label_2_1")
        self.label_2_1.setGeometry(QRect(50, 130, 71, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2_1.setFont(font1)
        self.label_2_2 = QLabel(Form)
        self.label_2_2.setObjectName(u"label_2_2")
        self.label_2_2.setGeometry(QRect(50, 170, 71, 31))
        self.label_2_2.setFont(font1)
        self.EmployeeID = QLineEdit(Form)
        self.EmployeeID.setObjectName(u"EmployeeID")
        self.EmployeeID.setGeometry(QRect(120, 130, 211, 31))
        self.Verification_code = QLineEdit(Form)
        self.Verification_code.setObjectName(u"Verification_code")
        self.Verification_code.setGeometry(QRect(120, 170, 211, 31))
        self.Verification_code.setEchoMode(QLineEdit.EchoMode.Password)
        self.Confirm_password_recovery = QPushButton(Form)
        self.Confirm_password_recovery.setObjectName(u"Confirm_password_recovery")
        self.Confirm_password_recovery.setGeometry(QRect(104, 260, 91, 31))
        self.Confirm_password_recovery.setFont(font1)
        self.Return_to_the_login_page = QPushButton(Form)
        self.Return_to_the_login_page.setObjectName(u"Return_to_the_login_page")
        self.Return_to_the_login_page.setGeometry(QRect(220, 260, 91, 31))
        self.Return_to_the_login_page.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Password_recovery.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u627e\u56de", None))
        self.label_2_1.setText(QCoreApplication.translate("Form", u"\u5de5\u53f7\uff1a", None))
        self.label_2_2.setText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801\uff1a", None))
        self.Confirm_password_recovery.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u627e\u56de", None))
        self.Return_to_the_login_page.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

