from app.src.model.archivosExcel import ExcelModel
from app.src.view.widgets import WidgetsGraf
class ControlTransversal():
    
    def __init__(self, model):
        self.transversalModel = model
        self.transversalView = None
        self.path = None
        self.data = []
        self.setup()
        
    def setup(self):
        self.transversalView = WidgetsGraf("trans")
        pass
    
    def loadCsv(self, path=None):
        #cargar datos y mostrarlos
        self.path = path
        if self.path is not None:
            self.transversalModel.leerData()
            self.mostrarData()
        else:
            print("error")
            
    def mostrarData(self):
        pass
            