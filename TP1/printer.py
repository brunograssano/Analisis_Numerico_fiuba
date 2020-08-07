from calculadora_nueva import *

def formatear(historia):
    barra = '\\'
    barras = barra + barra    
    alfa, historiaAlfa = CalcularHistoriaDeOrden(historia)
    constante, historiaLambda = CalcularHistoriaConstanteAsintotica(historia, alfa)
    i = 0
        
    #print(historiaAlfa)
          
    for landa in historiaLambda:
        print("{:.13f}".format(landa[1]))
          
          
    for actual in historia:
        print("{:.0f}".format(actual[0]),"     &", actual[1]," & ","{:.13f}".format(historia[i-1][2])," & ",\
              historiaAlfa[i][1]," & ",historiaLambda[i][1], barras)
        i = i + 1