import numpy as np
import matplotlib.pyplot as plt

def graficar_recta(angulo_pendiente, longitud_recta, distancia_y_origen):
    # Calcular las coordenadas finales de la recta
    x_final = longitud_recta / np.sqrt(1 + np.tan(np.radians(angulo_pendiente))**2)
    y_final = np.tan(np.radians(angulo_pendiente)) * x_final + distancia_y_origen

    # Generar puntos para la recta
    x = np.linspace(0, x_final, 100)
    y = np.tan(np.radians(angulo_pendiente)) * x + distancia_y_origen

    # Graficar la recta
    plt.plot(x, y, label=f'Recta con Ángulo de Pendiente {angulo_pendiente}°')

    # Configurar el gráfico
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title('Recta con Ángulo de Pendiente')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    
    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
angulo = 30  # Ángulo de pendiente en grados
longitud = 5  # Longitud de la recta
distancia_y = 2  # Distancia de y respecto al origen

graficar_recta(angulo, longitud, distancia_y)