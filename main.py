import sys
import  re

from main_ui import Ui_UserWindow
import main_ui
from PyQt4 import QtCore, QtGui
import connection
from chat_ui import Ui_message_window


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



app = QtGui.QApplication(sys.argv)
UserWindow = QtGui.QMainWindow()
ChatWindow = QtGui.QMainWindow()
client = connection.Connection()
ui = Ui_UserWindow(client)
ui.setupUi(UserWindow)
UserWindow.show()
chat = Ui_message_window(client)
chat.setupUi(ChatWindow)

QtCore.QObject.connect(ui, QtCore.SIGNAL(_fromUtf8("show_chat")),chat.show)


sys.exit(app.exec_())