import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import integrate

accfactor = 0.01

def accr(x):
    if x<0:
        return 0
    elif 0<=x<10:
        return x*accfactor
    elif 10<=x<30:
        return (10-(x-10))*accfactor
    elif 30<=x<40:
        return (-10+(x-30))*accfactor
    else:
        return 0

def main():
#---------------
    # x = [2*math.pi*i/50 for i in range(201)]
    # y1 = [math.sin(i) for i in x]
    # y = [integrate.quad(lambda t:integrate.quad(math.sin,0,t,args=())[0],0,i,args=())[0] for i in x]

    # xx = [xv for i,xv in enumerate(x) if i % 2 == 0]
    # yy = [yv for i,yv in enumerate(y) if i % 2 == 0]
    # plt.plot(xx,yy,x,y1)
#---------------
    x = [i for i in range(41)]
    ya = [accr(i) for i in range(41)] # accerelation
    yv = [integrate.quad(accr,0,i)[0] for i in range(41)] # velocity
    ys = [integrate.quad(lambda t:integrate.quad(accr,0,t)[0],0,i) for i in range(41)] # distance
    plt.plot(x,ya,x,yv,x,ys)
    plt.show()

    # for i in range(101):
    #     x= 2*math.pi*i/100
    #     print(i, x, math.cos(x))



if __name__ == '__main__':
    main()