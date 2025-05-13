# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Password_change_module.ui'
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
        Form.resize(400, 377)
        self.Confirm_password_change = QPushButton(Form)
        self.Confirm_password_change.setObjectName(u"Confirm_password_change")
        self.Confirm_password_change.setGeometry(QRect(90, 300, 91, 31))
        font = QFont()
        font.setPointSize(14)
        self.Confirm_password_change.setFont(font)
        self.Return_to_the_login_page = QPushButton(Form)
        self.Return_to_the_login_page.setObjectName(u"Return_to_the_login_page")
        self.Return_to_the_login_page.setGeometry(QRect(220, 300, 101, 31))
        self.Return_to_the_login_page.setFont(font)
        self.EmployeeID = QLineEdit(Form)
        self.EmployeeID.setObjectName(u"EmployeeID")
        self.EmployeeID.setGeometry(QRect(150, 80, 201, 31))
        self.New_password = QLineEdit(Form)
        self.New_password.setObjectName(u"New_password")
        self.New_password.setGeometry(QRect(150, 120, 201, 31))
        self.label_3_2 = QLabel(Form)
        self.label_3_2.setObjectName(u"label_3_2")
        self.label_3_2.setGeometry(QRect(40, 120, 71, 31))
        self.label_3_2.setFont(font)
        self.label_3_3 = QLabel(Form)
        self.label_3_3.setObjectName(u"label_3_3")
        self.label_3_3.setGeometry(QRect(40, 160, 111, 41))
        self.label_3_3.setFont(font)
        self.Confirm_new_password = QLineEdit(Form)
        self.Confirm_new_password.setObjectName(u"Confirm_new_password")
        self.Confirm_new_password.setGeometry(QRect(150, 170, 201, 31))
        self.label_3_1 = QLabel(Form)
        self.label_3_1.setObjectName(u"label_3_1")
        self.label_3_1.setGeometry(QRect(40, 80, 61, 31))
        self.label_3_1.setFont(font)
        self.label_3_1.setTextFormat(Qt.TextFormat.RichText)
        self.label_3_1.setMargin(0)
        self.label_3_1.setIndent(0)
        self.label_3_4 = QLabel(Form)
        self.label_3_4.setObjectName(u"label_3_4")
        self.label_3_4.setGeometry(QRect(40, 210, 81, 31))
        self.label_3_4.setFont(font)
        self.Verification_code = QLineEdit(Form)
        self.Verification_code.setObjectName(u"Verification_code")
        self.Verification_code.setGeometry(QRect(150, 210, 201, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 121, 41))
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Confirm_password_change.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u4fee\u6539", None))
        self.Return_to_the_login_page.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_3_2.setText(QCoreApplication.translate("Form", u"\u65b0\u5bc6\u7801\uff1a", None))
        self.label_3_3.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u65b0\u5bc6\u7801\uff1a", None))
        self.label_3_1.setText(QCoreApplication.translate("Form", u"\u5de5\u53f7\uff1a", None))
        self.label_3_4.setText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u4fee\u6539", None))
    # retranslateUi

