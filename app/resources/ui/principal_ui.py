# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mprob\Documents\Proyectos\Sistema de Estimacion de Rutas\SER\app\resources\ui\principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1058, 686)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777214, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background: rgb(123, 158, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.titulo = QtWidgets.QLabel(self.frame)
        self.titulo.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.gridLayout.addWidget(self.titulo, 0, 0, 1, 2)
        self.frameDer = QtWidgets.QFrame(self.frame)
        self.frameDer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDer.setObjectName("frameDer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameDer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnUpload = QtWidgets.QPushButton(self.frameDer)
        self.btnUpload.setMinimumSize(QtCore.QSize(100, 30))
        self.btnUpload.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnUpload.setFont(font)
        self.btnUpload.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background: rgb(0,85,255);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(52, 116, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(70, 184, 255);\n"
"}")
        icon = QtGui.QIcon.fromTheme("accessories-calculator")
        self.btnUpload.setIcon(icon)
        self.btnUpload.setDefault(True)
        self.btnUpload.setFlat(False)
        self.btnUpload.setObjectName("btnUpload")
        self.verticalLayout_4.addWidget(self.btnUpload)
        self.btnSave = QtWidgets.QPushButton(self.frameDer)
        self.btnSave.setMinimumSize(QtCore.QSize(100, 30))
        self.btnSave.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnSave.setFont(font)
        self.btnSave.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background: rgb(0,85,255);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(52, 116, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(70, 184, 255);\n"
"}")
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_4.addWidget(self.btnSave)
        self.btnConfig = QtWidgets.QPushButton(self.frameDer)
        self.btnConfig.setMinimumSize(QtCore.QSize(100, 30))
        self.btnConfig.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnConfig.setFont(font)
        self.btnConfig.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background: rgb(0,85,255);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background: rgb(52, 116, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background: rgb(70, 184, 255);\n"
"}")
        self.btnConfig.setObjectName("btnConfig")
        self.verticalLayout_4.addWidget(self.btnConfig)
        self.verticalLayout_4.setStretch(2, 10)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.dataGrafTrans = QtWidgets.QLabel(self.frameDer)
        self.dataGrafTrans.setMinimumSize(QtCore.QSize(0, 0))
        self.dataGrafTrans.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dataGrafTrans.setFont(font)
        self.dataGrafTrans.setStyleSheet("")
        self.dataGrafTrans.setObjectName("dataGrafTrans")
        self.verticalLayout.addWidget(self.dataGrafTrans)
        self.dataGeneral = QtWidgets.QLabel(self.frameDer)
        self.dataGeneral.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dataGeneral.setFont(font)
        self.dataGeneral.setObjectName("dataGeneral")
        self.verticalLayout.addWidget(self.dataGeneral)
        self.dataInfo = QtWidgets.QLabel(self.frameDer)
        self.dataInfo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dataInfo.setFont(font)
        self.dataInfo.setObjectName("dataInfo")
        self.verticalLayout.addWidget(self.dataInfo)
        self.gridLayout.addWidget(self.frameDer, 1, 1, 1, 1)
        self.frameIzq = QtWidgets.QFrame(self.frame)
        self.frameIzq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameIzq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameIzq.setObjectName("frameIzq")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameIzq)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titGrafLong = QtWidgets.QLabel(self.frameIzq)
        self.titGrafLong.setMinimumSize(QtCore.QSize(500, 25))
        self.titGrafLong.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titGrafLong.setFont(font)
        self.titGrafLong.setObjectName("titGrafLong")
        self.verticalLayout_2.addWidget(self.titGrafLong)
        self.titGrafTrans = QtWidgets.QLabel(self.frameIzq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titGrafTrans.sizePolicy().hasHeightForWidth())
        self.titGrafTrans.setSizePolicy(sizePolicy)
        self.titGrafTrans.setMinimumSize(QtCore.QSize(400, 25))
        self.titGrafTrans.setMaximumSize(QtCore.QSize(5000, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titGrafTrans.setFont(font)
        self.titGrafTrans.setObjectName("titGrafTrans")
        self.verticalLayout_2.addWidget(self.titGrafTrans)
        self.gridLayout.addWidget(self.frameIzq, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Diseño Interactivo de Razante"))
        self.btnUpload.setText(_translate("MainWindow", "Cargar Excel"))
        self.btnSave.setText(_translate("MainWindow", "Guardar Informe"))
        self.btnConfig.setText(_translate("MainWindow", "Config. Obra Arte"))
        self.dataGrafTrans.setText(_translate("MainWindow", "[Progresiva Número: 0]\n"
"[Cota Número: 0]\n"
"[Altura de Ruta: 45m]\n"
"[Altura de Terreno Natural: 50m]\n"
"[Diferencia: 5m] "))
        self.dataGeneral.setText(_translate("MainWindow", "Dato1: Área de tierra retirada por cada corte seleccionado\n"
"Dato2: Área de tierra cargada por cada corte seleccionado\n"
"Dato3: Balance Superficie por cada corte seleccionado\n"
"\n"
"Dato4: Volumen de tierra retirada total\n"
"Dato5: Volumen de tierra cargada total\n"
"Dato6: Balance total de Volumen remanente.\n"
""))
        self.dataInfo.setText(_translate("MainWindow", "[Repositorio de GitHub: ]\n"
"[Autores:  ]\n"
"LinkManual \n"
"Versión: 0.2 rev5"))
        self.titGrafLong.setText(_translate("MainWindow", "Gráfico de corte Longitudinal"))
        self.titGrafTrans.setText(_translate("MainWindow", "Grafico de corte Transversal por cada cota"))
