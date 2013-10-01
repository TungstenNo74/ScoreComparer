import sys
from PyQt4 import QtGui

class MenuWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MenuWindow, self).__init__()
        
        self.initUI()

    #Window Properties
    def initUI(self):
        self.setGeometry(100, 100, 400, 50)
        self.setWindowTitle('Scores Window')
        
        self.show()

class ScoreEntryWindow(QtGui.QWidget):
    
    def __init__(self):
        super(ScoreEntryWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(505, 100, 250, 400)
        self.setWindowTitle('Menu Window')
    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex1 = ScoreEntryWindow()
    ex2 = MenuWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()