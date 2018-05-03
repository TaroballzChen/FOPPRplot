from core.ui import window
from PyQt5 import QtWidgets
import os

class window_op(window):
    def __init__(self):
        super(window_op, self).__init__()

        self.NIdir = "D:/NI DATA/"
        self.Numpoint = 0
        self.Conclist = []

        self.init_UI()



    """
        initialize UI interface
    """

    def init_UI(self):
        self.setGeometry(100, 100, 980, 980)

        UI_layout = QtWidgets.QVBoxLayout()

        UI_layout.addLayout(self.Dir_block ( browse = self.chooseNIDirectory,))
        UI_layout.addLayout(self.Conc_block( plot = self.RecordTime_WriteData,
                                             add = self.add_conc_to_combo,
                                             delete=self.remove_conc_from_combo,
                                             blank = self.record_blank,
                                             deleteData=self.remove_plot_data,))
        UI_layout.addLayout(self.Status_Console())
        UI_layout.addLayout(self.matplotlib_block())

        self.setWindowTitle('FOPPR Data Plot & Record GUI Ver4.0 Designed by Yuan-Yu')
        self.setLayout(UI_layout)

    """
        Record Concentration & Time Block Method
    """

    def add_conc_to_combo(self):
        conc = self.conc_input.text()
        if conc != '':
            self.conc_combo.addItem(conc)
            self.Console.appendPlainText("Appended concentration %s sucessfully"%conc)
            self.Console.update()
            self.conc_input.clear()
            self.WriteData_button.setEnabled(True)

    def remove_conc_from_combo(self):
        conc = self.conc_combo.currentText()
        index = self.conc_combo.findText(conc)
        if conc != '':
            self.conc_combo.removeItem(index)
            self.Console.appendPlainText("Removed concentration %s sucessfully"%conc)
            self.Console.update()
        if self.conc_combo.currentText() == '':
            self.WriteData_button.setEnabled(False)

    def record_blank(self):
        if  self.Numpoint == 0:
            if self.Numpoint_input.text() != "":
                self.Numpoint_input.setReadOnly(True)
                self.Numpoint = int(self.Numpoint_input.text())
                self.Console.appendPlainText("Numberpoint : %d LOCKED\n------------------------------"%self.Numpoint)
                self.Console.update()
            else:
                self.Console.appendPlainText("please type Number Point parameter")
                return
        self.Blank_button.setEnabled(False)
        self.WriteData_button.setStyleSheet("background-color:green")

    def RecordTime_WriteData(self):
        if self.NIdir_input.text() == "" or os.path.exists(self.NIdir) == False:
            self.Console.appendPlainText("Please select correct Directory")
            return

        if self.Blank_button.isEnabled():
            self.Console.appendPlainText("Please Push Blank Button First")
            return

        if self.conc_combo.currentText() == '':
            return

        current_conc = self.conc_combo.currentText()
        index = self.conc_combo.findText(current_conc)

        if '^' in current_conc:
            current_conc = current_conc.replace('^','**')
        current_conc = eval(current_conc)

        self.Conclist.append(current_conc)
        self.conc_combo.removeItem(index)

        self.data_combo.addItem(str(current_conc))

        if self.conc_combo.currentText() == '':
            self.WriteData_button.setEnabled(False)

        self.data_remove_button.setEnabled(True)

    def remove_plot_data(self):
        pass




        """
            Choose Directory of NI Data folder Method
        """

    def chooseNIDirectory(self):
        self.NI_dir = QtWidgets.QFileDialog()
        inputdir = self.NI_dir.getExistingDirectory(None, 'select NI DATA folder')
        self.NIdir_input.setText(inputdir + '/')
        self.NIdir = inputdir + '/'