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
        self.btnDic = {}
        for btn in btnArray:
            self.btnDic[btn] = QtGui.QPushButton(btn)
            #load into layout
            hbox.addWidget(self.btnDic[btn])

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

        #layout for test
        testScores = QtGui.QVBoxLayout()
        testScores.addWidget(QtGui.QLabel('Enter Exam Scores'))
        
        #I switched it over to a QTextEdit.  We'll need parse out the score with \cr's, \t's or ,'s
        self.scoresBox = QtGui.QTextEdit()
        self.scoresBox.resize(100, 400)
        testScores.addWidget(self.scoresBox)
        #buttons
        self.submitBtn = QtGui.QPushButton('Submit', self)
        self.resetBtn = QtGui.QPushButton('Reset', self)
        
        self.resetBtn.clicked.connect(self.resetText)

        btnBar = QtGui.QHBoxLayout()
        btnBar.addStretch(1)
        btnBar.addWidget(self.submitBtn)
        btnBar.addWidget(self.resetBtn)
        testScores.addLayout(btnBar)
        testScores.addStretch(1)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(testScores)

        self.setLayout(hbox)
        self.setGeometry(505, 100, 250, 200) #Figure out how to auto set the height
        self.setWindowTitle('Student Scores')

        self.show()
    
    def resetText(self):
        self.scoresBox.setText('')

