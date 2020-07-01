import numpy as np


def CalcularHistoriaDeOrden(historiaRaices):
    """
    Calcula la constante alfa, necesita de la historia de la busqueda de la raiz.
    Devuelve la historia del alfa y el alfa final conseguido
    """

    if len(historiaRaices) < 5:
        return 0, np.array([])

    nIteraciones = len(historiaRaices)
    alfa = np.zeros((nIteraciones - 1, 2))
    #alfaAEnviar = 0
    j=0
    for n in range(2, nIteraciones - 1):
        a = historiaRaices[n+1][1] - historiaRaices[n][1]
        b = historiaRaices[n][1] - historiaRaices[n - 1][1]
        c = historiaRaices[n - 1][1] - historiaRaices[n - 2][1]

        if (np.abs(np.log10(np.abs(b / c))) < 1e-14) or (np.abs(b) < 1e-14) or (np.abs(c) < 1e-14) or (np.abs(a) < 1e-14) or (np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))) > 2.5 \
                or (np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))) < 0.3:
            #alfa[n] = n, 0
            continue
        else:
            #alfa[n] = n, np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))
            #alfaAEnviar=np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))
            alfa[j] = j, np.log10(np.abs(a / b)) / np.log10(np.abs(b / c))
            j = j+1

    alfa = alfa[:j]

    #print(alfa)
    if(len(alfa)!=0):
        promedioAlfas=sum(alfa)/len(alfa)
        promedioAlfas=promedioAlfas[1]
    else:
        promedioAlfas=0
    #print(promedioAlfas)
    if j==0:
        return 0, alfa
    return promedioAlfas, alfa
    #return alfaAEnviar, alfa



def CalcularHistoriaConstanteAsintotica(historia, alfa):
    """
    Calcula la constante lambda, necesita de la historia de la busqueda de la raiz y del alfa obtenido previamente
    Devuelve la historia del lambda y el lambda final conseguido
    """

    if alfa<0:
        return 0,np.zeros()
    #if alfa < 1:
    #    alfa =1

    #if alfa > 2:
    #    alfa =2


    tope = len(historia)
    j = 0
    historiaConstanteAsintotica = np.zeros((tope - 2, 2))
    for i in range(1, tope - 1-1):
        xMas1 = historia[i+1][1]
        x = historia[i][1]
        xMenos1 = historia[i-1][1]

        numerador = abs(xMas1 - x) #usando raiz empeora biseccion (oscila) y no altero a los demas
        denominador = abs(x - xMenos1) ** alfa #aca la raiz seria xMenos1

        if numerador < 1e-14 or denominador < 1e-14 or xMas1< 1e-14 or x<1e-14 or xMenos1<1e-14 or (numerador / denominador)<1e-14 or (numerador / denominador)>1 \
                or (numerador / denominador)<0.15:
            #historiaConstanteAsintotica[i][1] = 0
            #historiaConstanteAsintotica[i][0] = i
            continue
        else:
            constanteActual = numerador / denominador
            #historiaConstanteAsintotica[i][1] = constanteActual
            #historiaConstanteAsintotica[i][0] = i
            historiaConstanteAsintotica[j][1] = constanteActual
            historiaConstanteAsintotica[j][0] = j
            j = j+1

    
    historiaConstanteAsintotica = historiaConstanteAsintotica[:j]

    print(historiaConstanteAsintotica)
    if j==0:
        return 0, historiaConstanteAsintotica
    return historiaConstanteAsintotica[j - 1][1], historiaConstanteAsintotica
    #return historiaConstanteAsintotica[tope -2 - 1][1], historiaConstanteAsintotica
