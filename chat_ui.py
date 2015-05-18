# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_ui.ui'
#
# Created: Sat Apr 25 11:47:45 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from requests.packages.urllib3 import response
import socket
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_message_window(QtCore.QObject):
    def __init__(self, client,parent=None):
        super(Ui_message_window,self).__init__(parent)
        self.client = client
        self.username = ""
        self.contacts = []
        self.chattingwith = ""
    def setupUi(self, message_window):
        self.window = message_window
        message_window.setObjectName(_fromUtf8("message_window"))
        message_window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(message_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 271, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.Personnal_info = QtGui.QGridLayout(self.gridLayoutWidget)
        self.Personnal_info.setMargin(0)
        self.Personnal_info.setObjectName(_fromUtf8("Personnal_info"))
        self.Personnal_friendsonline = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Personnal_friendsonline.setFont(font)
        self.Personnal_friendsonline.setObjectName(_fromUtf8("Personnal_friendsonline"))
        self.Personnal_info.addWidget(self.Personnal_friendsonline, 1, 1, 1, 1)
        self.Personnal_lastname = QtGui.QLabel(self.gridLayoutWidget)
        self.Personnal_lastname.setObjectName(_fromUtf8("Personnal_lastname"))
        self.Personnal_info.addWidget(self.Personnal_lastname, 0, 1, 1, 1)
        self.Personnal_firstname = QtGui.QLabel(self.gridLayoutWidget)
        self.Personnal_firstname.setObjectName(_fromUtf8("Personnal_firstname"))
        self.Personnal_info.addWidget(self.Personnal_firstname, 0, 0, 1, 1)
        self.Personnal_status = QtGui.QLabel(self.gridLayoutWidget)
        self.Personnal_status.setObjectName(_fromUtf8("Personnal_status"))
        self.Personnal_info.addWidget(self.Personnal_status, 1, 0, 1, 1)
        self.search_box = QtGui.QLineEdit(self.centralwidget)
        self.search_box.setGeometry(QtCore.QRect(10, 210, 211, 31))
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.others = QtGui.QLabel(self.centralwidget)
        self.others.setGeometry(QtCore.QRect(8, 175, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setPointSize(15)
        self.others.setFont(font)
        self.others.setObjectName(_fromUtf8("others"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 249, 261, 281))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.contacts_list = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.contacts_list.setMargin(0)
        self.contacts_list.setObjectName(_fromUtf8("contacts_list"))
        self.contact8_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact8_lastname.setText(_fromUtf8(""))
        self.contact8_lastname.setObjectName(_fromUtf8("contact8_lastname"))
        self.contacts_list.addWidget(self.contact8_lastname, 7, 2, 1, 1)
        self.contact2_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact2_firstname.setText(_fromUtf8(""))
        self.contact2_firstname.setObjectName(_fromUtf8("contact2_firstname"))
        self.contacts_list.addWidget(self.contact2_firstname, 1, 1, 1, 1)
        self.contact2_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact2_status.setText(_fromUtf8(""))
        self.contact2_status.setObjectName(_fromUtf8("contact2_status"))
        self.contacts_list.addWidget(self.contact2_status, 1, 0, 1, 1)
        self.contact7_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact7_lastname.setText(_fromUtf8(""))
        self.contact7_lastname.setObjectName(_fromUtf8("contact7_lastname"))
        self.contacts_list.addWidget(self.contact7_lastname, 6, 2, 1, 1)
        self.contact3_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact3_lastname.setText(_fromUtf8(""))
        self.contact3_lastname.setObjectName(_fromUtf8("contact3_lastname"))
        self.contacts_list.addWidget(self.contact3_lastname, 2, 2, 1, 1)
        self.contact4_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact4_firstname.setText(_fromUtf8(""))
        self.contact4_firstname.setObjectName(_fromUtf8("contact4_firstname"))
        self.contacts_list.addWidget(self.contact4_firstname, 3, 1, 1, 1)
        self.contact9_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact9_status.setText(_fromUtf8(""))
        self.contact9_status.setObjectName(_fromUtf8("contact9_status"))
        self.contacts_list.addWidget(self.contact9_status, 8, 0, 1, 1)
        self.contact2_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact2_lastname.setText(_fromUtf8(""))
        self.contact2_lastname.setObjectName(_fromUtf8("contact2_lastname"))
        self.contacts_list.addWidget(self.contact2_lastname, 1, 2, 1, 1)
        self.contact9_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact9_lastname.setText(_fromUtf8(""))
        self.contact9_lastname.setObjectName(_fromUtf8("contact9_lastname"))
        self.contacts_list.addWidget(self.contact9_lastname, 8, 2, 1, 1)
        self.contact3_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact3_status.setText(_fromUtf8(""))
        self.contact3_status.setObjectName(_fromUtf8("contact3_status"))
        self.contacts_list.addWidget(self.contact3_status, 2, 0, 1, 1)
        self.contact8_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact8_firstname.setText(_fromUtf8(""))
        self.contact8_firstname.setObjectName(_fromUtf8("contact8_firstname"))
        self.contacts_list.addWidget(self.contact8_firstname, 7, 1, 1, 1)
        self.contact7_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact7_firstname.setText(_fromUtf8(""))
        self.contact7_firstname.setObjectName(_fromUtf8("contact7_firstname"))
        self.contacts_list.addWidget(self.contact7_firstname, 6, 1, 1, 1)
        self.contact3_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact3_firstname.setText(_fromUtf8(""))
        self.contact3_firstname.setObjectName(_fromUtf8("contact3_firstname"))
        self.contacts_list.addWidget(self.contact3_firstname, 2, 1, 1, 1)
        self.contact5_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact5_firstname.setText(_fromUtf8(""))
        self.contact5_firstname.setObjectName(_fromUtf8("contact5_firstname"))
        self.contacts_list.addWidget(self.contact5_firstname, 4, 1, 1, 1)
        self.contact4_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact4_lastname.setText(_fromUtf8(""))
        self.contact4_lastname.setObjectName(_fromUtf8("contact4_lastname"))
        self.contacts_list.addWidget(self.contact4_lastname, 3, 2, 1, 1)
        self.contact5_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact5_lastname.setText(_fromUtf8(""))
        self.contact5_lastname.setObjectName(_fromUtf8("contact5_lastname"))
        self.contacts_list.addWidget(self.contact5_lastname, 4, 2, 1, 1)
        self.contact6_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact6_firstname.setText(_fromUtf8(""))
        self.contact6_firstname.setObjectName(_fromUtf8("contact6_firstname"))
        self.contacts_list.addWidget(self.contact6_firstname, 5, 1, 1, 1)
        self.contact6_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact6_lastname.setText(_fromUtf8(""))
        self.contact6_lastname.setObjectName(_fromUtf8("contact6_lastname"))
        self.contacts_list.addWidget(self.contact6_lastname, 5, 2, 1, 1)
        self.contact1_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact1_firstname.setText(_fromUtf8(""))
        self.contact1_firstname.setObjectName(_fromUtf8("contact1_firstname"))
        self.contacts_list.addWidget(self.contact1_firstname, 0, 1, 1, 1)
        self.contact1_lastname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact1_lastname.setText(_fromUtf8(""))
        self.contact1_lastname.setObjectName(_fromUtf8("contact1_lastname"))
        self.contacts_list.addWidget(self.contact1_lastname, 0, 2, 1, 1)
        self.contact4_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact4_status.setText(_fromUtf8(""))
        self.contact4_status.setObjectName(_fromUtf8("contact4_status"))
        self.contacts_list.addWidget(self.contact4_status, 3, 0, 1, 1)
        self.contact9_firstname = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact9_firstname.setText(_fromUtf8(""))
        self.contact9_firstname.setObjectName(_fromUtf8("contact9_firstname"))
        self.contacts_list.addWidget(self.contact9_firstname, 8, 1, 1, 1)
        self.contact7_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact7_status.setText(_fromUtf8(""))
        self.contact7_status.setObjectName(_fromUtf8("contact7_status"))
        self.contacts_list.addWidget(self.contact7_status, 6, 0, 1, 1)
        self.contact8_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact8_status.setText(_fromUtf8(""))
        self.contact8_status.setObjectName(_fromUtf8("contact8_status"))
        self.contacts_list.addWidget(self.contact8_status, 7, 0, 1, 1)
        self.contact6_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact6_status.setText(_fromUtf8(""))
        self.contact6_status.setObjectName(_fromUtf8("contact6_status"))
        self.contacts_list.addWidget(self.contact6_status, 5, 0, 1, 1)
        self.contact5_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact5_status.setText(_fromUtf8(""))
        self.contact5_status.setObjectName(_fromUtf8("contact5_status"))
        self.contacts_list.addWidget(self.contact5_status, 4, 0, 1, 1)
        self.contact1_status = QtGui.QLabel(self.gridLayoutWidget_2)
        self.contact1_status.setText(_fromUtf8(""))
        self.contact1_status.setObjectName(_fromUtf8("contact1_status"))
        self.contacts_list.addWidget(self.contact1_status, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(303, 43, 461, 391))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.input_msg =  QtGui.QLineEdit(self.centralwidget)
        self.input_msg.setGeometry(QtCore.QRect(302, 454, 411, 61))
        self.input_msg.setObjectName(_fromUtf8("input_msg"))
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(720, 450, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.currentChat = QtGui.QLabel(self.centralwidget)
        self.currentChat.setGeometry(QtCore.QRect(298, 0, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currentChat.setFont(font)
        self.currentChat.setObjectName(_fromUtf8("currentChat"))
#adding combobox
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 10, 191, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
#end adding combobox
        self.addContactButton = QtGui.QPushButton(self.centralwidget)
        self.addContactButton.setGeometry(QtCore.QRect(230, 210, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addContactButton.setFont(font)
        self.addContactButton.setObjectName(_fromUtf8("addContactButton"))
        message_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(message_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuStatus = QtGui.QMenu(self.menubar)
        self.menuStatus.setObjectName(_fromUtf8("menuStatus"))
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        message_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(message_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        message_window.setStatusBar(self.statusbar)
        self.actionOnline = QtGui.QAction(message_window)
        self.actionOnline.setObjectName(_fromUtf8("actionOnline"))
        self.actionAway = QtGui.QAction(message_window)
        self.actionAway.setObjectName(_fromUtf8("actionAway"))
        self.actionDo_not_disturb = QtGui.QAction(message_window)
        self.actionDo_not_disturb.setObjectName(_fromUtf8("actionDo_not_disturb"))
        self.actionOffline = QtGui.QAction(message_window)
        self.actionOffline.setObjectName(_fromUtf8("actionOffline"))
        self.menuStatus.addAction(self.actionOnline)
        self.menuStatus.addAction(self.actionAway)
        self.menuStatus.addAction(self.actionDo_not_disturb)
        self.menuStatus.addAction(self.actionOffline)
        self.menubar.addAction(self.menuStatus.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())


        self.retranslateUi(message_window)
        QtCore.QMetaObject.connectSlotsByName(message_window)
        self.addContactButton.clicked.connect(self.addcontact)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("activated(const QString&)"), self.changechatcontext)
        self.sendButton.clicked.connect(self.sendmsg)

#adding user information to the interface
#        self.Personnal_firstname.setText("whaaaaaaaatt ?")



    def retranslateUi(self, message_window):
        message_window.setWindowTitle(QtGui.QApplication.translate("message_window", "Chat Window", None, QtGui.QApplication.UnicodeUTF8))
        self.Personnal_friendsonline.setText(QtGui.QApplication.translate("message_window", "online_friends", None, QtGui.QApplication.UnicodeUTF8))
        self.Personnal_lastname.setText(QtGui.QApplication.translate("message_window", "", None, QtGui.QApplication.UnicodeUTF8))
        self.Personnal_firstname.setText(QtGui.QApplication.translate("message_window", "first_name", None, QtGui.QApplication.UnicodeUTF8))
        self.Personnal_status.setText(QtGui.QApplication.translate("message_window", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("message_window", "search a specific contact", None, QtGui.QApplication.UnicodeUTF8))
        self.others.setText(QtGui.QApplication.translate("message_window", "Contacts", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("message_window", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.currentChat.setText(QtGui.QApplication.translate("message_window", "Current chat", None, QtGui.QApplication.UnicodeUTF8))
        self.addContactButton.setText(QtGui.QApplication.translate("message_window", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStatus.setTitle(QtGui.QApplication.translate("message_window", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setTitle(QtGui.QApplication.translate("message_window", "quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOnline.setText(QtGui.QApplication.translate("message_window", "online", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAway.setText(QtGui.QApplication.translate("message_window", "away", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDo_not_disturb.setText(QtGui.QApplication.translate("message_window", "do not disturb", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOffline.setText(QtGui.QApplication.translate("message_window", "offline", None, QtGui.QApplication.UnicodeUTF8))

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

    def show(self):
        self.window.show()
        data = open("/tmp/.aaa","r").read().split("|")
#        print data
        self.Personnal_firstname.setText("<font size='3' color='blue' > " + data[0] + " " + data[1] + "</font>"  )
#        self.Personnal_lastname.setText("   " + data[1])
        self.window.setWindowTitle("Hello "+ data[2])
        self.username = data[2]
        self.Personnal_status.setText("<font size='12' color='green' >  online </font>")
        self.getcontact_info()
        self.communicate()

    def communicate(self):
#        print "time to move to serious stuff ! "
        a=3
        #get list of contact and update the ui

    def addcontact(self):
        text, ok =  QtGui.QInputDialog.getText(None, 'Input Dialog','Enter a valid contact username')
        if ok:
            newname = str(text)
            s= socket.socket()
            s.connect(self.client.remote_address)
            s.send("ADDCONTACT:"+self.encrypt_RSA("server_public.pem",self.username + "|"+ newname)+"\n")
            try :
                response=s.recv(1024)
                if "valid" in response :
                    QtGui.QMessageBox.warning(None, "Warning", response)
                if "already" in response :
                    QtGui.QMessageBox.warning(None, "Warning", response)
                if "success" in response :
                    QtGui.QMessageBox.information(None, "Success", response)

            except:
                pass
        return  ""
    def getcontact_info(self):
        s= socket.socket()
        s.connect(self.client.remote_address)
        s.send("GETCONTACT:"+self.encrypt_RSA("server_public.pem",self.username)+"\n")
        try :
            response=s.recv(1024)
            response = json.loads(response)
            self.contacts = response
            n = len(response)
            self.Personnal_friendsonline.setText("contacts (%s)"  %(str(n)))
            self.updatecontact(response)
        except:
            pass

        return
    def updatecontact(self,response):
        n = len(response)
        if n==1 :
            self.comboBox.addItem(response[0][3])
            self.chattingwith = response[0][3]
            if (response[0][0] == 'online'):
                self.contact1_status.setText("<font style='color: green;background: green;'> </font>")
            else :
                self.contact1_status.setText("<font style='color: red;background: red;'> </font>")
            self.contact1_firstname.setText(response[0][1] + " " + response[0][2])
        if n==2 :
            self.chattingwith = response[0][3]
            self.comboBox.addItem(response[0][3])
            self.comboBox.addItem(response[1][3])
            if (response[0][0] == 'online'):
                self.contact1_status.setText("<font style='color: green;background: green;'>a </font>")
            else :
                self.contact1_status.setText("<font style='color: red;background: red;'>a</font>")
            self.contact1_firstname.setText(response[0][1] + " " + response[0][2])
            self.contact1_firstname.setText(response[0][1]  + " " + response[0][2] )
            if (response[1][0] == 'online'):
                self.contact2_status.setText("<font style='color: green;background: green;'>a</font>")
            else :
                self.contact2_status.setText("<font style='color: red;background: red;'> a</font>")
            self.contact2_firstname.setText(response[1][1]  + " " + response[1][2])
        if n==3 :
            self.chattingwith = response[0][3]
            self.comboBox.addItem(response[0][3])
            self.comboBox.addItem(response[1][3])
            self.comboBox.addItem(response[2][3])
            if (response[0][0] == 'online'):
                self.contact1_status.setText("<font style='color: green;background: green;'>a</font>")
            else :
                self.contact1_status.setText("<font style='color: red;background: red;'>a</font>")
            self.contact1_firstname.setText(response[0][1]  + " " + response[0][2])
            if (response[1][0] == 'online'):
                self.contact2_status.setText("<font style='color: green;background: green;'>a</font>")
            else :
                self.contact2_status.setText("<font style='color: red;background: red;'>a</font>")
            self.contact2_firstname.setText(response[1][1]  + " " + response[1][2])
            if (response[2][0] == 'online'):
                self.contact3_status.setText("<font style='color: green;background: green;'>a</font>")
            else :
                self.contact3_status.setText("<font style='color: red;background: red;'>a</font>")
            self.contact3_firstname.setText(response[2][1]  + " " + response[2][2] )

    def changechatcontext(self):
#        print "change chat context called "
        self.chattingwith = str(self.comboBox.currentText())
        self.currentChat.setText(self.chattingwith)
        s = socket.socket()
        s.connect(self.client.remote_address)
        s.send("GETMSGS:"+self.encrypt_RSA("server_public.pem",self.username+"|"+self.chattingwith)+"\n")
        try :
            print "trying to get %s chat history " %(self.chattingwith)
            response = s.recv(1024)
            if response:
                self.textEdit.clear()
                response = json.loads(response)
#                print response
                for i in response :
                    if (i[0] == self.username):
                        data = "<font color='red' > [%s] </font> %s" % (i[0],i[2])
                    else :
                        data = "<font color='blue'> [%s] </font> %s" % (i[0],i[2])
                    self.textEdit.insertHtml(data)
                    self.textEdit.insertPlainText('\n')
        except:
            pass




    def sendmsg(self):
        if (self.chattingwith == ""):
            QtGui.QMessageBox.warning(None, "Warning", "you need to select a contact in order to send a message")
            return
        if (self.input_msg.text() == ""):
            QtGui.QMessageBox.warning(None, "Warning", "you can't send empty message !")
            return
        message = str(self.input_msg.text() )
        self.textEdit.insertHtml( "<font color='red' > [%s] </font> %s <br>" % (self.username,message))
        data = (self.username + "|" + self.chattingwith + "|" + message).encode('ascii')
       # print "data = %s " %data
#        self.encrypt_RSA("server_public.pem",data)
        s = socket.socket()
        s.connect(self.client.remote_address)
        s.send("NEWMSG:"+self.encrypt_RSA("server_public.pem",data)+"\n")
        try :
            response=s.recv(1024)
            #print response
            if "sent" in response:
                QtGui.QMessageBox.information(None, "Message sent", response)
            else :
                QtGui.QMessageBox.warning(None, "Warning", "could not send message !")

        except:
            pass








if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    message_window = QtGui.QMainWindow()
    ui = Ui_message_window()
    ui.setupUi(message_window)
    message_window.show()
    sys.exit(app.exec_())

