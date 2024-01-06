from app.src.model.archivosExcel import ExcelModel
from app.src.view.widgets import WidgetsGraf
class ControlLongitudinal():
    
    def __init__(self, model):
        self.longitudinalModel = model
        self.longitudinalView = None
        self.path = None
        self.data = []
        self.setup()
        
    def setup(self):
        self.longitudinalView = WidgetsGraf("long")
        pass
    
    def loadCsv(self, path=None):
        #cargar datos y mostrarlos
        self.path = path
        if self.path is not None:
            self.longitudinalModel.leerData()
            self.mostrarData()
        else:
            print("error")
            
    def mostrarData(self):
        self.longitudinalView.updateData()
        pass
            