from PyQt4 import QtGui, QtCore 

class MenuWindow(QtGui.QWidget):
    """
        This is the main menu for the program.  This includes all basic 
        commands, buttons, menu items etc.
    """

    def __init__(self):
        super(MenuWindow, self).__init__()

        self.initUI()

    #Window Properties
    def initUI(self):

        #Make layout to hold btns
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        
        #***************************************************
        #                 Score Box                        
        # I want to move all functionality for the score-box
        # to here.  This should fix some problems I have with
        # passing variables.
        #***************************************************
        self.score_entry_btn = QtGui.QPushButton('Enter Scores')
        hbox.addWidget(self.score_entry_btn)
        self.score_entry_btn.clicked.connect(self.open_score_box)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 400, 50)
        self.setWindowTitle('TapTap')

        self.show()
    
    def open_score_box(self):
        self.score_entry_box = ScoreEntryWindow()
        
    def

class ScoreEntryWindow(QtGui.QWidget):
    """
    This is where the scores are entered into the program.
    """

    def __init__(self):
        super(ScoreEntryWindow, self).__init__()

        self.initUI()

    def initUI(self):

        #layout for test
        testScores = QtGui.QVBoxLayout()
        testScores.addWidget(QtGui.QLabel('Enter Exam Scores'))
        
        #I switched it over to a QTextEdit.  We'll need parse out the score 
        #with \cr's, \t's or ,'s
        self.scoresBox = QtGui.QTextEdit()
        self.scoresBox.resize(100, 400)
        testScores.addWidget(self.scoresBox)

        #buttons
        self.submitBtn = QtGui.QPushButton('Submit', self)
        self.resetBtn = QtGui.QPushButton('Reset', self)
        self.cancelBtn = QtGui.QPushButton('Cancel', self)
        
        self.resetBtn.clicked.connect(self.reset_text)
        self.submitBtn.clicked.connect(self.get_text_array)
        self.cancelBtn.clicked.connect(self.close)

        btnBar = QtGui.QHBoxLayout()
        btnBar.addStretch(1)
        btnBar.addWidget(self.submitBtn)
        btnBar.addWidget(self.resetBtn)
        btnBar.addWidget(self.cancelBtn)
        testScores.addLayout(btnBar)
        testScores.addStretch(1)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(testScores)

        self.setLayout(hbox)
        #Figure out how to auto set the height
        self.setGeometry(505, 100, 250, 200) 
        self.setWindowTitle('Student Scores')

        self.show()
    
    def reset_text(self):
        """
            Reset the box to no text
        """
        self.scoresBox.setText('')
        
    def get_text_array(self):
        """
            This creates an array of the scores.  The only non-score characters
            allowed are white-spaces and commas as these are taken out.
            If other characters are present... I guess we could take them out
            as well...
        """
        self.scores_string = (
                        str(self.scoresBox.toPlainText())
                        .replace(",", " ")
                        .split()
                        )
        print self.scores_string
        self.close()
        #return scores_string

