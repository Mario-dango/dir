# -*- coding: utf-8 -*-
##### LIBRERIAS Y DEPENDENCIAS NECESARIAS PARA LA CLASE #####
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from app.src.model.archivosExcel import ExcelModel
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
################################################################

## CLASE DEFINIDA DEL WIDGET GESTOR DE ARCHIVOS ##
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
        

## CLASE DEFINIDA DEL WIDGET GESTOR DE GRÁFICOS ##
class WidgetsGraf(QWidget):
    def __init__(self, dProgresiva, hRazante=None, hTerreno=None, parent=None):
        super().__init__(parent)
        
        self.figura = plt.figure()
        self.terreno = plt.subplot()
        self.razante = plt.subplot()
        self.canvas = FigureCanvas(self.figura)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.progresiva = dProgresiva
        if hTerreno is not None:
            self.hTerreno = hTerreno
        else:
            self.hTerreno = [15]*len(self.progresiva)
        if hRazante is not None:
            self.hRazante = hRazante
        else: 
            self.hRazante = [10]*len(self.progresiva)
        self.lineTerreno, = self.terreno.plot(self.progresiva, self.hTerreno, marker='+', linestyle=':', color='g')
        self.lineRazante, = self.razante.plot(self.progresiva, self.hRazante, marker='x', linestyle='--', color='b')

        self.selected_point = None  # Punto seleccionado
        self.offset = 0  # Offset del desplazamiento

        self.lbl_previous = QLabel('Posición anterior:')
        layout.addWidget(self.lbl_previous)
        self.lbl_new = QLabel('Nueva posición:')
        layout.addWidget(self.lbl_new)
        
    def update_grafico(self):
        # Actualizar los datos en el gráfico
        self.lineTerreno.set_data(self.progresiva, self.hTerreno)
        self.lineRazante.set_data(self.progresiva, self.hRazante)

        # Ajustar la vista al nuevo rango de datos
        self.terreno.relim()
        self.terreno.autoscale_view()

        # Redibujar el lienzo
        self.canvas.draw()
        
## CLASE DEFINIDA DEL DIALOG GESTOR DE DATOS PERFIL TRANSVERSAL ##
class VentanaEmergenteExcel(QDialog):
    def __init__(self, parent= None):
        super().__init__(parent)
        #Iniciar el objeto QMainWindow
        QDialog.__init__(self)
        pathUi = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/ui/configLoad.ui"
        # pathUi = "/SER/app/src/view/mainwindow.ui"
        # cargar la interfaz de usuario desde el archivo ui generado por Qt Designer
        self.dialogUi = uic.loadUi(pathUi, self)
        self.setWindowTitle("Datos tipo")
        

## CLASE DEFINIDA DEL WIDGET PARA PLOTEAR GRAFICOS DE EJEMPLO ##
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
