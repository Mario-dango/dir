from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from app.src.model.archivosExcel import ExcelModel

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class FileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.fileName = None
        self.pathSave = "../../resources/data/saveData"
        self.pathLoad = "../../resources/data/loadData"
        self.formats = "Excel2007 (*.xlsx);; Excel97 (*.xls);; doc CSV (*.csv);; Libre Office (*.ods)"
        self.fileDialog = QFileDialog()
      
    def open(self, mode=None):
        self.fileDialog.setFileMode(QFileDialog.ExistingFile)
        if mode is not None:
            print("mode is %s" % mode)
            #  or "SAVE" or "guardar" or "Guardar"
            if (mode == "save") or (mode == "Save"):
                self.fileName = self.fileDialog.getSaveFileName(self, "Guardar Documento", self.pathSave, self.formats)
                print(f"se guardó el archivo en: {self.fileName}")
                # "Load" or "LOAD" or "cargar" or "Cargar"
            elif (mode == "load") or (mode == "Load") or (mode == "LOAD") or (mode == "cargar") or (mode == "Cargar"):
                self.fileName = self.fileDialog.getOpenFileName(self, "Cargar Documento", self.pathLoad, self.formats)
                print(f"se seleccionó el archivo: {self.fileName}")
            else:
                self.fileName = None
                print("No se especifica el Método.")
                print(f"No se guardó el archivo: {self.fileName}")
            return self.fileName
    
    def directorio(self):
        self.fileDialog.setWindowTitle("Seleccionar directorio")
        self.fileDialog.setFileMode(QFileDialog.Directory)
        selected_directory = self.fileDialog.selectedFiles()
        print("Directorio seleccionado:", selected_directory[0])
        self.directory = selected_directory
        

