import sys
from PyQt5 import QtWidgets, QtCore
from gui.main import Ui_Dialog


def create_tree(level: int, branching_factor: int):
    global ui, row_no, column_no
    print("Creating tree... ")
    for x in range(level):
        column_no = 0
        for y in range(branching_factor**x):
            ui.label = QtWidgets.QLabel(ui.frame_tree)
            ui.label.setObjectName("userLabel_" + str(row_no) + str(column_no))
            # Style can be set manually like this or a class can be added
            # ui.label.setStyleSheet("background-color: white;\n"
            #                        "border: 5px solid black;\n"
            #                        "border-radius: 30%;\n"
            #                        "font-size: 45px;\n"
            #                        "padding: 5%;")
            ui.label.setProperty("class", "tree-node")
            ui.label.setAlignment(QtCore.Qt.AlignCenter)
            column_span = branching_factor**(level-1)//(branching_factor**x)
            ui.gridLayout_4.addWidget(ui.label, row_no, column_no * column_span, 1, column_span,
                                      alignment=QtCore.Qt.AlignCenter)
            ui.label.setText(f"({str(row_no)},{str(column_no)})")
            column_no += 1
        row_no += 1
    print("Tree created successfully!")


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

row_no = 0
column_no = 0
ui.button_create_tree.clicked.connect(
    lambda: create_tree(level=int(ui.spinBox_level.text()), branching_factor=int(ui.spinBox_branchingFactor.text())))


Dialog.show()
sys.exit(app.exec_())
