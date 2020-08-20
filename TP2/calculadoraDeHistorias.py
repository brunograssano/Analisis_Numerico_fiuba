import numpy as np


def f(thetaAngulo, uVelocidad, bCoeficienteAmortiguamiento, masa, longitud):
    gravedad = 9.81
    return -(bCoeficienteAmortiguamiento / masa) * uVelocidad - (gravedad / longitud) * thetaAngulo


def g(u):
    return u


def energia(thetaAngulo, uVelocidad, masa, longitud):
    gravedad = 9.81
    return masa * gravedad * (longitud - longitud * np.math.cos(thetaAngulo)) + 0.5 * masa * (longitud * uVelocidad) ** 2


def constantesRungeKutta4(f, g, uVelocidad, thetaAngulo, hPaso, bCoeficienteAmortiguamiento, masa, longitud):
    k1 = g(uVelocidad)
    m1 = f(thetaAngulo, uVelocidad, bCoeficienteAmortiguamiento, masa, longitud)
    m2 = f(thetaAngulo + 0.5 * hPaso * k1, uVelocidad + 0.5 * hPaso * m1, bCoeficienteAmortiguamiento, masa, longitud)
    k2 = g(uVelocidad + 0.5 * hPaso * m1)
    k3 = g(uVelocidad + 0.5 * hPaso * m2)
    m3 = f(thetaAngulo + 0.5 * hPaso * k2, uVelocidad + 0.5 * hPaso * m2, bCoeficienteAmortiguamiento, masa, longitud)
    m4 = f(thetaAngulo + hPaso * k3, uVelocidad + hPaso * m3, bCoeficienteAmortiguamiento, masa, longitud)
    k4 = g(uVelocidad + hPaso * m3)

    return k1, k2, k3, k4, m1, m2, m3, m4


def HistoriasRK4(u0VelocidadInicial, theta0AnguloInicial, hPaso, bCoeficienteAmortiguamiento, masa, longitud, tiempo):
    """
    PreCondiciones: Los valores recibidos son validos, por ejemplo, la longitud, tiempo, masa tienen que ser positivos.
    PostCondiciones: Calculara la historia de Runge Kutta 4
    """
    cantidadIteraciones = int(tiempo / hPaso) + 1

    uVelocidadAnterior, thetaAnguloAnterior = u0VelocidadInicial, theta0AnguloInicial

    HistoriaU = np.arange(0, round(cantidadIteraciones * hPaso, 4), hPaso / 2).reshape(cantidadIteraciones, 2)
    HistoriaTheta = np.arange(0, round(cantidadIteraciones * hPaso, 4), hPaso / 2).reshape(cantidadIteraciones, 2)
    HistoriaEnergia = np.arange(0, round(cantidadIteraciones * hPaso, 4), hPaso / 2).reshape(cantidadIteraciones, 2)

    for i in range(0, cantidadIteraciones):
        HistoriaU[i, 1] = uVelocidadAnterior
        HistoriaTheta[i, 1] = thetaAnguloAnterior
        HistoriaEnergia[i, 1] = energia(thetaAnguloAnterior, uVelocidadAnterior, masa, longitud)

        k1, k2, k3, k4, m1, m2, m3, m4 = constantesRungeKutta4(f, g, uVelocidadAnterior, thetaAnguloAnterior, hPaso,
                                                               bCoeficienteAmortiguamiento, masa, longitud)

        uVelocidadSiguiente = uVelocidadAnterior + (hPaso / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
        thetaAnguloSiguiente = thetaAnguloAnterior + (hPaso / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        uVelocidadAnterior = uVelocidadSiguiente
        thetaAnguloAnterior = thetaAnguloSiguiente

    return HistoriaTheta, HistoriaU, HistoriaEnergia


def HistoriasEuler(u0VelocidadInicial, theta0AnguloInicial, hPaso, bCoeficienteAmortiguamiento, masa, longitud, tiempo):
    """
    PreCondiciones: Los valores recibidos son validos, por ejemplo, la longitud, tiempo, masa tienen que ser positivos.
    PostCondiciones: Calculara la historia de Euler
    """
    cantidadIteraciones = int(tiempo / hPaso) + 1

    uVelocidadAnterior, thetaAnguloAnterior = u0VelocidadInicial, theta0AnguloInicial

    HistoriaU = np.arange(0, round(cantidadIteraciones * hPaso, 4), hPaso / 2).reshape(cantidadIteraciones, 2)
    HistoriaTheta = np.arange(0, round(cantidadIteraciones * hPaso, 4), hPaso / 2).reshape(cantidadIteraciones, 2)
    HistoriaEnergia = np.arange(0, round(cantidadIteraciones * hPaso, 4), hPaso / 2).reshape(cantidadIteraciones, 2)

    for i in range(0, cantidadIteraciones):
        HistoriaU[i, 1] = uVelocidadAnterior
        HistoriaTheta[i, 1] = thetaAnguloAnterior
        HistoriaEnergia[i, 1] = energia(thetaAnguloAnterior, uVelocidadAnterior, masa, longitud)

        uVelocidadSiguiente = uVelocidadAnterior + hPaso * f(thetaAnguloAnterior, uVelocidadAnterior,
                                                             bCoeficienteAmortiguamiento, masa, longitud)
        thetaAnguloSiguiente = thetaAnguloAnterior + hPaso * g(uVelocidadAnterior)

        uVelocidadAnterior = uVelocidadSiguiente
        thetaAnguloAnterior = thetaAnguloSiguiente

    return HistoriaTheta, HistoriaU, HistoriaEnergia
