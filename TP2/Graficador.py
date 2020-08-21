import matplotlib.pyplot as plt


def graficarSeparados(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, h):
    figura, graficos = plt.subplots(3, 2)
    figura.suptitle("Comparación RK1 - RK4 (h = {})".format(h))
    graficos[0, 0].set_title('RK1')
    graficos[0, 1].set_title('RK4')
    figura.set_size_inches(8,6)

    graficos[0, 0].set_ylabel('Ángulo [rad]')
    graficos[0, 0].plot(HistoriaThetaRK1[:, 0], HistoriaThetaRK1[:, 1], label = 'RK1')
    graficos[0, 1].plot(HistoriaThetaRK4[:, 0], HistoriaThetaRK4[:, 1], label = 'RK4', color= 'orange')

    graficos[0, 0].set_ylim([-5, 5])

    graficos[1, 0].set_ylabel('Vel. angular [rad/s]')
    graficos[1, 0].plot(HistoriaURK1[:, 0], HistoriaURK1[:, 1], label = 'RK1')
    graficos[1, 1].plot(HistoriaURK4[:, 0], HistoriaURK4[:, 1], label = 'RK4', color= 'orange')

    graficos[2, 0].set_ylabel('Energía [J]')
    graficos[2, 0].plot(HistoriaEnergiaRK1[:, 0], HistoriaEnergiaRK1[:, 1], label = 'RK1')
    graficos[2, 0].set_ylim([-5,5])
    graficos[2, 1].plot(HistoriaEnergiaRK4[:, 0], HistoriaEnergiaRK4[:, 1], label = 'RK4', color= 'orange')
    graficos[2, 1].set_ylim([-5,5])
    plt.show()


def graficarSuperpuestos(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, h):
    figura, graficos = plt.subplots(3, 1, sharex=True)
    figura.suptitle("Comparación RK1 - RK4 (h = {})".format(h))
    figura.set_size_inches(8,6)

    graficos[0].set_ylabel('Ángulo [rad]')
    graficos[0].plot(HistoriaThetaRK1[:, 0], HistoriaThetaRK1[:, 1], label = 'RK1')
    graficos[0].plot(HistoriaThetaRK4[:, 0], HistoriaThetaRK4[:, 1], label = 'RK4')
    graficos[0].legend()

    graficos[1].set_ylabel('Vel. angular [rad/s]')
    graficos[1].plot(HistoriaURK1[:, 0], HistoriaURK1[:, 1], label = 'RK1')
    graficos[1].plot(HistoriaURK4[:, 0], HistoriaURK4[:, 1], label = 'RK4')
    graficos[1].legend()

    graficos[2].set_ylabel('Energía [J]')
    graficos[2].plot(HistoriaEnergiaRK1[:, 0], HistoriaEnergiaRK1[:, 1], label = 'RK1')
    graficos[2].plot(HistoriaEnergiaRK4[:, 0], HistoriaEnergiaRK4[:, 1], label = 'RK4')
    graficos[2].set_ylim([-5,5])
    graficos[2].legend()
    plt.show()