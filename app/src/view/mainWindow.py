# -*- coding: utf-8 -*-
# # from controllers import main_controller
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        # cargar la interfaz de usuario desde el archivo ui generado por Qt Designer
        uic.loadUi('../../resources/ui/mainwindow.ui', self)
        self.setWindowTitle("Sistema de viabilidad de ruta")
        self.setMinimumSize(800,600)
        self.setMaximumSize(1920,1080)
