import numpy as np


def OrdenDeConvergencia(xNmenos2, xNmenos1, xN, xNmas1):
    """
    Calcula el orden de convergencia para determinado punto aplicando la division que se realiza en la definicion.
    Si algun denominador resultase nulo, no se devolvera una constante, se devuelve None.
    """
    a = xNmas1 - xN
    if a == 0:
        return None
    b = xN - xNmenos1
    if b == 0:
        return None

    numerador = np.log(abs(a / b))

    c = xN - xNmenos1
    if c == 0:
        return None

    d = xNmenos1 - xNmenos2
    if d == 0:
        return None

    denominador = np.log(abs(c / d))
    if denominador == 0:
        return None
    return numerador / denominador

#funcion original que habiamos hecho para calcular la constante alfa
def CalcularHistoriaDeOrden2(historia):
    """
    Calcula la constante alfa, necesita de la historia de la busqueda de la raiz.
    Devuelve la historia del alfa y el alfa final conseguido
    """
    tope = len(historia)
    if tope < 5:
        return 0, np.array([])
    historiaDeOrden = np.zeros((tope - 4, 2))

    j = 0
    for i in range(2, tope - 2):
        ordenActual = OrdenDeConvergencia(historia[i - 2][1], historia[i - 1][1], historia[i][1], historia[i + 1][1])
        if not (ordenActual is None):
            historiaDeOrden[j][1] = ordenActual
            historiaDeOrden[j][0] = i
            j = j + 1
    historiaDeOrden = historiaDeOrden[:j]
    return historiaDeOrden[j - 1][1], historiaDeOrden


def CalcularHistoriaDeOrden(historiaRaices):
    """
    Calcula la constante alfa, necesita de la historia de la busqueda de la raiz.
    Devuelve la historia del alfa y el alfa final conseguido
    """
    nIteraciones = len(historiaRaices) - 1
    if len(historiaRaices) < 5:
        return 0, np.array([])
    alfa = np.zeros((nIteraciones - 1, 2))

    for n in range(3 - 1, nIteraciones - 1):
        e_n_mas_1 = historiaRaices[n + 1][1] - historiaRaices[n][1]
        e_n = historiaRaices[n][1] - historiaRaices[n - 1][1]
        e_n_menos_1 = historiaRaices[n - 1][1] - historiaRaices[n - 2][1]

        # Tira un warning de division por 0 debido a que varios numeros estan cercanos al mismo, se agrego para evitarlo,
        # si se saltean estas divisiones los graficos quedan peor.
        with np.errstate(divide='ignore'):
            alfa[n] = n, np.log10(np.abs(e_n_mas_1 / e_n)) / np.log10(np.abs(e_n / e_n_menos_1))


    return alfa[nIteraciones - 2][1], alfa


def ConstanteAsintotica(xN, xNmas1, alfa, raiz):
    """
    Realiza el calculo de la constante asintotica para una iteracion. Los valores recibidos son validos.
    Si resulta que el denominador es 0, se devuelve None.
    """
    numerador = abs((xNmas1 - raiz))
    denominador = abs(xN - raiz) ** alfa
    if denominador == 0:
        return None
    return numerador / denominador


def CalcularHistoriaConstanteAsintotica(historia, alfa):
    """
    Calcula la constante lambda, necesita de la historia de la busqueda de la raiz y del alfa obtenido previamente
    Devuelve la historia del lambda y el lambda final conseguido
    """
    if alfa <= 0:
        return 0, np.array([])
    tope = len(historia)
    raiz = historia[tope - 1][1]

    historiaConstanteAsintotica = np.zeros((tope - 2, 2))
    j = 0
    for i in range(0, tope - 2):
        constanteActual = ConstanteAsintotica(historia[i][1], historia[i + 1][1], alfa, raiz)
        if not (constanteActual is None):
            historiaConstanteAsintotica[j][1] = constanteActual
            historiaConstanteAsintotica[j][0] = i
            j = j + 1

    historiaConstanteAsintotica = historiaConstanteAsintotica[:j]
    return historiaConstanteAsintotica[j - 1][1], historiaConstanteAsintotica
