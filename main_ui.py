# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Tue Jan 13 20:58:57 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import re
import os
import base64
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import chat_ui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_UserWindow(QtCore.QObject):
    def __init__(self, client):
        super(Ui_UserWindow,self).__init__()
        self.client = client
#        print self.client.lcaptcha
    def setupUi(self, UserWindow):
        self.window = UserWindow
        self.show_chat = QtCore.pyqtSignal()
        UserWindow.setObjectName(_fromUtf8("UserWindow"))
        UserWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(UserWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 751, 521))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.regsiter = QtGui.QWidget()
        self.regsiter.setObjectName(_fromUtf8("regsiter"))
        self.layoutWidget = QtGui.QWidget(self.regsiter)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 721, 401))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.key_generation_checkbox = QtGui.QCheckBox(self.layoutWidget)
        self.key_generation_checkbox.setText(_fromUtf8(""))
        self.key_generation_checkbox.setObjectName(_fromUtf8("key_generation_checkbox"))
        self.gridLayout.addWidget(self.key_generation_checkbox, 9, 0, 1, 1)
        self.lname_input = QtGui.QLineEdit(self.layoutWidget)
        self.lname_input.setObjectName(_fromUtf8("lname_input"))
        self.gridLayout.addWidget(self.lname_input, 1, 1, 1, 2)
        self.password_verif_input = QtGui.QLineEdit(self.layoutWidget)
        self.password_verif_input.setObjectName(_fromUtf8("password_verif_input"))
        self.password_verif_input.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout.addWidget(self.password_verif_input, 5, 1, 1, 2)
        self.username_input = QtGui.QLineEdit(self.layoutWidget)
        self.username_input.setObjectName(_fromUtf8("username_input"))
        self.gridLayout.addWidget(self.username_input, 3, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.fname_input = QtGui.QLineEdit(self.layoutWidget)
        self.fname_input.setObjectName(_fromUtf8("fname_input"))
        self.gridLayout.addWidget(self.fname_input, 0, 1, 1, 2)
        self.sex_female_input = QtGui.QCheckBox(self.layoutWidget)
        self.sex_female_input.setObjectName(_fromUtf8("sex_female_input"))
        self.gridLayout.addWidget(self.sex_female_input, 7, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.password_input = QtGui.QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.password_input.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout.addWidget(self.password_input, 4, 1, 1, 2)
        self.file_selection_btn = QtGui.QPushButton(self.layoutWidget)
        self.file_selection_btn.setObjectName(_fromUtf8("file_selection_btn"))
        self.gridLayout.addWidget(self.file_selection_btn, 8, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 9, 1, 1, 2)
        self.public_key_file_input = QtGui.QLineEdit(self.layoutWidget)
        self.public_key_file_input.setEnabled(False)
        self.public_key_file_input.setObjectName(_fromUtf8("public_key_file_input"))
        self.gridLayout.addWidget(self.public_key_file_input, 8, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.sex_male_input = QtGui.QCheckBox(self.layoutWidget)
        self.sex_male_input.setChecked(True)
        self.sex_male_input.setObjectName(_fromUtf8("sex_male_input"))
        self.gridLayout.addWidget(self.sex_male_input, 7, 1, 1, 1)
        self.email_input = QtGui.QLineEdit(self.layoutWidget)
        self.email_input.setText(_fromUtf8(""))
        self.email_input.setObjectName(_fromUtf8("email_input"))
        self.gridLayout.addWidget(self.email_input, 2, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 3, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 3, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 7, 3, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 8, 3, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 9, 3, 1, 1)
        self.birthdate_input = QtGui.QDateEdit(self.layoutWidget)
        self.birthdate_input.setCalendarPopup(True)
        self.birthdate_input.setObjectName(_fromUtf8("birthdate_input"))
        self.gridLayout.addWidget(self.birthdate_input, 6, 1, 1, 2)
        self.splitter_2 = QtGui.QSplitter(self.regsiter)
        self.splitter_2.setGeometry(QtCore.QRect(220, 450, 170, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.register_btn = QtGui.QPushButton(self.splitter_2)
        self.register_btn.setObjectName(_fromUtf8("register_btn"))
        self.cancel_btn = QtGui.QPushButton(self.splitter_2)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.tabWidget.addTab(self.regsiter, _fromUtf8(""))
        self.login = QtGui.QWidget()
        self.login.setObjectName(_fromUtf8("login"))
        self.widget = QtGui.QWidget(self.login)
        self.widget.setGeometry(QtCore.QRect(50, 40, 481, 381))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.username_login_input = QtGui.QLineEdit(self.widget)
        self.username_login_input.setObjectName(_fromUtf8("username_login_input"))
        self.gridLayout_2.addWidget(self.username_login_input, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 2)
        self.password_login_input = QtGui.QLineEdit(self.widget)
        self.password_login_input.setObjectName(_fromUtf8("password_login_input"))
        self.password_login_input.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout_2.addWidget(self.password_login_input, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.captcha_input = QtGui.QLineEdit(self.widget)
        self.captcha_input.setObjectName(_fromUtf8("captcha_input"))
        self.gridLayout_2.addWidget(self.captcha_input, 2, 2, 1, 1)
        self.captcha_field = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("rsfs10"))
        font.setPointSize(22)
        font.setItalic(True)
        self.captcha_field.setFont(font)
        self.captcha_field.setAutoFillBackground(False)
        self.captcha_field.setObjectName(_fromUtf8("captcha_field"))
        self.gridLayout_2.addWidget(self.captcha_field, 3, 1, 1, 2)
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout_2.addWidget(self.toolButton, 3, 3, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 0, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 1, 3, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 2, 3, 1, 1)
        self.splitter = QtGui.QSplitter(self.login)
        self.splitter.setGeometry(QtCore.QRect(160, 450, 336, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.login_btn = QtGui.QPushButton(self.splitter)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.password_reset_btn = QtGui.QPushButton(self.splitter)
        self.password_reset_btn.setObjectName(_fromUtf8("password_reset_btn"))
        self.cancel_login_btn = QtGui.QPushButton(self.splitter)
        self.cancel_login_btn.setObjectName(_fromUtf8("cancel_login_btn"))
        self.tabWidget.addTab(self.login, _fromUtf8(""))
        UserWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(UserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        UserWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(UserWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        UserWindow.setStatusBar(self.statusbar)
        self.actionMinimize = QtGui.QAction(UserWindow)
        self.actionMinimize.setObjectName(_fromUtf8("actionMinimize"))
        self.actionFull_screen = QtGui.QAction(UserWindow)
        self.actionFull_screen.setObjectName(_fromUtf8("actionFull_screen"))
        self.actionWhat_s_this = QtGui.QAction(UserWindow)
        self.actionWhat_s_this.setObjectName(_fromUtf8("actionWhat_s_this"))
        self.actionWho_are_We = QtGui.QAction(UserWindow)
        self.actionWho_are_We.setObjectName(_fromUtf8("actionWho_are_We"))
        self.actionClose = QtGui.QAction(UserWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionOpen_new_window = QtGui.QAction(UserWindow)
        self.actionOpen_new_window.setObjectName(_fromUtf8("actionOpen_new_window"))
        self.menuFile.addAction(self.actionOpen_new_window)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionWhat_s_this)
        self.menuHelp.addAction(self.actionWho_are_We)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionFull_screen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(UserWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.sex_female_input, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sex_male_input.toggle)
        QtCore.QObject.connect(self.sex_male_input, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sex_female_input.toggle)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fname_input.clear)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lname_input.clear)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.username_input.clear)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.password_input.clear)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.password_verif_input.clear)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.email_input.clear)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.public_key_file_input.clear)
        QtCore.QObject.connect(self.cancel_login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.username_login_input.clear)
        QtCore.QObject.connect(self.cancel_login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.password_login_input.clear)
        QtCore.QObject.connect(self.cancel_login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.captcha_input.clear)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)
        UserWindow.setTabOrder(self.tabWidget, self.fname_input)
        UserWindow.setTabOrder(self.fname_input, self.lname_input)
        UserWindow.setTabOrder(self.lname_input, self.email_input)
        UserWindow.setTabOrder(self.email_input, self.username_input)
        UserWindow.setTabOrder(self.username_input, self.password_input)
        UserWindow.setTabOrder(self.password_input, self.password_verif_input)
        UserWindow.setTabOrder(self.password_verif_input, self.birthdate_input)
        UserWindow.setTabOrder(self.birthdate_input, self.sex_male_input)
        UserWindow.setTabOrder(self.sex_male_input, self.sex_female_input)
        UserWindow.setTabOrder(self.sex_female_input, self.public_key_file_input)
        UserWindow.setTabOrder(self.public_key_file_input, self.file_selection_btn)
        UserWindow.setTabOrder(self.file_selection_btn, self.key_generation_checkbox)
        UserWindow.setTabOrder(self.key_generation_checkbox, self.register_btn)
        UserWindow.setTabOrder(self.register_btn, self.cancel_btn)
        UserWindow.setTabOrder(self.cancel_btn, self.username_login_input)
        UserWindow.setTabOrder(self.username_login_input, self.password_login_input)
        UserWindow.setTabOrder(self.password_login_input, self.captcha_input)
        UserWindow.setTabOrder(self.captcha_input, self.toolButton)
        UserWindow.setTabOrder(self.toolButton, self.login_btn)
        UserWindow.setTabOrder(self.login_btn, self.password_reset_btn)
        UserWindow.setTabOrder(self.password_reset_btn, self.cancel_login_btn)

# Button's Action
        self.captcha_field.setText( QtCore.QString( self.client.lcaptcha))
        self.toolButton.clicked.connect(self.gen_new_captcha)
        self.file_selection_btn.clicked.connect(self.select_file)
        self.register_btn.clicked.connect(self.get_registration_input)
        self.login_btn.clicked.connect(self.get_login_input)
        self.password_reset_btn.clicked.connect(self.password_reset)

    def retranslateUi(self, UserWindow):
        UserWindow.setWindowTitle(QtGui.QApplication.translate("UserWindow", "Secure mail transfert application", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("UserWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("UserWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("UserWindow", "Retype password", None, QtGui.QApplication.UnicodeUTF8))
        self.sex_female_input.setText(QtGui.QApplication.translate("UserWindow", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("UserWindow", "Sex", None, QtGui.QApplication.UnicodeUTF8))
        self.file_selection_btn.setText(QtGui.QApplication.translate("UserWindow", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("UserWindow", "Last name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("UserWindow", "i have no key , generate one for me please", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("UserWindow", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("UserWindow", "First name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("UserWindow", "Birthdate ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("UserWindow", "Public Key", None, QtGui.QApplication.UnicodeUTF8))
        self.sex_male_input.setText(QtGui.QApplication.translate("UserWindow", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.birthdate_input.setDisplayFormat(QtGui.QApplication.translate("UserWindow", "dd/M/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.register_btn.setText(QtGui.QApplication.translate("UserWindow", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("UserWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.regsiter), QtGui.QApplication.translate("UserWindow", "register ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("UserWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("UserWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("UserWindow", "Captcha", None, QtGui.QApplication.UnicodeUTF8))
        self.captcha_field.setText(QtGui.QApplication.translate("UserWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("UserWindow", "new", None, QtGui.QApplication.UnicodeUTF8))
        self.login_btn.setText(QtGui.QApplication.translate("UserWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.password_reset_btn.setText(QtGui.QApplication.translate("UserWindow", "Forgot your password ?", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_login_btn.setText(QtGui.QApplication.translate("UserWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QtGui.QApplication.translate("UserWindow", "login    ", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("UserWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("UserWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindow.setTitle(QtGui.QApplication.translate("UserWindow", "Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMinimize.setText(QtGui.QApplication.translate("UserWindow", "Minimize", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFull_screen.setText(QtGui.QApplication.translate("UserWindow", "Full screen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWhat_s_this.setText(QtGui.QApplication.translate("UserWindow", "What\'s this", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWho_are_We.setText(QtGui.QApplication.translate("UserWindow", "Who are We ?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("UserWindow", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_new_window.setText(QtGui.QApplication.translate("UserWindow", "open new window", None, QtGui.QApplication.UnicodeUTF8))
    def show(self):
        self.window.show()
    def hide(self):
        self.window.hide()


    def encrypt_RSA(self,public_key_loc, message):
        key = open(public_key_loc, "r").read()
        nb_chunks = len(message) / 200
        chunks = []
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        for i in range(nb_chunks+1):
            encrypted = rsakey.encrypt(message[i*200:(i+1)*200])
            chunks.append(encrypted.encode('base64').rstrip())
        encrypted = rsakey.encrypt(message[(nb_chunks+1)*200:])
        chunks.append(encrypted.encode('base64').rstrip())
#        return encrypted.encode('base64')
        return "-".join(chunks)

    def decrypt_RSA(self,private_key_loc, message):

        key = open(private_key_loc, "r").read()
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        chunks = message.split("-")
        plain = []
        for i in range(len(chunks)):
            decrypted = rsakey.decrypt(b64decode(chunks[i].rstrip()))
            plain.append(decrypted)
        return  "".join(plain)
#        return decrypted



    def select_file(self):
    	self.public_key_file_input.setText(QtGui.QFileDialog.getOpenFileName())

    def get_registration_input(self):
        if ((self.fname_input.text()) and re.match('^[\w-]+$', self.fname_input.text().replace(" ","")) ):
            self.client.fname = str(self.fname_input.text())
        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid first name")
            return
        if ((self.lname_input.text()) and re.match('^[\w-]+$', self.lname_input.text().replace(" ","")) ):
            self.client.lname = str(self.lname_input.text())
        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid last name")
            return
        if ((self.username_input.text()) and re.match('^[\w-]+$', self.username_input.text()) ):
            self.client.rusername = str(self.username_input.text())
        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid username")
            return
        if ((self.password_input.text()) and re.match('^[\w-]+$', self.password_input.text()) ):
            self.client.rpassword = str(self.password_input.text())
        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid password")
            return
        if ( self.password_input.text()  != self.password_verif_input.text() ):
            self.client.rpassword = ""
            QtGui.QMessageBox.warning(None, "Warning", "password mismatch")
            return
        if ((self.email_input.text()) and re.match('^[\w.-]+@[\w.-]+.\w+$', self.email_input.text()) ):
            self.client.reg_email = str(self.email_input.text())

        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid email address")
            return

        if (self.sex_female_input.isChecked()):
            self.client.gendre = "F"
        else :
            self.client.gendre = "M"

        self.client.birthdate = str(self.birthdate_input.text())
        # key pairs generation to be done
        if ( not(self.key_generation_checkbox.isChecked()) and  (self.public_key_file_input.text() == "")):
            QtGui.QMessageBox.warning(None, "Warning", "you must specify your public key , if you don't have one please check the checkbox below")
            return

        if ((self.key_generation_checkbox.isChecked()) and  (self.public_key_file_input.text() == "")):
            os.system("mkdir keys")
            os.system("openssl genrsa  -out keys/private.pem 2048")
            os.system("openssl rsa -in keys/private.pem -outform PEM -pubout -out keys/public.pem")
            self.client.key_file= "keys/public.pem"
            self.public_key_file_input.setText("keys/public.pem")
        key_content = open(str(self.public_key_file_input.text()),"r").read()
        if "BEGIN PUBLIC KEY" not in key_content :
            QtGui.QMessageBox.warning(None, "Warning", "Non valid public key file")
            return

        # if everything went right , we return the input serialized
        ret = self.client.fname + "|"+self.client.lname + "|" + self.client.reg_email + "|" + self.client.rusername + "|" + self.client.rpassword + "|"
        ret += self.client.birthdate + "|" + self.client.gendre + "|" + key_content
        test = self.encrypt_RSA("server_public.pem",ret)
        s= socket.socket()
        s.connect(self.client.remote_address)
        s.send("REGISTER:"+test+"\n")
        try :
            response=s.recv(1024)
            if "use" in response :
                QtGui.QMessageBox.warning(None, "Warning", response)
            else:
                QtGui.QMessageBox.information(None, "Registration Successful", response)
        except :
            pass
        return ret


    def gen_new_captcha(self):
        self.client.lcaptcha = self.client.gen_captcha()
        self.captcha_field.setText(self.client.lcaptcha)
        self.captcha_input.clear()

    def get_login_input(self):
        if ((self.username_login_input.text()) and re.match('^[\w-]+$', self.username_login_input.text()) ):
            self.client.lusername = str(self.username_login_input.text())
        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid username")
            return
        if ((self.password_login_input.text()) and re.match('^[\w-]+$', self.password_login_input.text()) ):
            self.client.lpassword = str(self.password_login_input.text())
        else :
            QtGui.QMessageBox.warning(None, "Warning", "non valid password")
            return
        if ( (self.captcha_input.text()) and  (self.captcha_input.text() == self.client.lcaptcha )):
            pass
        else:
            QtGui.QMessageBox.warning(None, "Warning", "Wrong captcha ")
            return
        ret = self.client.lusername + "|" + self.client.lpassword
        test = self.encrypt_RSA("server_public.pem",ret)
        s= socket.socket()
        s.connect(self.client.remote_address)
        s.send("LOGIN:"+test+"\n")
        try :
            response=s.recv(1024)
            print response
            if "no such" in response :
                QtGui.QMessageBox.warning(None, "Warning", response)
            else :
                QtGui.QMessageBox.information(None, "Login Successful", response)
                open("/tmp/.aaa","w").write(response.replace("Welcome ","").replace(" ","|").strip()  + self.client.lusername )
                self.emit(QtCore.SIGNAL("show_chat"))
                self.window.hide()
#                print "testing .. "
#                print dir(self.chat)

        except :
            pass
        return ret

    def password_reset(self):
        text, ok =  QtGui.QInputDialog.getText(None, 'Input Dialog','Enter your email address:')
        if ok:
            mail = str(text)
            if (re.match('^[\w.-]+@[\w.-]+.\w+$', mail)):
                QtGui.QMessageBox.information(None, 'Request sent', ''' you should receive a mail containing your password shortly ''',QtGui.QMessageBox.Ok)
            else :
                QtGui.QMessageBox.warning(None, "Warning", "non valid email address")
                return
            s= socket.socket()
            s.connect(self.client.remote_address)
            s.send("RESET:"+self.encrypt_RSA("server_public.pem",mail)+"\n")







if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UserWindow = QtGui.QMainWindow()
    ui = Ui_UserWindow()
    ui.setupUi(UserWindow)
    UserWindow.show()
    sys.exit(app.exec_())