class WidgetsGrafB(QWidget):
    def __init__(self, grafType):
        super().__init__()
        self.grafType = grafType
        self.data = None
        
        self.pathDataDefault = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/"
        # self.pathDataDefault = "../../resources/data/examples/"
        self.listGraf = []
        self.shortName = None
        self.tituloChart = None
        self.nombreCurva = None
        self.nombreCota = None
        self.defaultModel = ExcelModel()
        self.chart = QChart()
        self.seriesR = QLineSeries()
        self.seriesN = QLineSeries()
        self.axis_x = QValueAxis()
        self.axis_y = QValueAxis()
        self.chart_view = QChartView(self.chart)
        self.setMouseTracking(True)  # Habilitar el seguimiento del cursor
        
        # Conectar la señal mouseMoveEvent al método correspondiente
        self.chart_view.mouseMoveEvent = self.mouse_move_event
        self.chart_view.setMouseTracking(True)  # Habilitar el seguimiento del cursor
        
        
        self.setup()
    
    def mouse_move_event(self, event: QMouseEvent):
        # Verificar si el evento se produce dentro del área del gráfico
        if self.chart_view.chart().plotArea().contains(event.pos()):
            # Obtener la posición del cursor en relación con el gráfico
            chart_pos = self.chart_view.chart().mapToValue(event.pos())
            
            # Verificar si el cursor está cerca de los puntos de la serieR
            for i in range(self.seriesR.count()):
                if self.seriesR.at(i).x() - 0.5 < chart_pos.x() < self.seriesR.at(i).x() + 0.5 and self.seriesR.at(i).y() - 0.5 < chart_pos.y() < self.seriesR.at(i).y() + 0.5:
                    self.seriesR.setPointColor(i, QColor("red"))  # Cambiar el color del punto de la serieR a rojo
                else:
                    self.seriesR.setPointColor(i, QColor("blue"))  # Restaurar el color del punto de la serieR a azul por defecto

            # Actualizar la vista del gráfico
            self.chart_view.chart().removeAllSeries()
            self.chart_view.chart().addSeries(self.seriesR)
            self.chart_view.chart().addSeries(self.seriesN)

            # Refrescar el gráfico
            self.chart_view.update()
    
    def setup(self):
        # Conectar la señal mouseMoveEvent al método correspondiente
        self.chart_view.mouseMoveEvent = self.mouse_move_event
        
        if self.grafType == "long":
            self.pathDataDefault = self.pathDataDefault + "dataLongitud.csv"
            self.tituloChart = 'Gráfico de Corte Longitudinal - Razante'
            self.nombreCurva = "Curva Perfil de Razante"
            self.nombreCota = "Prograsivas"
            self.shortName = "Longitudinal"
            self.default()
        elif self.grafType == "tran" or self.grafType == "trans":
            self.pathDataDefault = self.pathDataDefault + "dataTransversal.csv"
            self.tituloChart = 'Gráfico de Corte Transversal - por cada Nodo Razante'
            self.nombreCurva = "Curva Perfil de Ruta"
            self.nombreCota = "Cotas"
            self.shortName = "Transversal"
            self.default()
        else:
            print("error al intentar graficar el widget")
            
    def default(self):
        if self.data is None:
            #usar datos de dafault
            print(type(self.data))
            try:
                self.data = self.defaultModel.leerData(self.pathDataDefault)
            
                self.seriesR.setName(self.nombreCurva)  # Nombre de la serie (para la leyenda)
                self.seriesR.setPointsVisible(True)  # Hacer visibles los puntos de la serie

                self.seriesN.setName('Curva Terreno Natural')  # Nombre de la serie (para la leyenda)
                self.seriesN.setPointsVisible(True)  # Hacer visibles los puntos de la serie

                print(self.data)
                for i in range(len(self.data)):
                    self.seriesR.append(self.data['cotas'][i], self.data['nodosR'][i])
                    self.seriesN.append(self.data['cotas'][i], self.data['nodosN'][i])

                print(type(self.data))
                self.chart.setBackgroundBrush(QBrush(QColor("lightblue")))
                self.chart.addSeries(self.seriesR)
                self.chart.addSeries(self.seriesN)
                
                # Establecer los ejes manualmente
                self.axis_x.setTitleText(self.nombreCota)
                self.axis_x.setRange(0, self.data['cotas'].max())
                self.chart.addAxis(self.axis_x, Qt.AlignBottom)
                self.seriesR.attachAxis(self.axis_x)
                self.seriesN.attachAxis(self.axis_x)

                self.axis_y.setTitleText('Alturas')
                self.axis_y.setRange(min(0, self.data['nodosR'].min(), self.data['nodosN'].min()) - 0,
                                max(self.data['nodosR'].max(), self.data['nodosN'].max()) + 5)
                self.chart.addAxis(self.axis_y, Qt.AlignLeft)
                self.seriesR.attachAxis(self.axis_y)
                self.seriesN.attachAxis(self.axis_y)
                
                self.chart.setTitle(self.tituloChart)

                self.chart_view = QChartView(self.chart)
            except Exception as e:
                print(f"Hubo un error: {e}")              
        
    
    def mouse_move_event(self, event: QMouseEvent):
        # Verificar si el evento se produce dentro del área del gráfico
        if self.chart_view.chart().plotArea().contains(event.pos()):
            # Obtener la posición del cursor en relación con el gráfico
            chart_pos = self.chart_view.chart().mapToValue(event.pos())
            
            # Verificar si el cursor está cerca de los puntos de la serieR
            for i in range(self.seriesR.count()):
                if self.seriesR.at(i).x() - 0.5 < chart_pos.x() < self.seriesR.at(i).x() + 0.5 and self.seriesR.at(i).y() - 0.5 < chart_pos.y() < self.seriesR.at(i).y() + 0.5:
                    self.seriesR.setColor(QColor("red"))  # Cambiar el color de la serieR a rojo
                else:
                    self.seriesR.setColor(QColor("blue"))  # Cambiar el color de la serieR a azul por defecto

            # Actualizar la vista del gráfico
            self.chart_view.chart().removeAllSeries()
            self.chart_view.chart().addSeries(self.seriesR)
            self.chart_view.chart().addSeries(self.seriesN)

            # Refrescar el gráfico
            self.chart_view.update()
    
    def updateData(self, newData):     
        if newData > 0 and newData is not None:   
            self.seriesR = QLineSeries()
            self.seriesR.setName(self.nombreCurva)  # Nombre de la serie (para la leyenda)
            self.seriesR.setPointsVisible(True)  # Hacer visibles los puntos de la serie

            self.seriesN = QLineSeries()
            self.seriesN.setName('Curva Terreno Natural')  # Nombre de la serie (para la leyenda)
            self.seriesN.setPointsVisible(True)  # Hacer visibles los puntos de la serie

            for i in range(len(newData)):
                self.seriesR.append(newData['cotas'][i], newData['nodosR'][i])
                self.seriesN.append(newData['cotas'][i], newData['nodosN'][i])

            self.chart = QChart()
            self.chart.setBackgroundBrush(QBrush(QColor("lightblue")))
            self.chart.addSeries(self.seriesR)
            self.chart.addSeries(self.seriesN)
        else:
            print(f"No se pudo actualizar los datos del grafico {self.shortName}")




