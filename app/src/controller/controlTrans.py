# -*- coding: utf-8 -*-
##### LIBRERIAS Y DEPENDENCIAS NECESARIAS PARA LA CLASE #####
from app.src.model.archivosExcel import ExcelModel
from app.src.view.widgets import WidgetsGraf
import pandas as pd
import numpy as np
################################################################

## CLASE DEFINIDA DEL CONTROLADOR TRANSVERSAL ##
class ControlTransversal():
    
    ## MÉTODO CONSTRUCTOR DE LA CLASE TRANSVERSAL
    def __init__(self):
        self.transversalView = None         ## Widget del grafico para el perfil transeversal
        self.dataPerfilesLista = []         ## Lista con los dataFrame de los perfiles transversales
        self.valorActualRazante = None      ## Valor actual de la razante para un perfil transversal dado
        self.dataPerfil = pd.DataFrame()    ## DataFrame del perfil transvers actual
        ## Datos de default para los calculos del perfil
        self.dataCalculo = {
            "Ancho Trocha": 3.65,           ## [m]
            "Ancho Banquina": 1.2,          ## [m]
            "Distancia al plano": 10,       ## [m]
            "Pendiente Transversal": 2,     ## [%]
            "Pendiente Banquina": 2.5,      ## [%]
            "Pendiente Talud": 1,           ## [(lateral)en(lateral)]
            "Paquete Estructural": 0.7      ## [m]
        }        

    ## MÉTODO PARA LA CONFIGURACIÓN DE LA CLASE
    def setup(self):
        
        dataCotaProgesiva = self.dataPerfilesLista[0]['DISTANCIA (PROGRESIVA)'].tolist()
        # dataRuta = self.dataPerfilesLista[0]['DISTANCIA (PROGRESIVA)'].tolist()
        dataTerreno = self.dataPerfilesLista[0]['COTA'].tolist()
        ## Para generar el grafico necesito enviarle los datos en forma de Listas
        self.transversalView = WidgetsGraf(dataCotaProgesiva, None, dataTerreno)
        self.cid_press = self.transversalView.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_release = self.transversalView.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_move = self.transversalView.canvas.mpl_connect('motion_notify_event', self.on_move)

    def generacionPerfil(self):
        pass

    def on_click(self, event):
        # print("estoy en On_click")
        if event.inaxes == self.transversalView.razante:
            xdata = self.transversalView.lineRazante.get_xdata()
            ydata = self.transversalView.lineRazante.get_ydata()

            # Verificar la distancia con los puntos
            for i, (x, y) in enumerate(zip(xdata, ydata)):
                distance = ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                if distance < 0.5:  # Valor de tolerancia para seleccionar el punto
                    self.transversalView.selected_point = i
                    self.transversalView.lbl_previous.setText(f'Posición anterior: ({x:.2f}, {y:.2f})')
                    break
                
    def acutalizarGrafico(self, progresiva):
        dataTerreno = {"nodoT": []}
        # For para acomodar las columans a fila y agregarlas ald ataframe self.dataPerfil
        for j in range(len(self.data.columns[2:])):
            columna_actual = self.data.iloc[progresiva, j+2]  # Obtener la columna actual por su índice numérico
            dataTerreno["nodoT"].append(columna_actual)  # Agregar los valores al final de la lista
        # print(f"longitud de columnas: {len(self.data.columns[2:])}")
        # print(f"longitud de array dataTerreno: {len(dataTerreno['nodoT'])}")
        # print(f"longitud de array dataTerreno: {len(self.dataPerfil['cotas'])}")
        dataColum = np.array(dataTerreno["nodoT"]).reshape(-1, 1)  # Transformar en vector columna
        self.dataPerfil['nodosT'] = dataColum        
        # Convierto los dataframe en lsitas para los gráficos
        dataTerreno = self.dataPerfil["nodosT"].tolist()   
        # Establece los nuevos datos de altura en la línea del gráfico de la vista transversal
        self.transversalView.lineTerreno.set_ydata(dataTerreno)
        # Actualiza el texto en la etiqueta lbl_new con la nueva posición del punto
        # self.transversalView.lbl_new.setText(f'Nueva posición: ({self.transversalView.progresiva[self.transversalView.selected_point]:.2f}, {event.ydata:.2f})')
        # Vuelve a dibujar la vista transversal para mostrar los cambios
        # self.transversalView.canvas.draw()
        self.actualizarPerfil(progresiva)

    def actualizarPerfil(self, prograsiva ):
        print("estoy en actualizar perfil")
        ###########################3333 Problema al graficar 
        valorDeRazanteData = self.data.iat[prograsiva,1]
        self.valorActualRazante = self.dataPerfil.iat[20,1]
        diferenciaDeAlturas = float(valorDeRazanteData) - float(self.valorActualRazante)
        # print(self.dataPerfil['nodosR'])
        # Convertir la columna a valores flotantes usando
        self.dataPerfil['nodosR'] = pd.to_numeric(self.dataPerfil['nodosR'], errors='coerce')
        # For para acomodar el perfil de ruta
        # print(self.dataPerfil)
        for i in range(len(self.dataPerfil["cotas"])):
            # if i ==6 or i ==8:
            #     print(self.dataPerfil.iat[i, 1])
            self.dataPerfil.iat[i, 1] = float(self.dataPerfil.iat[i, 1]) + diferenciaDeAlturas
        self.valorActualRazante = self.dataPerfil.iat[20,1]
        # print(self.dataPerfil["nodosR"])
        dataRuta = self.dataPerfil["nodosR"].tolist()        
        # print(dataRuta)
        # Establece los nuevos datos de altura en la línea del gráfico de la vista transversal
        self.transversalView.lineRazante.set_ydata(dataRuta)
        # Actualiza el texto en la etiqueta lbl_new con la nueva posición del punto
        # self.transversalView.lbl_new.setText(f'Nueva posición: ({self.transversalView.progresiva[self.transversalView.selected_point]:.2f}, {event.ydata:.2f})')
        # Vuelve a dibujar la vista transversal para mostrar los cambios
        self.transversalView.canvas.draw()
            
        

    def on_release(self, event):
        # print("estoy en on_release")
        self.transversalView.selected_point = None
    def on_move(self, event):
        # Verifica si hay un punto seleccionado en la vista transversal
        if self.transversalView.selected_point is not None:
            # Verifica si el evento está ocurriendo dentro del eje "razante" en la vista transversal
            if event.inaxes == self.transversalView.razante:
                # Copia los datos de alturas del razante
                new_y = self.transversalView.hRazante.copy()
                # Actualiza la altura del punto seleccionado en la copia de los datos con el nuevo valor
                new_y[self.transversalView.selected_point] = event.ydata
                # Establece los nuevos datos de altura en la línea del gráfico de la vista transversal
                self.transversalView.line.set_ydata(new_y)
                # Actualiza el texto en la etiqueta lbl_new con la nueva posición del punto
                self.transversalView.lbl_new.setText(f'Nueva posición: ({self.transversalView.progresiva[self.transversalView.selected_point]:.2f}, {event.ydata:.2f})')
                # Vuelve a dibujar la vista transversal para mostrar los cambios
                self.transversalView.canvas.draw()

    
            
    def mostrarData(self):
        pass
            