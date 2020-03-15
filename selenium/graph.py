import numpy as np
import matplotlib.pyplot as plt

def graph(infection, active_case, deaths, recovered ):
    x = np.linspace(0,20,2)
    y1 = [0,infection]
    y2 = [0,active_case]
    y3 = [0,deaths]
    y4 = [0,recovered]

    # COVID INDONESIA
    ax = plt.gca()
    # for data in range(data1):
    #     ax.scatter(x=[data,data], y=[data,data], label='Data')
    plt.plot(x, y1, "-b", label='infection')
    plt.plot(x, y2, "-r", label='active case')
    plt.plot(x, y3, "-y", label='deaths')
    plt.plot(x, y4, "-g", label='recovered')
    plt.legend(loc="best")
    # plt.ylim(-1.5, 2.0)
    ax.set_xlabel("")
    ax.set_ylabel("Jumlah")
    plt.title("COVID - INDONESIA")
    plt.show()

    print("debug")