# -*- coding: utf-8 -*-
##### LIBRERIAS Y DEPENDENCIAS NECESARIAS PARA LA CLASE #####
from PyQt5 import QtWidgets
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
################################################################

## CLASE DEFINIDA DE LA VENTANA PRINCIPAL ##
class VentanaPrincipal(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        pathUi = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/ui/principal.ui"
        # pathUi = "/SER/app/src/view/mainwindow.ui"
        # cargar la interfaz de usuario desde el archivo ui generado por Qt Designer
        self.windowUI = uic.loadUi(pathUi, self)
        self.setWindowTitle("DIR 1.0")
        
        # self.setMinimumSize(800,600)
        # self.setMaximumSize(1920,1080)
        self.setGeometry(800, 600, 1920, 1080)
        
        # Configura las banderas de la ventana
        flags = self.windowFlags()
        flags |= Qt.WindowMaximizeButtonHint  # Agrega la bandera de maximizar
        self.setWindowFlags(flags)

    ## MÉTODO PARA LA INICIALIZACION DE LA CLASE
    def initUI(self, widgetLong=None, widgetTrans=None): 
        
        if (widgetLong != None) and (widgetTrans != None):# Obtener el layout del QFrame si es un contenedor de layout
            frame_layout = self.windowUI.frameIzq.layout()  # Reemplaza con el método correcto si el QFrame tiene un layout

            # frame_layout.insertWidget(1, widgetLong.chart_view) 
            # self.widgetGrafLong = widgetLong
            # frame_layout.insertWidget(5, widgetTrans.chart_view) 
            # self.widgetGrafTrans = widgetTrans
            
            frame_layout.insertWidget(1, widgetLong) 
            self.widgetGrafLong = widgetLong
            frame_layout.insertWidget(5, widgetTrans) 
            self.widgetGrafTrans = widgetTrans
        pass

    def showEvent(self, event):
        pass
    
    def updateLongInfo(self, data):
        pass
    
    def updateTransInfo(self, data):
        self.windowUI.dataGrafTrans.setText(data)
        # self.window.layoutIzq.insertWidget(5, widgetTrans.chart_view) 
        # self.widgetGrafTrans = widgetTrans
        pass
    
    def updateInfo(self, data):
        self.windowUI.dataInfo.setText(data)
        
## CLASE DEFINIDA DE LA VENTANA OBRAS DE ARTE ##
class VentanaArte(QMainWindow):
    def __init__(self):
        super().__init__()
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)

        self.setWindowTitle('Gráfico de Polígonos desde Excel')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.initUI()
    
    def initUI(self):
        # Crear un layout vertical para el contenido
        self.layout = QVBoxLayout()
        # WidgetsGraf = widget
        # Crear una instancia de WidgetsGraf
        # self.ruta = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/dataLongitud.csv"
        # self.widget_graf = ChartWidget(path=self.ruta)  # Puedes pasar el tipo de gráfico que necesites

        # # Agregar el widget de WidgetsGraf al layout
        # self.layout.addWidget(self.widget_graf)

        # # Crear un widget contenedor para el layout
        # self.central_widget = QWidget()
        # self.central_widget.setLayout(self.layout)

        # # Establecer el widget contenedor como el widget central del QMainWindow
        # self.setCentralWidget(self.central_widget)
        
        
        # self.layout.addWidget(self.widget_graf.chart_view)

    # def initUI(self):
    #     self.layoutIzq = QtWidgets.QVBoxLayout()
        
    # def agregarWidget(self, widget):
    #     print(widget)
    #     self.widgetGrafLong = widget
    #     self.widgetGrafLong.setObjectName("widgetGrafLong")
    #     self.layoutIzq.addWidget(self.widgetGrafLong)
        