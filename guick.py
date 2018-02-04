import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,\
    QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
# from PyQt5 import QtCore
# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    # QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    # QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
import click


@click.command()
@click.option("--helo")
def example_cmd(helo):
    print(helo)


class App(QMainWindow):

    def __init__(self, func):
        super().__init__()
        self.func = func
        self.title = func.name
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('run', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        sys.argv = [self.func.name]
        sys.argv.append(self.func.params[0].opts[0])
        textboxValue = self.textbox.text()
        sys.argv.append(textboxValue)
        print(sys.argv)
        self.func()


if __name__ == "__main__":
    # example_cmd()
    app = QApplication(sys.argv)
    ex = App(example_cmd)
    sys.exit(app.exec_())
