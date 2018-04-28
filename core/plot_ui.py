from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


class plot_window():
    def __init__(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)


    def plot(self,conc,data,samplename="sample"):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.clear()

        logconc = [np.log10(x) for x in conc]

        ax.scatter(logconc,data,marker='s',label=samplename,c="k")
        ax.set(ylabel=r'normalize data (I - I$_0$ / I$_0$)',xlabel = "-log [concentration (g/mL) ]")
        ax.set_ylim(auto=True)
        ax.set_xlim(auto=True)

        ax.legend(loc='upper right')

        if len(data) > 1:
            # Trendline plot
            equation = self._trendline(logconc,data)
            # get data stats
            slope, intercept, r_value, Rsquare = self.get_stats(logconc,data)
            # table in fig
            self.table(equation,samplename,intercept,slope,r_value,Rsquare)

        self.canvas.draw()
        return logconc

    def _trendline(self,conc,data):
        z = np.polyfit(conc,data,1)
        p = np.poly1d(z)

        y_hat = p(conc)
        plt.plot(conc,y_hat,"r",linewidth=.8)
        equation = "y = %.3fx + %.3f"%(z[0],z[1])

        return equation


    def get_stats(self,conc,data):
        slope, intercept, r_value, p_value, std_err = stats.linregress(conc,data)

        return "%.4f"%slope,"%.4f"%intercept,"%.4f"%r_value,"%.4f"%(r_value**2)


    def table(self,equation,plot_sample,intercept,slope,Pearsons_r,r_square_value):
        # col_labels = ['']
        row_labels = ['Equation','Plot','Intercept','Slope',"Pearson's r","R-square"]
        table_vals = [[equation],[plot_sample],[intercept],[slope],[Pearsons_r],[r_square_value]]
        fig_table = plt.table(cellText = table_vals,colWidths = [0.2]*1,
                              rowLabels = row_labels, colLabels = None,
                              loc='lower right')
        fig_table.set_fontsize(15.0)
