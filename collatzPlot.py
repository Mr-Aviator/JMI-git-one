import numpy as np
import matplotlib.pyplot as plt


def collatzPlot(top):
    top = int(top)
    counter = np.zeros(top, dtype = int)
    number = list(range(1,top+1))
    for i in range(top):
        while number[i] != 1:
            if number[i] % 2 == 0:
                number[i] = number[i] / 2 
                counter[i] += 1
            else:
                number[i] = 3 * number[i] + 1
                counter[i] += 1
    plt.plot(counter)
    #plt.ylabel(list(range(1,top+1)))
    return(plt.show())
