import sys
from PyQt4 import QtGui

class Main_Window(QtGui.QWidget):
    "This is the main window for the, housing all controls and info"
    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.data_array = []
        self.initUi()
    
    def initUi(self):
        "This includes both the layout and sets bindings for this window"
    ##Layout
        btn_box = QtGui.QHBoxLayout()
        btn_box.addStretch(1)

        self.ent_scrs_btn = QtGui.QPushButton('Enter Scores')
        btn_box.addWidget(self.ent_scrs_btn)

        wndw_box = QtGui.QVBoxLayout()
        wndw_box.addStretch(1)
        wndw_box.addLayout(btn_box)
        
        self.setLayout(wndw_box)
        self.setGeometry(100, 100, 400, 50)
        self.setWindowTitle('TapTap')
        self.show()
        
    ##Bindings
        self.ent_scrs_btn.clicked.connect(self.open_score_frame)
    
    def open_score_frame(self):
        "Opens the frame where scores are entered"
        self.score_frame = Score_Frame()
        sf = self.score_frame #alias
        sf.sub_btn.clicked.connect(self.append_data)
        sf.rst_btn.clicked.connect(self.reset_text)
    
    def append_data(self):
        "Add score frame data to the master data array"
        scores_string = str(self.score_frame.score_entry_box.toPlainText())

                
        scores_dict = {}
        scores_dict['scores'] = clean_scores_string(self, scores_string)

        #Insert the date
        date = self.score_frame.cal.selectedDate()
        scores_dict['date'] = date
        self.score_frame.close()

        self.data_array.append(scores_dict)
        print self.data_array[len(self.data_array)-1]['date']
        print self.data_array[len(self.data_array)-1]['scores']
    
    def reset_text(self):
        "Resets score entry box text to an empty string"
        self.score_frame.score_entry_box.setText('')

class Score_Frame(QtGui.QWidget):
    """
       This is the frame where we enter scores 
    """
    
    def __init__(self):
        "Initialize the window"
        super(Score_Frame, self).__init__()
        self.initUi()

    def initUi(self):
        """
        The UI layout.  Bindings should be present in the Main_Window Class.
        """

        wndw_box = QtGui.QVBoxLayout()

        #Calendar
        wndw_box.addWidget(QtGui.QLabel("Enter the date of the Exam"))
        self.cal = QtGui.QCalendarWidget()
        wndw_box.addWidget(self.cal)

        #Score Entry Box
        wndw_box.addWidget(QtGui.QLabel("Enter Scores Below"))
        self.score_entry_box = QtGui.QTextEdit()
        wndw_box.addWidget(self.score_entry_box)

        #Buttons
        btn_box = QtGui.QHBoxLayout()
        btn_box.addStretch(1)

        self.sub_btn = QtGui.QPushButton('Submit')
        self.ccl_btn = QtGui.QPushButton('Cancel')
        self.rst_btn = QtGui.QPushButton('Reset')
        
        btn_box.addWidget(self.sub_btn)
        btn_box.addWidget(self.ccl_btn)
        btn_box.addWidget(self.rst_btn)
        wndw_box.addLayout(btn_box)
        
        self.setLayout(wndw_box)
        self.setGeometry(100, 100, 300, 550)
        self.setWindowTitle('Enter Scores')
        self.show()

def sort_array(scores_string):
    "Puts cleaned string into float array"
    punc_array = [',', ';'] 
    for punc in punc_array:
        scores_string = scores_string.replace(punc, ' ')

    scores_array = scores_string.split()
    clean_array = []
    num_reject = 0
    reject_array = []
    for score in scores_array:
        temp_string = score.replace('.', '').replace('-', '')
        if temp_string.isdigit():
            clean_array.append(float(score))
        else:
            num_reject += 1
            reject_array.append(score)
    
    return num_reject, reject_array, clean_array

def clean_scores_string(self, scores_string):
    "notifies user of any unacepted data"
    num_reject, reject_array, clean_array = sort_array(scores_string)

    if num_reject > 0:
        "Tell the user which scores didn't make it in"
        QtGui.QMessageBox.about(self,
                                'Invalid Scores',
                                '%d score(s) rejected: %s'
                                % (num_reject, ', '.join(reject_array)))
    return clean_array

