from calculadoraDeHistorias import HistoriasEuler
from calculadoraDeHistorias import HistoriasRK4
import Graficador
import numpy as np

np.set_printoptions(formatter={'float_kind':"{:.3e}".format})

#ayudenme a pensar un mejor nombre (no me juzgen ahre)
def ejecutarParaLosDatos(u0, theta0, h,b,l,m,t):
    HistoriaThetaRK1, HistoriaURK1, HistoriaEnergiaRK1 = HistoriasEuler(np.math.radians(u0), np.math.radians(theta0), h, b, m, l, t)
    HistoriaThetaRK4, HistoriaURK4, HistoriaEnergiaRK4 = HistoriasRK4(np.math.radians(u0), np.math.radians(theta0), h, b, m, l, t)

    Graficador.graficarSeparados(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, h)
    Graficador.graficarSuperpuestos(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, h)

    print("PRIMEROS 5 VALORES - ANGULO RK4")
    print(HistoriaThetaRK4[0:5, :])
    print("ULTIMOS 5 VALORES - ANGULO RK4")
    print(HistoriaThetaRK4[-5:, :])

    print("PRIMEROS 5 VALORES - VELOCIDAD RK4")
    print(HistoriaURK4[0:5, :])
    print("ULTIMOS 5 VALORES - VELOCIDAD RK4")
    print(HistoriaURK4[-5:, :])

    print("PRIMEROS 5 VALORES - ENERGIA RK4")
    print(HistoriaEnergiaRK4[0:5, :])
    print("ULTIMOS 5 VALORES - ENERGIA RK4")
    print(HistoriaEnergiaRK4[-5:, :])

    print("PRIMEROS 5 VALORES - ANGULO EULER")
    print(HistoriaThetaRK1[0:5, :])
    print("ULTIMOS 5 VALORES - ANGULO EULER")
    print(HistoriaThetaRK1[-5:, :])

    print("PRIMEROS 5 VALORES - VELOCIDAD EULER")
    print(HistoriaURK1[0:5, :])
    print("ULTIMOS 5 VALORES - VELOCIDAD EULER")
    print(HistoriaURK1[-5:, :])

    print("PRIMEROS 5 VALORES - ENERGIA EULER")
    print(HistoriaEnergiaRK1[0:5, :])
    print("ULTIMOS 5 VALORES - ENERGIA EULER")
    print(HistoriaEnergiaRK1[-5:, :])


u0 = 0 #velocidad incial (EN GRAD/S)
theta0 = 30 #angulo inicial (EN GRAD)
h = 0.02 #paso
b = 0 #coeficiente de amortiguamiento
l = 1 #longitud en metros
m = 1 #masa en Kg
t = 5 #tiempo durante el que se requieren mediciones

ejecutarParaLosDatos(u0, theta0, h,b,l,m,t)

u0 = 100 #velocidad incial (EN GRAD/S)
theta0 = 30 #angulo inicial (EN GRAD)
h = 0.02 #paso
b = 0.5 #coeficiente de amortiguamiento
l = 1 #longitud en metros
m = 1 #masa en Kg
t = 20 #tiempo durante el que se requieren mediciones

ejecutarParaLosDatos(u0, theta0, h,b,l,m,t)

u0 = 0 #velocidad incial (EN GRAD/S)
theta0 = 30 #angulo inicial (EN GRAD)
h = 0.02 #paso
b = 1 #coeficiente de amortiguamiento
l = 1 #longitud en metros
m = 1 #masa en Kg
t = 20 #tiempo durante el que se requieren mediciones

ejecutarParaLosDatos(u0, theta0, h,b,l,m,t)

