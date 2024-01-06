from PyQt5.QtWidgets import QWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPainter


class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dataExcel = None
        
    def setup(self):

        seriesR = QLineSeries()
        seriesR.setName('Curva Ruta')  # Nombre de la serie (para la leyenda)
        seriesR.setPointsVisible(True)  # Hacer visibles los puntos de la serie

        seriesN = QLineSeries()
        seriesN.setName('Curva Natural')  # Nombre de la serie (para la leyenda)
        seriesN.setPointsVisible(True)  # Hacer visibles los puntos de la serie
        if self.dataExcel is not None:
            for i in range(len(self.dataExcel)):
                seriesR.append(self.dataExcel['cotas'][i], self.dataExcel['nodosR'][i])
                seriesN.append(self.dataExcel['cotas'][i], self.dataExcel['nodosN'][i])
        
        chart = QChart()
        chart.setBackgroundBrush(QBrush(QColor("lightblue")))
        chart.addSeries(seriesR)
        chart.addSeries(seriesN)
        
        # Establecer los ejes manualmente
        axis_x = QValueAxis()
        axis_x.setTitleText('Cotas')
        axis_x.setRange(0, self.dataExcel['cotas'].max())
        chart.addAxis(axis_x, Qt.AlignBottom)
        seriesR.attachAxis(axis_x)
        seriesN.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText('Alturas')
        axis_y.setRange(min(0, self.dataExcel['nodosR'].min(), self.dataExcel['nodosN'].min()) - 0,
                        max(self.dataExcel['nodosR'].max(), self.dataExcel['nodosN'].max()) + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        seriesR.attachAxis(axis_y)
        seriesN.attachAxis(axis_y)
        
        chart.setTitle('Gráfico de Corte Transversal - Razante')

        self.chart_view = QChartView(chart)
        
    def updateData(self, data):
        pass
        