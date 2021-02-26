import sys
from PyQt5 import QtWidgets
from gui.main import Ui_Dialog


def greet(user_name):
    global ui
    print("Hello", user_name)
    ui.label.setText("Hello, " + user_name)


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

ui.label = QtWidgets.QLabel(ui.layoutWidget)
ui.label.setObjectName("userLabel")
ui.gridLayout.addWidget(ui.label, 1, 0, 1, 3)
ui.pushButton.clicked.connect(lambda: greet(ui.lineEdit.text()))


Dialog.show()
sys.exit(app.exec_())
