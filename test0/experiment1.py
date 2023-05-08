import random
import math
import numpy as np
import matplotlib.pyplot as plt
def PfromC(C):
    pProcOnN = np.float64(0.0)
    pProcByN = np.float64(0.0)#第一次成功+第二次成功+...+第n此成功的概率
    E_N = np.float64(0.0)

    maxFails = int(math.ceil(1.0 / C))

    for N in range(1, maxFails + 1):
        pProcOnN = min(1.0, N * C) * (1.0 - pProcByN)
        pProcByN += pProcOnN
        E_N += N * pProcOnN

    return 1.0 / E_N

def CfromP(p):
    if not isinstance(p, float):
        p = float(p)  # double precision

    Cupper = p
    Clower = np.float64(0.0)
    Cmid = np.float64(0.0)
    p2 = np.float64(1.0)

    while (True):
        Cmid = (Cupper + Clower) / 2.0
        p1 = PfromC(Cmid)

        if math.fabs(p1 - p2) <= 0:
            break

        if p1 > p:
            Cupper = Cmid
        else:
            Clower = Cmid

        p2 = p1

    return Cmid


def testPfromC(C, iterations):

    nsum = 0

    for i in range(iterations):
        n = 1

        while (C * n) < 1.0 and random.random() > (C * n):
            n += 1

        nsum += n

    av_iters = float(nsum) / iterations
    return 100.0 / av_iters


if __name__ == "__main__":
    iterations = 100000
    x=[]
    print(x)
    y1=x
    y2=[]

    for i in range(1, 100):
        p = i / 100.0
        x.append(p)
        C = CfromP(p)
        y2.append(C)
        print("%.2f\t%f\t%f" % (p, C, testPfromC(C, iterations)))
    # fig, ax = plt.subplots()
    # ax.plot(x,y1,color='blue',lable='line')
    # ax.plot(x,y2,color='blue',lable='scatter')
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    plt.scatter(x,y2)
    plt.plot(x,y1)

    # 显示图形
    plt.show()