class WidgetsGraf(QWidget):
    def __init__(self, dProgresiva, hRazante, hTerreno, parent=None):
        super().__init__(parent)
        
        self.figura = plt.figure()
        self.terreno = plt.subplot()
        self.razante = plt.subplot()
        self.canvas = FigureCanvas(self.figura)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.progresiva = dProgresiva
        self.hRazante = hRazante
        self.hTerreno = hTerreno
        self.lineTerreno, = self.terreno.plot(self.progresiva, self.hTerreno, marker='+', linestyle=':', color='g')
        self.lineRazante, = self.razante.plot(self.progresiva, self.hRazante, marker='x', linestyle='--', color='b')

        self.selected_point = None  # Punto seleccionado
        self.offset = 0  # Offset del desplazamiento

        self.lbl_previous = QLabel('Posición anterior:')
        layout.addWidget(self.lbl_previous)
        self.lbl_new = QLabel('Nueva posición:')
        layout.addWidget(self.lbl_new)
        

class PlotWidget(QWidget):
    def __init__(self, parent=None, fig=None, canvas=None, ax=None):
        super().__init__(parent)

        # self.fig, self.ax = plt.subplots()
        # self.canvas = FigureCanvas(self.fig)
        
        self.fig = fig
        self.ax = ax
        self.canvas = canvas
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 3, 5, 7, 11]
        self.line, = self.ax.plot(self.x, self.y, marker='o', linestyle='-', color='b')

        self.selected_point = None  # Punto seleccionado
        self.offset = 0  # Offset del desplazamiento

        self.lbl_previous = QLabel('Posición anterior:')
        layout.addWidget(self.lbl_previous)
        self.lbl_new = QLabel('Nueva posición:')
        layout.addWidget(self.lbl_new)

        self.cid_press = self.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_release = self.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_move = self.canvas.mpl_connect('motion_notify_event', self.on_move)

    def on_click(self, event):
        if event.inaxes == self.ax:
            xdata = self.line.get_xdata()
            ydata = self.line.get_ydata()

            # Verificar la distancia con los puntos
            for i, (x, y) in enumerate(zip(xdata, ydata)):
                distance = ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                if distance < 0.1:  # Valor de tolerancia para seleccionar el punto
                    self.selected_point = i
                    self.lbl_previous.setText(f'Posición anterior: ({x:.2f}, {y:.2f})')
                    break

    def on_release(self, event):
        self.selected_point = None

    def on_move(self, event):
        if self.selected_point is not None:
            if event.inaxes == self.ax:
                new_y = self.y.copy()
                new_y[self.selected_point] = event.ydata
                self.line.set_ydata(new_y)
                self.lbl_new.setText(f'Nueva posición: ({self.x[self.selected_point]:.2f}, {event.ydata:.2f})')
                self.canvas.draw()
