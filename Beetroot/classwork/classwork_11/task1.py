import sys
import numpy as np
from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from main import Ui_MainWindow
from help import Ui_MainWindow



class Figure:
    def __init__(self):
        """Координати фігури"""
        self.figure = np.array([[0, 0, 1],
                                [75, 0, 1],
                                [-25, 25, 1],
                                [50, 25, 1],
                                [-25, 100, 1],
                                [50, 100, 1],
                                [-50, 125, 1],
                                [25, 125, 1]])

        """Матриця перетворення(збільшення/маштабування)"""
        self.scale = lambda x: np.array([[x, 0, 0],
                                         [0, x, 0],
                                         [0, 0, 1]])

        """Виклик бібліотеки для малювання"""
        self.root = Tk()
        self.root.title('octahedron')  # назва вікна
        self.root.geometry('+0+0')

        """Створення полтна на якому буде малюватись фігура"""
        self.canvas = Canvas(self.root, width=500, height=500, background='white')
        self.canvas.pack(fill=BOTH, expand=NO)

    def create_zero_mat(self, m, n):
        return np.zeros(m, n)

    def matrix_multiplication(self, mat1, mat2):
        """Множення двох матриць mat1 на mat2"""
        return np.matmul(mat1, mat2)

    def translate(self, x, y, dx, dy):
        """Зсув кооординати на крок"""
        return x + dx, y + dy

    def draw(self, x, y, scale, visible, unvisible):
        self.canvas.delete(ALL)  # очищення попередніх дій(малювання)
        size = len(self.figure)  # розмірність матриці

        if scale != 0:
            figure = self.matrix_multiplication(self.figure, self.scale(scale))
        else:
            figure = self.figure

        for m in range(size):
            for n in range(m + 1, size):
                if (m, n) not in [(0, 3), (0, 5), (0, 6), (0, 7), (1, 2), (1, 4), (1, 6), (1, 7), (2, 4), (2, 5),
                                  (2, 7), (3, 4), (3, 5), (3, 6), (4, 7), (5, 6)]:
                    if (m, n) in [(0, 4), (4, 5), (4, 6)]:
                        """Перебір координат, малювання ліній між ними і їх зсув від центру координат"""
                        self.canvas.create_line(self.translate(figure[m][0], figure[m][1], x, y),
                                                self.translate(figure[n][0], figure[n][1], x, y),
                                                fill=unvisible, dash=(5, 2))
                    else:
                        self.canvas.create_line(self.translate(figure[m][0], figure[m][1], x, y),
                                                self.translate(figure[n][0], figure[n][1], x, y), fill=visible)

    def main(self, x, y, scale, visible, unvisible):
        self.draw(x, y, scale, visible, unvisible)  # малювання фігури
        mainloop()  # виклик вікна, яке очікує дій користувача


class My_MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.canva = Figure()

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        self.canva.draw(self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(), 'blue', 'red')
        self.spinBox.valueChanged.connect(self.show_result)
        self.spinBox_2.valueChanged.connect(self.show_result)
        self.spinBox_3.valueChanged.connect(self.show_result)
        self.pushButton.clicked.connect(self.show_result)

    def show_result(self):
        self.canva.draw(self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(),
                        self.lineEdit.text(), self.lineEdit_2.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = My_MainWindow()
    ui.setupUi(window)
    window.show()
    mainloop()
    sys.exit(app.exec_())
    # canva = Figure()
    # canva.main(100, 100, 1, 'blue', 'red')
