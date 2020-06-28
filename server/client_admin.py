import sys
from PyQt5 import QtWidgets
import design
from controller import Controller
control = Controller()


class MyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.params = []
        self.pushButton.clicked.connect(lambda: self.set_params())
        self.pushButton.clicked.connect(lambda: self.add_new_game())

    def add_new_game(self):
        control.add_new_game(self.params[0],
                             self.params[1],
                             self.params[2],
                             self.params[3],
                             self.params[4],
                             self.params[5],
                             self.params[6],
                             self.params[7],
                             self.params[8],
                             self.params[9],
                             self.params[10])

    def set_params(self):
        self.params.append(self.textEdit.toPlainText())
        self.params.append(get_str(self.textEdit_2.toPlainText()))
        self.params.append(get_str(self.textEdit_3.toPlainText()))
        self.params.append(get_str(self.textEdit_4.toPlainText()))
        self.params.append(get_str(self.textEdit_5.toPlainText()))
        self.params.append(get_str(self.textEdit_6.toPlainText()))
        self.params.append(self.textEdit_7.toPlainText())
        self.params.append(self.textEdit_8.toPlainText())
        self.params.append(self.textEdit_9.toPlainText())
        self.params.append(self.textEdit_10.toPlainText())
        self.params.append(self.textEdit_11.toPlainText())


def get_str(item):
    return "'" + item + "'"


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()