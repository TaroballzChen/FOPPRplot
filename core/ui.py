from PyQt5 import QtWidgets
from core.plot_ui import plot_window
import os

class window(QtWidgets.QWidget,plot_window):

    def __init__(self):
        super().__init__()

    """
        Record Concentration & Time Block
    """

    def Conc_block(self,plot,add,delete,blank,deleteData):
        self.conc_input = QtWidgets.QLineEdit()
        self.conc_input.setFixedWidth(75)
        concLabel = QtWidgets.QLabel("conc.")
        self.concinput_add_button = QtWidgets.QPushButton("add")

        self.conc_combo = QtWidgets.QComboBox()
        self.conc_combo.setFixedWidth(75)
        conclistLabel = QtWidgets.QLabel("ConcList")
        self.conc_remove_button = QtWidgets.QPushButton("delete")

        self.RecordTime = QtWidgets.QLineEdit()
        self.RecordTime.setFixedWidth(60)
        self.RecordTime.setReadOnly(True)
        TimeRecordLabel = QtWidgets.QLabel("Recorded Time")

        self.Numpoint_input = QtWidgets.QLineEdit()
        self.Numpoint_input.setFixedWidth(40)
        NumpointLabel = QtWidgets.QLabel("point quantity")

        self.WriteData_button = QtWidgets.QPushButton("plot")
        self.WriteData_button.setEnabled(False)

        self.Blank_button = QtWidgets.QPushButton("blank")

        self.data_combo = QtWidgets.QComboBox()
        self.data_combo.setFixedWidth(75)

        datalistLabel = QtWidgets.QLabel("Recorded Conc.")
        self.data_remove_button = QtWidgets.QPushButton("delete")
        self.data_remove_button.setEnabled(False)
        self.data_remove_button.setStyleSheet("background-color:red")

        box = QtWidgets.QHBoxLayout()
        box.addWidget(NumpointLabel)
        box.addWidget(self.Numpoint_input)
        box.addWidget(concLabel)
        box.addWidget(self.conc_input)
        box.addWidget(self.concinput_add_button)
        box.addWidget(conclistLabel)
        box.addWidget(self.conc_combo)
        box.addWidget(self.conc_remove_button)
        box.addWidget(TimeRecordLabel)
        box.addWidget(self.RecordTime)
        box.addWidget(self.Blank_button)
        box.addWidget(self.WriteData_button)


        # Recorded Data delete
        box.addWidget(datalistLabel)
        box.addWidget(self.data_combo)
        box.addWidget(self.data_remove_button)


        self.WriteData_button.clicked.connect(plot)      #self.RecordTime_WriteData
        self.Blank_button.clicked.connect(blank)         #self.record_blank
        self.concinput_add_button.clicked.connect(add)   #self.add_conc_to_combo
        self.conc_remove_button.clicked.connect(delete)  #self.remove_conc_from_combo
        self.data_remove_button.clicked.connect(deleteData)

        return box

    """
        Choose Directory of NI Data folder
    """

    def Dir_block(self,browse):
        self.NIdir_input = QtWidgets.QLineEdit()
        self.NIdir_input.setText(self.NIdir)
        NIdirLabel = QtWidgets.QLabel("NI directory path")
        self.chooseNIfolder = QtWidgets.QPushButton("...")

    ### Sample Name input

        self.SampleName_input = QtWidgets.QLineEdit()
        SampleNameLabel = QtWidgets.QLabel("Sample Name")

        if os.path.exists(self.NIdir) == False:
            self.NIdir_input.clear()

    ### Sample Molecular Weight input

        SampleMWLabel = QtWidgets.QLabel("Sample M.W.")
        self.SampleMW_input = QtWidgets.QLineEdit()
        self.SampleMW_input.setText("150.0")
        Kda = QtWidgets.QLabel("Kda")

        box = QtWidgets.QHBoxLayout()
        box.addWidget(NIdirLabel)
        box.addWidget(self.NIdir_input)
        box.addWidget(self.chooseNIfolder)
        box.addWidget(SampleNameLabel)
        box.addWidget(self.SampleName_input)

        box.addWidget(SampleMWLabel)
        box.addWidget(self.SampleMW_input)
        box.addWidget(Kda)




        self.chooseNIfolder.clicked.connect(browse)  #self.chooseNIDirectory

        return box

    """
        Status Display
    """

    def Status_Console(self):
        self.Console = QtWidgets.QPlainTextEdit()
        self.Console.setStyleSheet(
            """QPlainTextEdit {background-color: #333;
                               color: #00FF00;
                               font-family: Courier;}""")
        self.Console.document().setPlainText("Welcome to FOPPR Data Operate System !\n"
                                          "================================================================================================")
        self.Console.setReadOnly(True)
        box = QtWidgets.QHBoxLayout()
        box.addWidget(self.Console)

        return box

    """
        matplotlib
    """

    def matplotlib_block(self):
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.toolbar)
        box.addWidget(self.canvas)

        return box