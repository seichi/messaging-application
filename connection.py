import socket
from PyQt4 import QtCore, QtGui
import string
import random

class  Connection(QtCore.QObject):
    fname = lname = reg_mail = rusername = rpassword =rpassword2 = birthdate = gendre = key_file = ""  # registration value initialisation
    lusername = lpassword =  lcaptcha =""
    remote_address = ("localhost",1337)
#    remote_address = ("192.168.3.223",1337)
#    remote_address = ("192.168.1.4",1337)
    def __init__(self,parent=None):
        super(Connection,self).__init__(parent)
        self.lcaptcha = self.gen_captcha()
        #signals handling here
#        QtCore.QObject.connect(self, QtCore.SIGNAL("tonextwindow"), self.update_client)

    def gen_captcha(self,l=7):
        key =""
        for i in range(l):
            key += random.choice(string.lowercase  + string.digits) #+ string.uppercase
        return key
