## Cargar y mostrar datos desde el Excel a chart en PyQT5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPainter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def leer_datos_excel(nombre_archivo):
    datos = pd.read_csv(nombre_archivo)
    return datos

def graficar_datos(datos):
    fig, ax = plt.subplots()
    
        # Graficar los datos de distancia vs número de muestra
    ax.plot(datos['Cotas'], datos['nodosR'], label='Nodos Ruta')
    # Graficar otro conjunto de datos desde otra columna
    ax.plot(datos['Cotas'], datos['nodosN'], label='Nodos Terreno')
    ax.legend()
    
    # # Ajustar los límites del gráfico y desactivar el ajuste automático
    # max_distancia = datos['Distancia'].max()
    # max_muestra = datos['Numero de muestra'].max()
    # min_muestra = datos['Numero de muestra'].min()

    # ax.set_xlim(0, max_distancia)
    # ax.set_ylim(min(0, min_muestra) - 5, max_muestra + 5)  # Ajustar el espacio entre el eje Y en 0 y los valores
    # ax.autoscale(enable=False)  # Desactivar el ajuste automático de los límites

    # Dibujar línea horizontal en el eje Y = 0
    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

    plt.show()

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        datos_excel = leer_datos_excel('../../resources/data/examples/dataTransversal.csv')


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
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Gráfico de Polígonos desde Excel')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        chart1 = ChartWidget()
        chart2 = ChartWidget()
        
        layout.addWidget(chart1.chart_view)
        layout.addWidget(chart2.chart_view)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())