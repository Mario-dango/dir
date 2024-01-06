import sys
from PyQt5.QtWidgets import QApplication
from app.src.controller.controladorPrincipal import MainController
from app.src.view.mainWindow import VentanaPrincipal

if __name__ == '__main__':
    print("Iniciando Sistema")
    #Instancia para iniciar una aplicación
    app = QApplication(sys.argv)
    # ventana = VentanaPrincipal()
    # controlador = MainController(ventana)
    # ventana.show()
    controlador = MainController()
    #Ejecutar la aplicación
    sys.exit(app.exec_())