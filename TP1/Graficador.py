import matplotlib.pyplot as plt


# Recibe las 4 historias de los métodos y las grafica.
def graficarMetodos(historiaBiseccion, historiaNR, historiaNRM, historiaSecante):
    plt.figure()
    plt.plot(historiaBiseccion[:, 0], historiaBiseccion[:, 1], \
             '-', lw=1, label='Biseccion', color='blue')
    plt.plot(historiaNR[:, 0], historiaNR[:, 1], \
             '-', lw=1, label='Newton-Raphson', color='red')
    plt.plot(historiaNRM[:, 0], historiaNRM[:, 1], \
             '-', lw=1, label='NR modificado', color='orange')
    plt.plot(historiaSecante[:, 0], historiaSecante[:, 1], \
             '-', lw=1, label='Secante', color='green')
    
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
    plt.plot(historiaOCBiseccion[:, 0], historiaOCBiseccion[:, 1], \
             '-', lw=1, label='Bisección', color='blue')
    plt.plot(historiaOCNewtonRaphson[:, 0], historiaOCNewtonRaphson[:, 1], \
             '-', lw=1, label='Newton-Raphson', color='red')
    plt.plot(historiaOCNewtonRaphsonModif[:, 0], historiaOCNewtonRaphsonModif[:, 1], \
             '-', lw=1, label='NR modificado', color='orange')
    plt.plot(historiaOCSec[:, 0], historiaOCSec[:, 1], \
             '-', lw=1, label='Secante', color='green')

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
    plt.plot(historiaCABIS[:, 0], historiaCABIS[:, 1], \
             '-', lw=1, label='Bisección', color='blue')

    plt.plot(historiaCANR[:, 0], historiaCANR[:, 1], \
             '-', lw=1, label='Newton-Raphson', color='red')

    plt.plot(historiaCANRM[:, 0], historiaCANRM[:, 1], \
             '-', lw=1, label='NR modificado', color='orange')

    plt.plot(historiaCASEC[:, 0], historiaCASEC[:, 1], \
             '-', lw=1, label='Secante', color='green')

    plt.xlabel('Iteración')
    plt.ylabel('Lambda')
    plt.legend(loc='best')
    plt.title('Constante asintótica estimada')
    plt.grid(True)
    plt.show()
