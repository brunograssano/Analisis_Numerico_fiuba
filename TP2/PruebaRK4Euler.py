from calculadoraDeHistorias import HistoriasEuler
from calculadoraDeHistorias import HistoriasRK4
import numpy as np
import matplotlib.pyplot as plt

u0 = 0 #velocidad incial (EN GRAD/S)
theta0 = 30 #angulo inicial (EN GRAD)
h = 0.2 #paso
b = 0 #coeficiente de amortiguamiento
l = 1 #longitud en metros
m = 1 #masa en Kg

HistoriaTheta, HistoriaU, HistoriaEnergia = HistoriasRK4(np.math.radians(u0), np.math.radians(theta0), h, b, m, l)

plt.plot(HistoriaTheta[:, 0], HistoriaTheta[:, 1])
plt.ylabel('Angulo (rad)')
plt.xlabel('Tiempo(s)')
plt.title('Angulo - Runge Kutta 4')
plt.show()

plt.plot(HistoriaU[:, 0], HistoriaU[:, 1])
plt.ylabel('Velocidad angular (rad/seg)')
plt.xlabel('Tiempo(s)')
plt.title('Velocidad - Runge Kutta 4')
plt.show()

plt.plot(HistoriaEnergia[:, 0], HistoriaEnergia[:, 1])
plt.ylabel('Energia')
plt.xlabel('Tiempo(s)')
plt.title('Energia - Runge Kutta 4')
plt.xlim(0, 30*h)
plt.ylim(-5, 5)
plt.show()

u0 = 0 #velocidad incial (EN GRAD/S)
theta0 = 30 #angulo inicial (EN GRAD)
h = 0.001 #paso
b = 0 #coeficiente de amortiguamiento
l = 1 #longitud en metros
m = 1 #masa en Kg

HistoriaTheta, HistoriaU, HistoriaEnergia = HistoriasEuler(np.math.radians(u0), np.math.radians(theta0), h, b, m, l)

plt.plot(HistoriaTheta[:, 0], HistoriaTheta[:, 1])
plt.ylabel('Angulo (rad)')
plt.xlabel('Tiempo(s)')
plt.title('Angulo - Euler')
plt.show()

plt.plot(HistoriaU[:, 0], HistoriaU[:, 1])
plt.ylabel('Velocidad angular (rad/seg)')
plt.xlabel('Tiempo(s)')
plt.title('Velocidad - Euler')
plt.show()

plt.plot(HistoriaEnergia[:, 0], HistoriaEnergia[:, 1])
plt.ylabel('Energia')
plt.xlabel('Tiempo(s)')
plt.title('Energia - Euler')
plt.xlim(0, 6000*h)
plt.ylim(-5, 5)
plt.show()