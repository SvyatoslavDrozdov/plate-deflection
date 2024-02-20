import Core
import math as m
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def DEFLECTION(a, b, Q, N, M, dx, dy, D, LvL, Num, Scale):
    C = Core.core_calculation(a, b, Q, N, M, dx, dy, D, LvL, Num)
    # Make data
    Num = 5 * LvL
    DX = 2 * a / 100
    DY = 2 * b / 100
    X = np.arange(-a, a, DX)
    Y = np.arange(-b, b, DY)
    X, Y = np.meshgrid(X, Y)

    def Fi(i_n, iX, iY):
        if 1 <= i_n <= LvL:
            f = (1 + np.cos((2 * i_n - 1) * m.pi * iX / a)) * (1 + np.cos((2 * i_n - 1) * m.pi * iY / b))
        elif LvL + 1 <= i_n <= 2 * LvL:
            f = (1 + np.cos(m.pi * iX / a)) * np.exp((i_n - LvL) * iX) * (1 + np.cos(m.pi * iY / b)) * np.exp(
                (i_n - LvL) * iY)
        elif 2 * LvL + 1 <= i_n <= 3 * LvL:
            f = (1 + np.cos(m.pi * iX / a)) * np.exp(-(i_n - 2 * LvL) * iX) * (1 + np.cos(m.pi * iY / b)) * np.exp(
                -(i_n - 2 * LvL) * iY)
        elif 3 * LvL + 1 <= i_n <= 4 * LvL:
            f = (1 + np.cos(m.pi * iX / a)) * np.exp(-(i_n - 3 * LvL) * iX) * (1 + np.cos(m.pi * iY / b)) * np.exp(
                +(i_n - 3 * LvL) * iY)
        elif 4 * LvL + 1 <= i_n <= 5 * LvL:
            f = (1 + np.cos(m.pi * iX / a)) * np.exp(+(i_n - 4 * LvL) * iX) * (1 + np.cos(m.pi * iY / b)) * np.exp(
                -(i_n - 4 * LvL) * iY)
        else:
            f = 0
            print("ERROR")
        return f

    Z = C[0] * Fi(1, X, Y)
    if Num > 1:
        for i in range(2, Num + 1):
            Z += C[i - 1] * Fi(i, X, Y)

    Max_Deflection = min(np.amin(Z, axis=0))

    # Plot the surface

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Greys)

    ax.set_xlabel('x -axis')
    ax.set_ylabel('y - axis')
    ax.set_zlabel('z - axis')
    dimensions = [a, b]
    ax.set_xlim(-max(dimensions), max(dimensions))
    ax.set_ylim(-max(dimensions), max(dimensions))
    if Scale == "":
        ax.set_zlim(2 * Max_Deflection, -2 * Max_Deflection)
    else:
        ax.set_zlim(-Scale, Scale)

    plt.title("Max deflection = " + f"{format(Max_Deflection, '.3e')}")
    plt.show()

    # The next things I used for testing
    # h = 0.01
    # Nu = 0.3
    # E = 2.1 * 10 ** 11
    # D = E * h ** 3 / (12 * (1 - Nu ** 2))
    # print("We calculated: ", min(np.amin(Z, axis=0)))
    # print("Accurate solution for distributed force: ", -0.00126 * 780 * 2**4/ D)  #  Distributed loading
    # print("Accurate solution for point force: ", - 0.0056 * 3120 * 2 ** 2 / D)  # Point Loading
