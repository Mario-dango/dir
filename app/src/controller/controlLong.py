from app.src.model.archivosExcel import ExcelModel
from app.src.view.widgets import WidgetsGraf

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ControlLongitudinal():
    
    def __init__(self, model):
        self.longitudinalModel = model
        self.longitudinalView = None
        self.data = pd.DataFrame()
        
    def setup(self):
        print(f"Los datos son: \n{self.data}")
        if self.data is not None:
            dataProgesiva = self.data['progresiva'].tolist()
            dataRazante = self.data["razante"].tolist()
            dataTerrenoMedio = self.data["tm"].tolist()
            self.longitudinalView = WidgetsGraf(dataProgesiva, dataRazante, dataTerrenoMedio)
            self.cid_press = self.longitudinalView.canvas.mpl_connect('button_press_event', self.on_click)
            self.cid_release = self.longitudinalView.canvas.mpl_connect('button_release_event', self.on_release)
            self.cid_move = self.longitudinalView.canvas.mpl_connect('motion_notify_event', self.on_move)

    def on_click(self, event):
        # print("estoy en On_click")
        if event.inaxes == self.longitudinalView.razante:
            xdata = self.longitudinalView.line.get_xdata()
            ydata = self.longitudinalView.line.get_ydata()

            # Verificar la distancia con los puntos
            for i, (x, y) in enumerate(zip(xdata, ydata)):
                distance = ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                if distance < 0.5:  # Valor de tolerancia para seleccionar el punto
                    self.longitudinalView.selected_point = i
                    self.longitudinalView.lbl_previous.setText(f'Valor de Progresiva: {self.longitudinalView.progresiva[self.longitudinalView.selected_point]}| Altura de razante anterior: {y:.2f}')
                    break

    def on_release(self, event):
        # print("estoy en on_release")
        self.longitudinalView.selected_point = None

    def on_move(self, event):
        # print("estoy en on_move")
        if self.longitudinalView.selected_point is not None:
            if event.inaxes == self.longitudinalView.razante:
                new_y = self.longitudinalView.hRazante.copy()
                new_y[self.longitudinalView.selected_point] = event.ydata
                self.longitudinalView.line.set_ydata(new_y)
                self.longitudinalView.lbl_new.setText(f'Valor de Progresiva: {self.longitudinalView.progresiva[self.longitudinalView.selected_point]}| Altura de razante nueva: {event.ydata:.2f}')
                self.longitudinalView.hRazante[self.longitudinalView.progresiva[self.longitudinalView.selected_point]] = event.ydata
                self.longitudinalView.canvas.draw()
    
    def updateData(self):
        
        pass
    
                
    def mostrarData(self):
        self.longitudinalView.updateData()
        pass
            