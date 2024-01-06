from app.src.controller.controlLong import ControlLongitudinal
from app.src.controller.controlTrans import ControlTransversal
from app.src.model.archivosExcel import ExcelModel
from app.src.view.mainWindow import VentanaPrincipal, VentanaArte
from app.src.view.widgets import FileManager
from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainController(QObject):
    
    def __init__(self, mainWindow = None):
        super().__init__()
        # self.ventanaPrincipal = mainWindow
        self.ventanaPrincipal = VentanaPrincipal()
        self.qFile = FileManager()
        self.modelExcel = ExcelModel()
        self.longitudinalController = ControlLongitudinal(self.modelExcel)
        self.transversalController = ControlTransversal(self.modelExcel)
        self.ventanaArte = VentanaArte()
        ## interactive part
        
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.selected_point = None  # Punto seleccionado
        self.offset = 0  # Offset del desplazamiento

        self.setup()
        
    def setup(self):
        
        #cargar datos de prueba
        pathDefault = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/dataTest.csv"
        dataDefault = self.modelExcel.leerData(pathDefault)
        print(dataDefault.loc[1])
        print(type(pathDefault))  # Verifica el tipo de pathDefault
            
        medias = {"tm": []}
        for i in range(len(dataDefault)):
            rowData = dataDefault.loc[i]
            media = rowData[2:].mean().round(2)
            medias["tm"].append(media)

        dataDefault['tm'] = medias["tm"]
        dataLong = pd.DataFrame()
        print(medias)
            
        
        # # Conectar la señal mouseMoveEvent al método correspondiente
        # self.transversalController.transversalView.chart_view.mouseMoveEvent = self.mouseMoveEvent
        # self.transversalController.transversalView.chart_view.setMouseTracking(True)  # Habilitar el seguimiento del cursor
        
        # # Conectar la señal mouseMoveEvent al método correspondiente
        # self.longitudinalController.longitudinalView.chart_view.mouseMoveEvent = self.mouseMoveEvent
        # self.longitudinalController.longitudinalView.chart_view.setMouseTracking(True)  # Habilitar el seguimiento del cursor
        
        #Mostrar la ventana
        self.ventanaPrincipal.show()
        
        self.ventanaPrincipal.initUI(self.longitudinalController.longitudinalView, self.transversalController.transversalView)
        self.ventanaPrincipal.btnUpload.clicked.connect(self.cargar)
        self.ventanaPrincipal.btnSave.clicked.connect(self.guardar)
        self.ventanaPrincipal.btnConfig.clicked.connect(self.obraArte)
        
        self.cid_press = self.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_release = self.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_move = self.canvas.mpl_connect('motion_notify_event', self.on_move)
        
        self.setInfo("""
Repositorio GitHub: https://github.com/Mario-dango/dir
Autores:     Gerardo
                Mario Papetti Funes
Link del Manual: https://github.com/Mario-dango/dir/userManual
Versión: v0.2.4""")
        
    def cargar(self):
        print("Cargando el archivo")
        fileName = self.qFile.open("cargar")
        if fileName is not None:
            if fileName[-4:] != '.csv':
                print("favor de usar formato .CSV")
            else:
                self.longitudinalController.path = fileName
                self.longitudinalController.loadCsv()
                
    def guardar(self):
        try:
            name = self.qFile.open("guardar")
            data = self.longitudinalController.data
            with open(name, "w") as csv:
                csv.write(data)
            print("se logró guarda el archivo de informe")
        except Exception as e:
            print(f"Error al guardar el archivo de informe: {e}")
        finally:          
            pass
    
    def obraArte(self):
        ## Calculo y seteo de configuraciones de obra de arte
        pass
    
    def updateLongInfo(self, default=None):
        if default is None:
            dataDefault = self.longitudinalController.longitudinalModel.leerData()
            self.longitudinalController.longitudinalView.updateData(dataDefault)
        ##llamar al controlador Longitudinal
        # self.asdasdasdasdas.updateData(self.nodoId)
        # self.ventanaPrincipal.updateTransInfo(self.longiasdasdasdasdasd.data)
        pass
    
    def updateTransInfo(self):
        ##llamar al controlador transversal
        # self.transversalController.updateData(self.nodoId)
        # self.ventanaPrincipal.updateTransInfo(self.transversalController.data)
        pass
    
    def setInfo(self, data):
        self.ventanaPrincipal.updateInfo(data)
        pass
            
        
    def on_click(self, event):
        print("estoy en on_click")
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
        print("estoy en on_release")
        self.selected_point = None

    def on_move(self, event):
        print("estoy en on_move")
        if self.selected_point is not None:
            if event.inaxes == self.ax:
                new_y = self.y.copy()
                new_y[self.selected_point] = event.ydata
                self.line.set_ydata(new_y)
                self.lbl_new.setText(f'Nueva posición: ({self.x[self.selected_point]:.2f}, {event.ydata:.2f})')
                self.canvas.draw()
