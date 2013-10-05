#Setup the UI
from window import *
import sys
from PyQt4 import QtGui

def main():
    
    app = QtGui.QApplication(sys.argv)
    main_window = Main_Window() 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()