import sys
from view import *
from controller import Controller
from model import evaluateExpression


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

Controller(model=evaluateExpression, view=ui)

sys.exit(app.exec_())
