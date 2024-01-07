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
        if mainWindow is None:
            self.ventanaPrincipal = VentanaPrincipal()
        else:
            self.ventanaPrincipal = mainWindow
        self.qFile = FileManager()
        self.modelExcel = ExcelModel()
        self.longitudinalController = ControlLongitudinal(self.modelExcel)
        self.transversalController = ControlTransversal(self.modelExcel)
        self.ventanaArte = VentanaArte()

        self.setup()
        
    def setup(self):
        
        #cargar datos de prueba
        pathDefault = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/dataTest.csv"
        dataDefault = self.modelExcel.leerData(pathDefault)
        pathDefault = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/perfilRuta.csv"
        dataTransDefault = self.modelExcel.leerData(pathDefault)
        # print("Los datos leído son:\n %s" % dataDefault)
        # print(dataDefault.loc[1]) 
        # print(type(pathDefault))  # Verifica el tipo de pathDefault
            
        medias = {"tm": []}
        for i in range(len(dataDefault)):
            rowData = dataDefault.loc[i]
            media = rowData[2:].mean().round(2)
            medias["tm"].append(media)

        dataDefault['tm'] = medias["tm"]
        dataLong = dataDefault.iloc[:, [0, 1, -1]].copy()
        # dataTrans = dataDefault.iloc[:, [0, 1, -1]].copy()
        dataTrans = dataDefault.iloc[:,0:-1].copy()
        # print(medias)
        # print(dataLong['tm'])
        self.longitudinalController.data = dataLong
        self.longitudinalController.setup()
        self.transversalController.dataPerfil = dataTransDefault
        self.transversalController.data = dataTrans
        self.transversalController.setup()
        
        #Mostrar la ventana
        self.ventanaPrincipal.show()
        
        self.ventanaPrincipal.initUI(self.longitudinalController.longitudinalView, self.transversalController.transversalView)
        self.ventanaPrincipal.btnUpload.clicked.connect(self.cargar)
        self.ventanaPrincipal.btnSave.clicked.connect(self.guardar)
        self.ventanaPrincipal.btnConfig.clicked.connect(self.obraArte)
        
        
        self.cid_press = self.longitudinalController.longitudinalView.canvas.mpl_connect('button_press_event', self.on_click_long)
        self.cid_release = self.longitudinalController.longitudinalView.canvas.mpl_connect('button_release_event', self.on_release_long)
        self.cid_move = self.longitudinalController.longitudinalView.canvas.mpl_connect('motion_notify_event', self.on_move_long)
        self.cid_press = self.transversalController.transversalView.canvas.mpl_connect('button_press_event', self.on_click_trans)
        self.cid_release = self.transversalController.transversalView.canvas.mpl_connect('button_release_event', self.on_release_trans)
        self.cid_move = self.transversalController.transversalView.canvas.mpl_connect('motion_notify_event', self.on_move_trans)
        
        
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
            print(fileName[-4:])
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
    
    def updateTransInfo(self, dataSelect=None):
        if dataSelect is not None:
            #cambiar datos en grafico transversal
            pass
        else: 
            ##llamar al controlador transversal
            # self.transversalController.updateData(self.nodoId)
            # self.ventanaPrincipal.updateTransInfo(self.transversalController.data)
            pass
    
    def setInfo(self, data):
        self.ventanaPrincipal.updateInfo(data)
        pass
            
        
    def on_click_trans(self, event):
        pass

    def on_release_trans(self, event):
        pass

    def on_move_trans(self, event):
        pass
    
    def on_click_long(self, event):
        if self.longitudinalController.longitudinalView.selected_point is not None:
            alturaRazante = self.longitudinalController.longitudinalView.hRazante[self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]]
            progresiva = self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]
            alturaTerreno = self.longitudinalController.longitudinalView.hTerreno[self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]]
            diferencia = alturaRazante - alturaTerreno
            self.transversalController.acutalizarGrafico(progresiva)
            dataText = (
            f"[Progresiva Número: {progresiva}\n"
            f"[Cota Número: {progresiva}]\n"
            f"[Altura de Ruta: {alturaRazante:.2f}m]\n"
            f"[Altura de Terreno Natural: {alturaTerreno:.2f}m]\n"
            f"[Diferencia: {diferencia:.2f}m] ")
            self.updateTransInfo(progresiva)
            self.ventanaPrincipal.updateTransInfo(dataText)
        else:
            pass

    def on_release_long(self, event):
        pass

    def on_move_long(self, event):
        if self.longitudinalController.longitudinalView.selected_point is not None:
            alturaRazante = self.longitudinalController.longitudinalView.hRazante[self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]]
            progresiva = self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]
            alturaTerreno = self.longitudinalController.longitudinalView.hTerreno[self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]]
            diferencia = alturaRazante - alturaTerreno
            self.transversalController.data.iat[progresiva, 1] = self.longitudinalController.longitudinalView.hRazante[self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]]
            self.transversalController.acutalizarGrafico(progresiva)
            dataText = (
            f"[Progresiva Número: {progresiva}\n"
            f"[Cota Número: {progresiva}]\n"
            f"[Altura de Ruta: {alturaRazante:.2f}m]\n"
            f"[Altura de Terreno Natural: {alturaTerreno:.2f}m]\n"
            f"[Diferencia: {diferencia:.2f}m] ")           

            self.ventanaPrincipal.updateTransInfo(dataText)
        else:
            pass