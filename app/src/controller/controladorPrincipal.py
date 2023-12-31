from app.src.controller import controlLong
from app.src.controller import controlTrans
from app.src.view.mainWindow import 

class mainController():
    
    def __init__(self):
        self.longitudinalController = controlLong()
        self.transversalController = controlTrans()
        self.mainWindow = None
        self.setup()
        
    def setup(self):
        pass