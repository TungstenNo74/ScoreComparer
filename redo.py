import sys
from PyQt4 import QtGui

class Main_Window(QtGui.QWidget):
    """
        This is the main window for the, housing all controls and info
    """
    
    def __init__(self):
        "Initialize the window"
        super(Main_Window, self).__init__()
        self.data_array = []
        self.initUi()
    
    def initUi(self):

        """The Ui layout.  All buttons and widgets need to be 'selfed', but
        let's leave the methods out of this thing..."""

    ##Layout
        btn_box = QtGui.QHBoxLayout()
        btn_box.addStretch(1)

        self.open_score_frame_btn = QtGui.QPushButton('Enter Scores')
        btn_box.addWidget(self.open_score_frame_btn)

        wndw_box = QtGui.QVBoxLayout()
        wndw_box.addStretch(1)
        wndw_box.addLayout(btn_box)
        
        self.setLayout(wndw_box)
        self.setGeometry(100, 100, 400, 50)
        self.setWindowTitle('TapTap')
        self.show()
        
    ##Bindings
        self.open_score_frame_btn.clicked.connect(self.open_score_frame)
    
    def open_score_frame(self):
        self.score_frame = Score_Frame()
        self.score_frame.sub_btn.clicked.connect(self.append_data)
        self.score_frame.rst_btn.clicked.connect(self.reset_text)
    
    def append_data(self):

        scores_string = str(self.score_frame.score_entry_box.toPlainText())

        """"I'm using the array below to hold any punctuation marks I want to 
        remove.  It's not the most readable way of doing this, but I want to
        be able to add and remove marks easily."""
        punc_array = [',', ';'] 
        for punc in punc_array:
            scores_string = scores_string.replace(punc, ' ')

        scores_array = scores_string.split()
        cleaned_array = []
        not_accepted = 0
        not_accepted_array = []
        for score in scores_array:
            if score.replace('.', '').replace('-','').isdigit():
                cleaned_array.append(float(score))
            else:
                not_accepted += 1
                not_accepted_array.append(score)

        if not_accepted > 0:
            "Tell the user which scores didn't make it in"
            QtGui.QMessageBox.about(self,
                                    'Invalid Scores',
                                    'Not all scores were accepted: %s'
                                    % ', '.join(not_accepted_array))
                
        scores_dict = {}
        scores_dict['scores'] = cleaned_array
        
        
        #Insert the date
        date = self.score_frame.cal.selectedDate()
        scores_dict['date'] = date
        self.score_frame.close()

        self.data_array.append(scores_dict)
        print self.data_array[len(self.data_array)-1]['date']
        print self.data_array[len(self.data_array)-1]['scores']
    
    def reset_text(self):
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
        """The Ui layout.  All buttons and widgets need to be 'selfed', but
        let's leave the methods out of this thing..."""

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

def main():
    
    app = QtGui.QApplication(sys.argv)
    main_window = Main_Window() 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
