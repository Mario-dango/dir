import sys
from PyQt5.QtWidgets import QApplication
from app.src.controller.controladorPrincipal import mainController

if __name__ == '__main__':
    print("Iniciando Sistema")
    #Instancia para iniciar una aplicación
    app = QApplication(sys.argv)
    controlador = mainController()
    #Ejecutar la aplicación
    sys.exit(app.exec_())