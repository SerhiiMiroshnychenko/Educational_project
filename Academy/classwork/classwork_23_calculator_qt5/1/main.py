import sys
from view import *
from controler import CalculatorController
from model import evaluateExpression


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    CalculatorController(model=evaluateExpression, view=ui)

    sys.exit(app.exec_())

# auto-py-to-exe
