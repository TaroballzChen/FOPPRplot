from module.calc import calc
from module.RecordData import Record
from module.io import IO
from core.ui_operation import window_op
import sys,threading
from PyQt5 import QtWidgets

class Main(window_op):

    def __init__(self):
        super(Main, self).__init__()
        self.io = IO()
        self.calc = calc()
        self.NIDATA = ''
        self.SignalMeanData = []
        self.FinalTimeData =[]
        self.NormalizeData = []



    def makeMeanList_and_getTime(self):
        Rec = Record(self.NIDATA,self.Numpoint,)
        MeanValue = Rec.GetMean()
        Time = float(Rec.GetFinalTime())
        self.SignalMeanData.append(MeanValue)
        self.FinalTimeData.append(Time)
        return MeanValue,Time


    def RecordTime_WriteData(self):
        super(Main, self).RecordTime_WriteData()
        if self.Blank_button.isEnabled():
            return
        sampleMean, Time = self.makeMeanList_and_getTime()
        self.WriteDatathread = threading.Thread(target=self.io.write_conc_with_x_point,
                                        args=(self.NIDATA, self.Conclist[-1], self.FinalTimeData[-1]))
        self.Console.appendPlainText("Samplemean Data write : %s with time %s" % (sampleMean, Time))
        self.WriteDatathread.start()
        self.RecordTime.setText(str(Time))
        y_point = self.calc.normalize(self.SignalMeanData)
        self.NormalizeData.append(y_point)
        self.WriteDatathread.join()


        logconc = self.plot(self.Conclist,self.NormalizeData)
        self.io.plotDataWrite(self.NIDATA,logconc,self.NormalizeData)


    def record_blank(self):
        super(Main, self).record_blank()
        if self.NIDATA == '':
            if self.io.find_latest_file(self.NIdir) != None:
                self.NIDATA = self.io.find_latest_file(self.NIdir)
                self.Console.appendPlainText("Latest NI recorded File %s Locked"%self.NIDATA)
                self.WriteData_button.setEnabled(True)
            else:
                self.Console.appendPlainText("Please select correct Directory")
                self.Blank_button.setEnabled(True)
                self.WriteData_button.setEnabled(False)
                self.WriteData_button.setStyleSheet("background-color:red")
                return
        if self.Numpoint == 0:
            return
        if self.conc_combo.currentText() =='':
            return

        blankMean,Time = self.makeMeanList_and_getTime()
        self.WriteDatathread = threading.Thread(target=self.io.write_conc_with_x_point,
                                        args=(self.NIDATA, 'blank', self.FinalTimeData[-1]))
        self.WriteDatathread.start()
        self.Console.appendPlainText("blankmean Data write : %s with time %s"%(blankMean,Time))
        self.RecordTime.setText(str(Time))
        self.WriteDatathread.join()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())