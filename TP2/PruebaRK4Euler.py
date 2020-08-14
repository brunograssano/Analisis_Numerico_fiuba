from calculadoraDeHistorias import HistoriasEuler
from calculadoraDeHistorias import HistoriasRK4
import Graficador
import numpy as np

np.set_printoptions(formatter={'float_kind':"{:.3e}".format})

def imprimirHistorias(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4):
    print("PRIMEROS 5 VALORES - ANGULO RK4")
    print(HistoriaThetaRK4[0:5, :])
    print("ULTIMOS 5 VALORES - ANGULO RK4")
    print(HistoriaThetaRK4[-5:, :])
    print("PRIMEROS 5 VALORES - VELOCIDAD RK4")
    print(HistoriaURK4[0:5, :])
    print("ULTIMOS 5 VALORES - VELOCIDAD RK4")
    print(HistoriaURK4[-5:, :])
    print("PRIMEROS 5 VALORES - ANGULO EULER")
    print(HistoriaThetaRK1[0:5, :])
    print("ULTIMOS 5 VALORES - ANGULO EULER")
    print(HistoriaThetaRK1[-5:, :])
    print("PRIMEROS 5 VALORES - VELOCIDAD EULER")
    print(HistoriaURK1[0:5, :])
    print("ULTIMOS 5 VALORES - VELOCIDAD EULER")
    print(HistoriaURK1[-5:, :])


def ejecutarMetodosParaLosDatos(u0VelocidadInicial, theta0AnguloInicial, hPaso, bCoeficienteAmortiguamiento, longitud, masa,
                                tiempo):
    HistoriaThetaRK1, HistoriaURK1, HistoriaEnergiaRK1 = HistoriasEuler(np.math.radians(u0VelocidadInicial), np.math.radians(theta0AnguloInicial), hPaso, bCoeficienteAmortiguamiento, masa, longitud, tiempo)
    HistoriaThetaRK4, HistoriaURK4, HistoriaEnergiaRK4 = HistoriasRK4(np.math.radians(u0VelocidadInicial), np.math.radians(theta0AnguloInicial), hPaso, bCoeficienteAmortiguamiento, masa, longitud, tiempo)

    Graficador.graficarSeparados(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, hPaso)
    Graficador.graficarSuperpuestos(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, hPaso)

    imprimirHistorias(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4)


def main():
    u0VelocidadInicial = 0  # EN GRADOS/S
    theta0AnguloInicial = 30  # EN GRADOS
    hPaso = 0.02
    bCoeficienteAmortiguamiento = 0
    longitud = 1  # en metros
    masa = 1  # en Kg
    tiempo = 20

    ejecutarMetodosParaLosDatos(u0VelocidadInicial, theta0AnguloInicial, hPaso, bCoeficienteAmortiguamiento, longitud, masa,
                                tiempo)

    u0VelocidadInicial = 100  # EN GRADOS/S
    theta0AnguloInicial = 30  # EN GRADOS
    hPaso = 0.02
    bCoeficienteAmortiguamiento = 0.5
    longitud = 1  # en metros
    masa = 1  # en Kg
    tiempo = 20

    ejecutarMetodosParaLosDatos(u0VelocidadInicial, theta0AnguloInicial, hPaso, bCoeficienteAmortiguamiento, longitud, masa,
                                tiempo)

if __name__ == "__main__":
    main()




