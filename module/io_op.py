import glob,os

class IO():
    def __init__(self):
        pass

    def find_latest_file(self,NIdirPATH):
        All_of_Origin_file = glob.glob('%s*.lvm'%NIdirPATH)
        if All_of_Origin_file:
            Latest_file = max(All_of_Origin_file,key=os.path.getmtime)
            return Latest_file

    def write_conc_with_x_point(self,FileName,now_conc,now_time):
        point_record = FileName.replace('.lvm','.txt')
        with open(point_record,'a') as pr:
            pr.write('\t'.join([str(now_conc),str(now_time),'\n']))
        return

    def plotDataWrite(self,FileName,xvalue,yvalue):
        PlotDataName = FileName.replace(".lvm",'_plotdata.txt')
        with open(PlotDataName,'a') as p:
            p.write('\t'.join([str(xvalue[-1]), str(abs(yvalue[-1])), '\n']))
        return