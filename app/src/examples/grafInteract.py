# # import sys
# # import matplotlib.pyplot as plt
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
# # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Gráfico Interactivo")

# #         # Crear un widget central
# #         central_widget = QWidget()
# #         self.setCentralWidget(central_widget)

# #         # Crear un layout vertical
# #         layout = QVBoxLayout(central_widget)

# #         # Crear un botón
# #         self.button = QPushButton("Desplazar Curva")
# #         self.button.clicked.connect(self.desplazar_curva)
# #         layout.addWidget(self.button)

# #         # Crear un gráfico de ejemplo
# #         self.fig, self.ax = plt.subplots()
# #         self.canvas = FigureCanvas(self.fig)
# #         layout.addWidget(self.canvas)

# #         # Dibujar la curva inicial
# #         self.dibujar_curva()

# #     def dibujar_curva(self):
# #         # Datos de ejemplo para la curva
# #         x = [1, 2, 3, 4, 5]
# #         y = [2, 3, 5, 7, 11]

# #         # Dibujar la curva
# #         self.ax.clear()
# #         self.ax.plot(x, y)
# #         self.canvas.draw()

# #     # def desplazar_curva(self):
# #     #     # Aquí puedes modificar los datos para desplazar la curva
# #     #     pass

# #     def desplazar_curva(self):
# #         # Datos de ejemplo para desplazar la curva hacia arriba
# #         incremento = 2
# #         nueva_y = [y + incremento for y in [2, 3, 5, 7, 11]]

# #         # Dibujar la curva desplazada
# #         self.ax.clear()
# #         self.ax.plot([1, 2, 3, 4, 5], nueva_y)
# #         self.canvas.draw()


# # def main():
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())

# # if __name__ == "__main__":
# #     main()



# # import sys
# # import matplotlib.pyplot as plt
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# # class PlotWidget(QWidget):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)

# #         self.fig, self.ax = plt.subplots()
# #         self.canvas = FigureCanvas(self.fig)
# #         layout = QVBoxLayout(self)
# #         layout.addWidget(self.canvas)

# #         self.x = [1, 2, 3, 4, 5]
# #         self.y = [2, 3, 5, 7, 11]
# #         self.line, = self.ax.plot(self.x, self.y)

# #         self.cid = self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)

# #     def on_mouse_move(self, event):
# #         if event.inaxes == self.ax:  # Verificar si el evento del ratón está dentro del área del gráfico
# #             new_y = [point + event.ydata for point in self.y]  # Desplazar la curva verticalmente según la posición del ratón
# #             self.line.set_ydata(new_y)
# #             self.canvas.draw()

# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Gráfico Interactivo")
# #         central_widget = QWidget()
# #         self.setCentralWidget(central_widget)
# #         layout = QVBoxLayout(central_widget)

# #         self.plot_widget = PlotWidget(self)
# #         layout.addWidget(self.plot_widget)

# # def main():
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())

# # if __name__ == "__main__":
# #     main()

# ## Funciona Tomar de referencia

# import sys
# import matplotlib.pyplot as plt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# class PlotWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.fig, self.ax = plt.subplots()
#         self.canvas = FigureCanvas(self.fig)
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.canvas)

#         self.x = [1, 2, 3, 4, 5]
#         self.y = [2, 3, 5, 7, 11]
#         self.line, = self.ax.plot(self.x, self.y, marker='o', linestyle='-', color='b')

#         self.selected_point = None  # Punto seleccionado
#         self.offset = 0  # Offset del desplazamiento

#         self.cid_press = self.canvas.mpl_connect('button_press_event', self.on_click)
#         self.cid_release = self.canvas.mpl_connect('button_release_event', self.on_release)
#         self.cid_move = self.canvas.mpl_connect('motion_notify_event', self.on_move)

#     def on_click(self, event):
#         if event.inaxes == self.ax:
#             xdata = self.line.get_xdata()
#             ydata = self.line.get_ydata()

#             # Verificar la distancia con los puntos
#             for i, (x, y) in enumerate(zip(xdata, ydata)):
#                 distance = ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
#                 if distance < 0.1:  # Valor de tolerancia para seleccionar el punto
#                     self.selected_point = i
#                     break

#     def on_release(self, event):
#         self.selected_point = None

#     def on_move(self, event):
#         if self.selected_point is not None:
#             if event.inaxes == self.ax:
#                 new_y = self.y.copy()
#                 new_y[self.selected_point] = event.ydata
#                 self.line.set_ydata(new_y)
#                 self.canvas.draw()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Gráfico Interactivo")
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout(central_widget)

#         self.plot_widget = PlotWidget(self)
#         layout.addWidget(self.plot_widget)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()





import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 3, 5, 7, 11]
        self.line, = self.ax.plot(self.x, self.y, marker='o', linestyle='-', color='b')

        self.selected_point = None  # Punto seleccionado
        self.offset = 0  # Offset del desplazamiento

        self.lbl_previous = QLabel('Posición anterior:')
        layout.addWidget(self.lbl_previous)
        self.lbl_new = QLabel('Nueva posición:')
        layout.addWidget(self.lbl_new)

        self.cid_press = self.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_release = self.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_move = self.canvas.mpl_connect('motion_notify_event', self.on_move)

    def on_click(self, event):
        if event.inaxes == self.ax:
            xdata = self.line.get_xdata()
            ydata = self.line.get_ydata()

            # Verificar la distancia con los puntos
            for i, (x, y) in enumerate(zip(xdata, ydata)):
                distance = ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                if distance < 0.1:  # Valor de tolerancia para seleccionar el punto
                    self.selected_point = i
                    self.lbl_previous.setText(f'Posición anterior: ({x:.2f}, {y:.2f})')
                    break

    def on_release(self, event):
        self.selected_point = None

    def on_move(self, event):
        if self.selected_point is not None:
            if event.inaxes == self.ax:
                new_y = self.y.copy()
                new_y[self.selected_point] = event.ydata
                self.line.set_ydata(new_y)
                self.lbl_new.setText(f'Nueva posición: ({self.x[self.selected_point]:.2f}, {event.ydata:.2f})')
                self.canvas.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gráfico Interactivo")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.plot_widget = PlotWidget(self)
        layout.addWidget(self.plot_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
