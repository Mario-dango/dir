from app.src.model.archivosExcel import ExcelModel
from app.src.view.widgets import WidgetsGraf
import pandas as pd
class ControlTransversal():
    
    def __init__(self, model):
        self.transversalModel = model
        self.transversalView = None
        self.data = pd.DataFrame()
        

    def setup(self):
        dataCotaProgesiva = self.data['progresiva'].tolist()
        dataRazante = self.data["razante"].tolist()
        dataTerrenoMedio = self.data["tm"].tolist()
        self.transversalView = WidgetsGraf(dataCotaProgesiva, dataRazante, dataTerrenoMedio)
        self.cid_press = self.transversalView.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_release = self.transversalView.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_move = self.transversalView.canvas.mpl_connect('motion_notify_event', self.on_move)

    def on_click(self, event):
        # print("estoy en On_click")
        if event.inaxes == self.transversalView.razante:
            xdata = self.transversalView.line.get_xdata()
            ydata = self.transversalView.line.get_ydata()

            # Verificar la distancia con los puntos
            for i, (x, y) in enumerate(zip(xdata, ydata)):
                distance = ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                if distance < 0.1:  # Valor de tolerancia para seleccionar el punto
                    self.transversalView.selected_point = i
                    self.transversalView.lbl_previous.setText(f'Posición anterior: ({x:.2f}, {y:.2f})')
                    break

    def on_release(self, event):
        # print("estoy en on_release")
        self.transversalView.selected_point = None

    def on_move(self, event):
        # print("estoy en on_move")
        if self.transversalView.selected_point is not None:
            if event.inaxes == self.transversalView.razante:
                new_y = self.transversalView.hRazante.copy()
                new_y[self.transversalView.selected_point] = event.ydata
                self.transversalView.line.set_ydata(new_y)
                self.transversalView.lbl_new.setText(f'Nueva posición: ({self.transversalView.progresiva[self.transversalView.selected_point]:.2f}, {event.ydata:.2f})')
                self.transversalView.canvas.draw()
    
            
    def mostrarData(self):
        pass
            