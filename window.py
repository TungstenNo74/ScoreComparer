import sys
from PyQt4 import QtGui

class MenuWindow(QtGui.QWidget):

    def __init__(self):
        super(MenuWindow, self).__init__()

        self.initUI()

    #Window Properties
    def initUI(self):
        #Make layout to hold btns
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        #Create Buttons
        #This will arbitrarily create buttons as they are added to this list.
        btnArray = ['Run', 'Reset', 'Print']
        btnDic = {}
        for btn in btnArray:
            btnDic[btn] = QtGui.QPushButton(btn)
            #load into layout
            hbox.addWidget(btnDic[btn])


        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 400, 50)
        self.setWindowTitle('TapTap')

        self.show()

class ScoreEntryWindow(QtGui.QWidget):

    def __init__(self):
        super(ScoreEntryWindow, self).__init__()

        self.initUI()

    def initUI(self):
        #Set number of students here.  Later, this will be moved onto the Frame
        noStudents = 8

        #layout for test 1
        testScores1 = QtGui.QVBoxLayout()
        testScores1.addWidget(QtGui.QLabel('Test 1'))

        #Dictionary to hold widgets
        scoreDic1 = {}

        i = 0
        while i < noStudents:
            #I'm not really sure that I need the 'Score' part...
            #but I think that it may become more readable with it.
            #I should probably turn it into an array and just use i as the index
            scoreDic1['Score' + str(i)] = QtGui.QLineEdit()
            testScores1.addWidget(scoreDic1['Score' + str(i)])
            i = i + 1
        testScores1.addStretch(1)


        #Same as above but with the second set of test scores.
        #I probably should combine both into one dictionary
        testScores2 = QtGui.QVBoxLayout()
        testScores2.addWidget(QtGui.QLabel('Test 2'))

        i = 0

        scoreDic2 = {}
        while i < noStudents:
            scoreDic2['Score' + str(i)] = QtGui.QLineEdit()
            testScores2.addWidget(scoreDic2['Score' + str(i)])
            i = i + 1
        testScores2.addStretch(1)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(testScores1)
        hbox.addLayout(testScores2)

        self.setLayout(hbox)
        self.setGeometry(505, 100, 250, 400) #Figure out how to auto set the height
        self.setWindowTitle('Student Scores')

        self.show()

#TODO: move main into its own module...
def main():

    app = QtGui.QApplication(sys.argv)
    #I would eventually like to tether these both into the same window, but for now they're separate
    ex1 = ScoreEntryWindow()
    ex2 = MenuWindow()
    #When the report window is created, I would like to keep that separated.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
