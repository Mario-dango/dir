from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPainter


class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dataExcel = None
        
        
    def setup(self):
        datos_excel = leer_datos_excel('../../resources/data/examples/data.csv')


        seriesR = QLineSeries()
        labelGraf = QLabel()
        labelGraf.setText('Grafico de corte Transversal')
        seriesR.setName('Curva Ruta')  # Nombre de la serie (para la leyenda)
        seriesR.setPointsVisible(True)  # Hacer visibles los puntos de la serie

        seriesN = QLineSeries()
        seriesN.setName('Curva Natural')  # Nombre de la serie (para la leyenda)
        seriesN.setPointsVisible(True)  # Hacer visibles los puntos de la serie

        for i in range(len(datos_excel)):
            seriesR.append(datos_excel['cotas'][i], datos_excel['nodosR'][i])
            seriesN.append(datos_excel['cotas'][i], datos_excel['nodosN'][i])

        chart = QChart()
        chart.setBackgroundBrush(QBrush(QColor("lightblue")))
        chart.addSeries(seriesR)
        chart.addSeries(seriesN)
        
        # Establecer los ejes manualmente
        axis_x = QValueAxis()
        axis_x.setTitleText('Cotas')
        axis_x.setRange(0, datos_excel['cotas'].max())
        chart.addAxis(axis_x, Qt.AlignBottom)
        seriesR.attachAxis(axis_x)
        seriesN.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText('Alturas')
        axis_y.setRange(min(0, datos_excel['nodosR'].min(), datos_excel['nodosN'].min()) - 0,
                        max(datos_excel['nodosR'].max(), datos_excel['nodosN'].max()) + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        seriesR.attachAxis(axis_y)
        seriesN.attachAxis(axis_y)
        
        chart.setTitle('Gráfico de Corte Transversal - Razante')

        self.chart_view = QChartView(chart)
        