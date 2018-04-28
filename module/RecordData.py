import pandas as pd
import csv


class Record():
    def __init__(self,intputFilePath,NumPoint):
        self.File = intputFilePath
        self.NumPoint = NumPoint
        self.Tail = self.GetTail()
        self.SetColInfo()

    def GetTail(self):
        dataframe = pd.read_csv(self.File,sep='\t',header=0)
        return dataframe.tail(self.NumPoint)

    def SetColInfo(self):
        self.Tail.columns = ["Time","Data"]

    def GetMean(self):
        return self.Tail.Data.mean()

    def GetFinalTime(self):
        return self.Tail.tail(1).Time

    def DataWrite(self,conc,output):
        data = [conc, '', ]
        data.extend(list(self.Tail.Data))
        data.extend(['', self.GetMean()])
        with open (output,"a") as out:
            wt = csv.writer(out)
            wt.writerow(data)

    def close(self):
        pass