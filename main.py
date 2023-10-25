import sys
import hktt
from hktt import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class ExampleApp(QtWidgets.QMainWindow, hktt.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def p_click(self):
        self.label.setText("testing..")

    def initUI(self):
        self.pushButton.clicked.connect(self.p_click)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.setWindowTitle("КС Ведомость")
    window.setWindowIcon(QtGui.QIcon('Icon.ico'))
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
