import math as m
import numpy


def core_calculation(a, b, Q, N, M, dx, dy, D, LvL, Num):
    def Fi(i_n, ix, iy):
        if 1 <= i_n <= LvL:
            f = (1 + m.cos((2 * i_n - 1) * m.pi * ix / a)) * (1 + m.cos((2 * i_n - 1) * m.pi * iy / b))
        elif LvL + 1 <= i_n <= 2 * LvL:
            f = (1 + m.cos(m.pi * ix / a)) * m.e ** ((i_n - LvL) * ix) * (
                    1 + m.cos(m.pi * iy / b)) * m.e ** ((i_n - LvL) * iy)
        elif 2 * LvL + 1 <= i_n <= 3 * LvL:
            f = (1 + m.cos(m.pi * ix / a)) * m.e ** (-(i_n - 2 * LvL) * ix) * (
                    1 + m.cos(m.pi * iy / b)) * m.e ** (-(i_n - 2 * LvL) * iy)
        elif 3 * LvL + 1 <= i_n <= 4 * LvL:
            f = (1 + m.cos(m.pi * ix / a)) * m.e ** (-(i_n - 3 * LvL) * ix) * (
                    1 + m.cos(m.pi * iy / b)) * m.e ** (+(i_n - 3 * LvL) * iy)
        elif 4 * LvL + 1 <= i_n <= 5 * LvL:
            f = (1 + m.cos(m.pi * ix / a)) * m.e ** (+(i_n - 4 * LvL) * ix) * (
                    1 + m.cos(m.pi * iy / b)) * m.e ** (-(i_n - 4 * LvL) * iy)
        else:
            f = 0
            print("ERROR")
        return f

    def dxFi(i_n, ix, iy):
        dxf = (Fi(i_n, ix + dx, iy) - Fi(i_n, ix - dx, iy)) / (2 * dx)
        return dxf

    def dyFi(i_n, ix, iy):
        dyf = (Fi(i_n, ix, iy + dy) - Fi(i_n, ix, iy - dy)) / (2 * dy)
        return dyf

    def d2xFi(i_n, ix, iy):
        d2xf = (dxFi(i_n, ix + dx, iy) - dxFi(i_n, ix - dx, iy)) / (2 * dx)
        return d2xf

    def d2yFi(i_n, ix, iy):
        d2yf = (dyFi(i_n, ix, iy + dy) - dyFi(i_n, ix, iy - dy)) / (2 * dy)
        return d2yf

    def F(ik):
        p = 0
        for jj in range(0, M):
            y = -b + jj * dy
            for ii in range(0, N):
                x = -a + ii * dx
                p += Q(x, y) * Fi(ik, x, y) * dx * dy
        p = -p
        return p

    def R(ik, i_n):
        R_kn = 0
        for jj in range(0, M):
            y = -b + jj * dy
            for ii in range(0, N):
                x = -a + ii * dx
                R_kn += (d2xFi(i_n, x, y) + d2yFi(i_n, x, y)) * (d2xFi(ik, x, y) + d2yFi(ik, x, y)) * dx * dy
        R_kn = D * R_kn
        return R_kn

    Matrix = []
    for j in range(1, Num + 1):
        Matrix.append([])
        for i in range(1, Num + 1):
            Matrix[j - 1].append(R(j, i))

    V = []
    for j in range(1, Num + 1):
        V.append(F(j))

    Ms = numpy.array(Matrix)
    Vs = numpy.array(V)
    C = numpy.linalg.solve(Ms, Vs)
    return C
