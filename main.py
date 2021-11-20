import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = self.width()
        self.y = self.height()
        self.do_paint = False
        self.magic_button.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.abs_random(qp)
            qp.end()

    def run(self):
        self.do_paint = True
        self.repaint()

    def abs_random(self, qp):
        for i in range(20):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255),
                               randint(0, 255)))
            x_ell = randint(0, self.x)
            y_ell = randint(0, self.y)
            qp.drawEllipse(x_ell, y_ell, x_ell, x_ell)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
