import numpy as np

def f(theta, u, b, m, l):
    return(-(b/m) *u - (9.8/l) * theta)

def g(u):
    return u

def energia(theta, u, m, l):
    return m*9.8*(l - l*np.math.cos(theta)) + 0.5 * m * (l*u)**2

def constantesRungeKutta4(f,g,u,theta,h ,b, m, l):
    k1 = g(u)
    m1 = f(theta, u, b, m, l)
    m2 = f(theta + 0.5 * h * k1, u + 0.5 * h * m1, b, m, l)
    k2 = g(u + 0.5 * h * m1)
    k3 = g(u + 0.5 * h * m2)
    m3 = f(theta + 0.5 * h * k2, u + 0.5 * h * m2, b, m, l)
    m4 = f(theta + h * k3, u + h * m3, b, m, l)
    k4 = g(u + h * m3)

    return k1, k2, k3, k4, m1, m2, m3, m4

def HistoriasRK4(u0, theta0, h, b, m, l, t):

    N = int(t/h) + 1 #cantidad de iteraciones del metodo

    u_ant, theta_ant = u0, theta0

    HistoriaU = np.arange(0, round(N*h, 4) , h/2).reshape(N, 2)
    HistoriaTheta = np.arange(0, round(N*h, 4), h/2).reshape(N, 2)
    HistoriaEnergia = np.arange(0, round(N*h, 4), h/2).reshape(N, 2)

    for i in range(0 , N):
        HistoriaU[i, 1] = u_ant
        HistoriaTheta[i, 1] = theta_ant
        HistoriaEnergia[i, 1] = energia(theta_ant, u_ant, m, l)

        k1, k2, k3, k4, m1, m2, m3, m4 = constantesRungeKutta4(f,g, u_ant, theta_ant , h ,b, m,l)

        u_sig = u_ant + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
        theta_sig = theta_ant + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        u_ant = u_sig
        theta_ant = theta_sig

    return HistoriaTheta, HistoriaU, HistoriaEnergia

def HistoriasEuler(u0, theta0, h, b, m, l, t):

    N = int(t/h) + 1 #cantidad de iteraciones del metodo

    u_ant, theta_ant = u0, theta0

    HistoriaU = np.arange(0, round(N*h, 4), h/2).reshape(N, 2)
    HistoriaTheta = np.arange(0, round(N*h, 4), h/2).reshape(N, 2)
    HistoriaEnergia = np.arange(0, round(N*h, 4), h/2).reshape(N, 2)

    for i in range(0, N):
        HistoriaU[i, 1] = u_ant
        HistoriaTheta[i, 1] = theta_ant
        HistoriaEnergia[i, 1] = energia(theta_ant, u_ant, m, l)

        u_sig = u_ant + h * f(theta_ant, u_ant, b, m, l)
        theta_sig = theta_ant + h * g(u_ant)

        u_ant = u_sig
        theta_ant = theta_sig

    return HistoriaTheta, HistoriaU, HistoriaEnergia