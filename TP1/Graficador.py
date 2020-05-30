import matplotlib.pyplot as plt




def graficar(historia, nombre, color):
    if(historia.size != 0):
        plt.plot(historia[:, 0], historia[:, 1], \
                 '-', lw=1, label=nombre, color=color)
    else:
        plt.plot(0,0,'*',lw=0, label = nombre +'; no suf datos.', color = color)




# Recibe las 4 historias de los métodos y las grafica.
def graficarMetodos(historiaBiseccion, historiaNR, historiaNRM, historiaSecante):
    plt.figure()

    graficar(historiaBiseccion, 'Biseccion', 'blue')
    graficar(historiaNR, 'Newton-Raphson', 'red')
    graficar(historiaNRM, 'NR modificado', 'orange')
    graficar(historiaSecante, 'Secante', 'green')
    
    plt.xlabel('Iteración')
    plt.ylabel('Raiz')
    plt.legend(loc='best')
    plt.title('Raiz estimada')
    plt.grid(True)
    plt.show()


# Recibe la historia de los órdenes de convergencia respecto a cada paso.
# OC: "Orden de convergencia"
def graficarOrdenDeConvergencia(historiaOCBiseccion, historiaOCNewtonRaphson, \
                                historiaOCNewtonRaphsonModif, historiaOCSec):
    plt.figure()
    
    graficar(historiaOCBiseccion, 'Biseccion', 'blue')
    graficar(historiaOCNewtonRaphson, 'Newton-Raphson', 'red')
    graficar(historiaOCNewtonRaphsonModif, 'NR modificado', 'orange')
    graficar(historiaOCSec, 'Secante', 'green')
    
    plt.xlabel('Iteración')
    plt.xlabel('Iteración')
    plt.ylabel('Alfa')
    plt.legend(loc='best')
    plt.title('Orden de convergencia estimado')
    plt.grid(True)
    plt.show()    


## OJO, falta testearlo. Si bien teóricamente funciona, prácticamente no logra la convergencia teórica.
# Cuando tengamos los demás métodos deberíamos probarlo.
# Recibe como parámetros las historias de las constantes asintóticas respecto a cada paso.
# CA: "Constante asintótica"
def graficarConstantesAsintoticas(historiaCABIS, historiaCANR, historiaCANRM, historiaCASEC):
    plt.figure()
    
    graficar(historiaCABIS , 'Biseccion', 'blue')
    graficar(historiaCANR, 'Newton-Raphson', 'red')
    graficar(historiaCANRM , 'NR modificado', 'orange')
    graficar(historiaCASEC, 'Secante', 'green')


    plt.xlabel('Iteración')
    plt.ylabel('Lambda')
    plt.legend(loc='best')
    plt.title('Constante asintótica estimada')
    plt.grid(True)
    plt.show()
