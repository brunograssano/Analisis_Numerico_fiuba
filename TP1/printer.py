from calculadora_nueva import *

def formatear(historia):
    barra = '\\'
    barras = barra + barra    
    alfa, historiaAlfa = CalcularHistoriaDeOrden(historia)
    historiaLambda = CalcularHistoriaConstanteAsintotica(historia, alfa)
    i = 0
    for actual in historia:
        print("{:.0f}".format(actual[0]),"     &", actual[1]," & ","{:.13f}".format(actual[2])," & ",\
              historiaAlfa[i][1]," & ", historiaLambda[i], barras)
        i++;