import sys
from PyQt5 import QtWidgets, QtCore
from gui.main import Ui_Dialog


def create_tree(node_name):
    global ui, row_no, column_no
    print("Creating tree for: ", node_name)
    level = 4
    for x in range(level):
        column_no = 0
        for y in range(2**x):
            ui.label = QtWidgets.QLabel(ui.frame_tree)
            ui.label.setObjectName("userLabel_" + str(row_no) + str(column_no))
            column_span = 2**(level-1)//(2**x)
            ui.gridLayout_4.addWidget(ui.label, row_no, column_no * column_span, 1, column_span,
                                      alignment=QtCore.Qt.AlignCenter)
            ui.label.setText("Node name: " + node_name)
            column_no += 1
        row_no += 1


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

row_no = 0
column_no = 0
ui.button_create_tree.clicked.connect(lambda: create_tree(ui.lineEdit_nodeName.text()))


Dialog.show()
sys.exit(app.exec_())
