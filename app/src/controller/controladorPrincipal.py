# -*- coding: utf-8 -*-
##### LIBRERIAS Y DEPENDENCIAS NECESARIAS PARA LA CLASE #####
from app.src.controller.controlLong import ControlLongitudinal
from app.src.controller.controlTrans import ControlTransversal
from app.src.model.archivosExcel import PlanillaModel
from app.src.view.mainWindow import VentanaPrincipal, VentanaArte
from app.src.view.widgets import FileManager, VentanaEmergenteExcel
from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
################################################################


## CLASE DEFINIDA DEL CONTROLADOR PRINCIPAL ##
class MainController(QObject):
    
    ## MÉTODO CONSTRUCTOR DE LA CLASE PRINCIPAL
    def __init__(self, mainWindow = None):
        super().__init__()
        ##  Si la ventana no es pasada cómo parametro, crear objeto ventana principal
        if mainWindow is None:
            self.ventanaPrincipal = VentanaPrincipal()
        else:
            self.ventanaPrincipal = mainWindow
        self.qFile = FileManager()                                  ##
        self.planillaManager = PlanillaModel()                      ##
        self.longitudinalController = ControlLongitudinal()    ##
        self.transversalController = ControlTransversal()      ##
        self.ventanaArte = VentanaArte()                            ##
        self.ventanaPaqueteEstructural = None                       ##
        self.ventanaDatos = VentanaEmergenteExcel()                 ##
        ## Llamado al método de configuración de inicio para la clase
        self.setup()
        
        
    ## MÉTODO PARA LA CONFIGURACIÓN DE LA CLASE
    def setup(self):
        ## Defino la ruta de default del archivo de ejemplo a cargar
        pathDefault = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/planillaTest.xlsx"
        ## Leo el archivo entero y almaceno la data formateada dentro de los atributos del objeto planillaManager 
        #### {Datos para perfil longitudinal} <=> self.planillaManager.dataLongitudinal = pd.DataFrame()
        #### {Datos para perfil transversal} <=> self.planillaManager.dataTransversal = []
        self.planillaManager.leerData(pathDefault, "Datos")     ## leo el archivo de ruta "pathDefault" en la hoja de nombre "Datos"
        ## Hago el transpase de los datos a los atributos de los objetos correspondientes para sus tratamientos
        self.longitudinalController.data = self.planillaManager.dataLongitudinal                ## Le paso un DataFrame
        self.transversalController.dataPerfilesLista = self.planillaManager.dataTransversal     ## Le paso una lista de DataFrames 
        # Conectar el clic del botón OK al método correspondiente
        self.ventanaDatos.buttonBox.accepted.connect(self.accepted) # type: ignore
        self.ventanaDatos.buttonBox.rejected.connect(self.rejected) # type: ignore       
        ##  Comienzo las configuraciones de los objetos pertenecientes a los controladores de los perfiles
        self.longitudinalController.setup()     ## Controlador Lonitudinal
        self.transversalController.setup()      ## Controlador Transversal           
        self.ventanaPrincipal.show()            ## Mostrar la ventana principal     
        ## Inicializar los elementos de la ventana Principal con los gráficos longitudinal y transversal en progresiva 0
        self.ventanaPrincipal.initUI(self.longitudinalController.longitudinalView, self.transversalController.transversalView)
        self.ventanaPrincipal.btnUpload.clicked.connect(self.cargar)
        self.ventanaPrincipal.btnSave.clicked.connect(self.guardar)
        self.ventanaPrincipal.btnConfig.clicked.connect(self.obraArte)    
        self.ventanaPrincipal.btnEstructural.clicked.connect(self.paqueteEstructural)        
        ## Definir los conectores de eventos para cada gráfico, dando la interactividad necesaria
        self.cid_press = self.longitudinalController.longitudinalView.canvas.mpl_connect('button_press_event', self.on_click_long)
        self.cid_release = self.longitudinalController.longitudinalView.canvas.mpl_connect('button_release_event', self.on_release_long)
        self.cid_move = self.longitudinalController.longitudinalView.canvas.mpl_connect('motion_notify_event', self.on_move_long)
        self.cid_press = self.transversalController.transversalView.canvas.mpl_connect('button_press_event', self.on_click_trans)
        self.cid_release = self.transversalController.transversalView.canvas.mpl_connect('button_release_event', self.on_release_trans)
        self.cid_move = self.transversalController.transversalView.canvas.mpl_connect('motion_notify_event', self.on_move_trans)
        ## Seteo de data de información "AboutUs" del proyecto
        self.setInfo("""
Repositorio GitHub: https://github.com/Mario-dango/dir
Autores:     Gerardo
                Mario Papetti Funes
Link del Manual: https://github.com/Mario-dango/dir/userManual
Versión: v0.2.4""")
        
    ## MÉTODO PARA EL CARGADO DEL ARCHIVO PARA LA EXTRACIÓN DE LA DATA
    def cargar(self):
        print("Cargando el archivo")
        fileName = self.qFile.open("cargar")
        if fileName is not None:
            print(fileName[-4:])
            # if fileName[-4:] != '.csv':
            #     print("favor de usar formato .CSV")
            # else:
            #     self.longitudinalController.path = fileName
            #     self.longitudinalController.loadCsv()
            
            self.planillaManager.leerData(fileName, "Datos")
            self.ventanaDatos.show()
            
    ## MÉTODO PARA EL GENERACIÓN Y GUARDADO DE INFORME
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
    
    ## MÉTODO PARA LA CONFIGURACIÓN DE LAS OBRAS DE ARTE
    def obraArte(self):
        ## Gestión de las configuraciones de obra de arte
        pass
    
    ## MÉTODO PARA LA CONFIGURACIÓN y CÁLCULOS DEL PAQUETE ESTRUCTURAL
    def paqueteEstructural(self):
        ## Gestión de calculos para el paquete estructural del perfil transversal
        pass
    
    ## MÉTODO PARA EL FORMATEO DE DATA NECESARIA EN EL PERFIL TRANSVERSAL
    def accepted(self):
        ## Guardo los datos ingresados en variables tomados desde la ventana emergente
        datoAnchuraDeTrocha = self.ventanaDatos.leAnchTroch.text()
        datoPendienteTransversal = self.ventanaDatos.lePendTroch.text()
        datoAnchoBanquina = self.ventanaDatos.leAnchBanq.text()
        datoPendienteBanquina = self.ventanaDatos.lePendBanq.text()
        datoPendienteTalud = self.ventanaDatos.lePendTalud.text()
        datoDistanciaReferencia = self.ventanaDatos.leDist.text()
        ## Limpió el array de datos generales para la generación del perfil para luego cargar los datos ingresados
        self.transversalController.dataGeneral.clear()
        self.transversalController.dataGeneral.append(datoAnchuraDeTrocha)
        self.transversalController.dataGeneral.append(datoPendienteTransversal)
        self.transversalController.dataGeneral.append(datoAnchoBanquina)
        self.transversalController.dataGeneral.append(datoPendienteBanquina)
        self.transversalController.dataGeneral.append(datoPendienteTalud)
        self.transversalController.dataGeneral.append(datoDistanciaReferencia)
        ## Cierro la ventana emergente
        self.ventanaDatos.close()
        
    def rejected(self):
        pass
        
    ## MÉTODO PARA LA ACTUALIZACIÓN GENERAL DE DATOS ACERCA VOLUMENES Y ÁREAS
    def updateData(self, dataSelect=None):
        if dataSelect is not None:
            #cambiar datos en grafico transversal
            pass
        else: 
            ##llamar al controlador transversal
            # self.transversalController.updateData(self.nodoId)
            # self.ventanaPrincipal.updateTransInfo(self.transversalController.data)
            pass
    
    ## MÉTODO CONECTOR DE EVENTO CLICK GRAFICO TRANSVERSAL
    def setInfo(self, data):
        self.ventanaPrincipal.updateInfo(data)
        pass
                    
    ## MÉTODO CONECTOR DE EVENTO CLICK GRAFICO TRANSVERSAL
    def on_click_trans(self, event):
        pass

    ## MÉTODO CONECTOR DE EVENTO LIBERAR GRAFICO TRANSVERSAL
    def on_release_trans(self, event):
        pass

    ## MÉTODO CONECTOR DE EVENTO MOVER GRAFICO TRANSVERSAL
    def on_move_trans(self, event):
        pass
        
    ## MÉTODO CONECTOR DE EVENTO CLICK GRAFICO LONGITUDINAL
    def on_click_long(self, event):
        if self.longitudinalController.longitudinalView.selected_point is not None:
            ## Extracción de datos para mostrarlos en el lateral derecho
            print(f"Punto seleccionado: {self.longitudinalController.longitudinalView.selected_point}")
            alturaRazante = self.longitudinalController.longitudinalView.hRazante[self.longitudinalController.longitudinalView.selected_point]
            progresiva = self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]
            alturaTerreno = self.longitudinalController.longitudinalView.hTerreno[self.longitudinalController.longitudinalView.selected_point]
            diferencia = alturaRazante - alturaTerreno
            # pendiente = self.longitudinalController.data.loc["Pendiente", self.longitudinalController.data.columns[self.longitudinalController.longitudinalView.selected_point]]
            pendiente ="NONE"
            ## Actualizo grafico de perfil Transversal
            self.transversalController.acutalizarGrafico(int(self.longitudinalController.longitudinalView.selected_point))
            ## Formateo los Datos para ser mostrados en el grafico Longitudinal
            dataText = (
            f"[Progresiva: {progresiva}m]\n"
            f"[Cota de Terreno: {alturaTerreno:.4f}m]\n"
            f"[Cota de Proyecto: {alturaRazante:.4f}m]\n"
            f"[Diferencia entre Cotas: {diferencia:.4f}m]\n"
            f"[Pendiente: {pendiente}m] ")
            ## Actualizo Datos mostrados acerca del grafico Longitudinal
            self.ventanaPrincipal.updateTransInfo(dataText)
        else:
            pass

    ## MÉTODO CONECTOR DE EVENTO LIBERAR GRAFICO LONGITUDINAL
    def on_release_long(self, event):
        pass

    ## MÉTODO CONECTOR DE EVENTO MOVER GRAFICO LONGITUDINAL
    def on_move_long(self, event):
        if self.longitudinalController.longitudinalView.selected_point is not None:
            ## Extracción de datos para mostrarlos en el lateral derecho
            alturaRazante = self.longitudinalController.longitudinalView.hRazante[self.longitudinalController.longitudinalView.selected_point]
            progresiva = self.longitudinalController.longitudinalView.progresiva[self.longitudinalController.longitudinalView.selected_point]
            alturaTerreno = self.longitudinalController.longitudinalView.hTerreno[self.longitudinalController.longitudinalView.selected_point]
            diferencia = alturaRazante - alturaTerreno
            # pendiente = self.longitudinalController.data.loc["Pendiente", self.longitudinalController.data.columns[self.longitudinalController.longitudinalView.selected_point]]
            pendiente ="NONE"
            ## Actualizo grafico de perfil Transversal
            # self.transversalController.data.iat[progresiva, 1] = self.longitudinalController.longitudinalView.hRazante[self.longitudinalController.longitudinalView.selected_point]
            self.transversalController.acutalizarGrafico(int(self.longitudinalController.longitudinalView.selected_point))
            ## Formateo los Datos para ser mostrados en el grafico Longitudinal
            dataText = (
            f"[Progresiva: {progresiva}m]\n"
            f"[Cota de Terreno: {alturaTerreno:.4f}m]\n"
            f"[Cota de Proyecto: {alturaRazante:.4f}m]\n"
            f"[Diferencia entre Cotas: {diferencia:.4f}m]\n"
            f"[Pendiente: {pendiente}m] ")
            ## Actualizo Datos mostrados acerca del grafico Longitudinal
            self.ventanaPrincipal.updateTransInfo(dataText)
        else:
            pass