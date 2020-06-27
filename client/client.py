import sys
from PyQt5 import QtWidgets
import design
from backend import Data

data = Data()


class MyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget.addItems(data.games.keys())
        self.listWidget.itemSelectionChanged.connect(lambda: self.selection_changed())
        self.pushButton.clicked.connect(lambda: self.update_text())
        self.pushButton_2.clicked.connect(lambda: self.update_rate())

    def update_text(self):
        game_info = data.get_value()
        self.textBrowser.setText(data.selected)
        self.textBrowser_2.setText(game_info[1])
        self.textBrowser_3.setText(game_info[2])
        self.textBrowser_4.setText(game_info[3])
        self.textBrowser_5.setText(game_info[4])
        self.textBrowser_6.setText(game_info[5] + "/" + game_info[6])
        self.textBrowser_7.setText(game_info[9])
        self.textBrowser_8.setText(game_info[8])
        self.textBrowser_9.setText(game_info[7])
        self.textBrowser_10.setText(game_info[10])

    def selection_changed(self):
        data.selected = self.listWidget.currentItem().text()

    def update_rate(self):
        data.send_rate(self.spinBox.value())

    def closeEvent(self, event):
        data.save_rates()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
