
import matplotlib.pyplot as plt

def graficarSeparados(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, h):
    fig, ax = plt.subplots(3,2)
    fig.suptitle("Comparación RK1 - RK4 (h = {})".format(h))
    ax[0, 0].set_title('RK1')
    ax[0, 1].set_title('RK4')
    fig.set_size_inches(8,6)

    ax[0, 0].set_ylabel('Ángulo [rad]')
    ax[0, 0].plot(HistoriaThetaRK1[:, 0], HistoriaThetaRK1[:, 1], label = 'RK1')
    ax[0, 1].plot(HistoriaThetaRK4[:, 0], HistoriaThetaRK4[:, 1], label = 'RK4', color= 'orange')

    ax[1, 0].set_ylabel('Vel. angular [rad/s]')
    ax[1, 0].plot(HistoriaURK1[:, 0], HistoriaURK1[:, 1], label = 'RK1')
    ax[1, 1].plot(HistoriaURK4[:, 0], HistoriaURK4[:, 1], label = 'RK4', color= 'orange')

    ax[2, 0].set_ylabel('Energía [J]')
    ax[2, 0].plot(HistoriaEnergiaRK1[:, 0], HistoriaEnergiaRK1[:, 1], label = 'RK1')
    ax[2,0].set_ylim([-5,5])
    ax[2, 1].plot(HistoriaEnergiaRK4[:, 0], HistoriaEnergiaRK4[:, 1], label = 'RK4', color= 'orange')
    ax[2,1].set_ylim([-5,5])
    plt.show()

def graficarSuperpuestos(HistoriaThetaRK1, HistoriaThetaRK4, HistoriaURK1, HistoriaURK4, HistoriaEnergiaRK1, HistoriaEnergiaRK4, h):
    fig, ax = plt.subplots(3,1, sharex=True)
    fig.suptitle("Comparación RK1 - RK4 (h = {})".format(h))
    fig.set_size_inches(8,6)

    ax[0].set_ylabel('Ángulo [rad]')
    ax[0].plot(HistoriaThetaRK1[:, 0], HistoriaThetaRK1[:, 1], label = 'RK1')
    ax[0].plot(HistoriaThetaRK4[:, 0], HistoriaThetaRK4[:, 1], label = 'RK4')
    ax[0].legend()

    ax[1].set_ylabel('Vel. angular [rad/s]')
    ax[1].plot(HistoriaURK1[:, 0], HistoriaURK1[:, 1], label = 'RK1')
    ax[1].plot(HistoriaURK4[:, 0], HistoriaURK4[:, 1], label = 'RK4')
    ax[1].legend()

    ax[2].set_ylabel('Energía [J]')
    ax[2].plot(HistoriaEnergiaRK1[:, 0], HistoriaEnergiaRK1[:, 1], label = 'RK1')
    ax[2].plot(HistoriaEnergiaRK4[:, 0], HistoriaEnergiaRK4[:, 1], label = 'RK4')
    ax[2].set_ylim([-5,5])
    ax[2].legend()
    plt.show()