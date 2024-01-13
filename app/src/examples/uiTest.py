# -*- coding: utf-8 -*-
# # from controllers import main_controller
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

app = QApplication([])

pathUi = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/ui/configLoad.ui"
# pathUi = "/SER/app/src/view/mainwindow.ui"
# cargar la interfaz de usuario desde el archivo ui generado por Qt Designer
windowUI = uic.loadUi(pathUi)
windowUI.setWindowTitle("Sistema de viabilidad de ruta")
        

windowUI.show()
#Ejecutar la aplicación
app.exec_()
