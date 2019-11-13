import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def run(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = choice(list(range(50, 300)))
        qp.drawEllipse(300, 300, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
