#Setup the UI
import window
import sys
from PyQt4 import QtGui

def main():

    app = QtGui.QApplication(sys.argv)
    #I would eventually like to tether these both into the same window, but for now they're separate
    ex1 = window.ScoreEntryWindow()
    ex2 = window.MenuWindow()
    #When the report window is created, I would like to keep that separated.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()