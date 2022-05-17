#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 15:18:52 2022

@author: klarajons
"""
import random
import matplotlib.pyplot as plt
import math
import concurrent.futures as future
from time import perf_counter as pc

#DEL 1.1
def pi_approx(n):
    fig = plt.figure()#figsize =(10, 7))
    ax = fig.add_subplot()
    in_circle = 0
    x_red = []
    y_red = []
    x_blue = []
    y_blue =[]
    for i in range(n):
        punkt_x = random.uniform(-1,1)
        punkt_y = random.uniform(-1,1) #Skapa punkt
        if math.sqrt(punkt_x**2 + punkt_y**2) <= 1: #Punkt innuti cirkel 
            in_circle += 1
            x_red.append(punkt_x)
            y_red.append(punkt_y)
        else:
            x_blue.append(punkt_x)
            y_blue.append(punkt_y)
    print('antal punkter i cirkeln:',in_circle)
    pi = 4*in_circle/n
    plt.scatter(x_red,y_red,color = 'red')
    plt.scatter(x_blue,y_blue,color = 'blue')
    plt.title("Approximation av pi")
    plt.show()
    return pi
    
#print('approximerat pi:',pi_approx(100), 'teoretiskt värde:',math.pi)    
  
#DEL 1.2      
def vol_approx(n,d): 
    in_vol = 0
    for i in range(n):
        dim = [random.uniform(-1,1) for i in range(d+1)] # använda list comprehension
        if sum(map(lambda x: x*x,dim)) <= 1: # använda map & lambda
            in_vol += 1
    vol = (in_vol/n)*2**d #Hur räknar jag ut volymen?!
    v_teori = lambda d : math.pi**(d/2)/(math.gamma(d/2+1))
    print(f"Det teoretiska värdet på volymen för {d} dimmensioner: {v_teori(d)}")
    return vol

#vol_approx(100, 3)

#DEL 1.3
def main():

    start = pc()
    
    with future.ProcessPoolExecutor() as ex:
        inp = [10**6,11] 
        for i in range(10):
            ex.map(vol_approx, inp)

    end = pc() 
    print(f"Processen tog {round(end-start, 2)} sekunder")
    
start = pc()
vol_approx(10**7,11)
end = pc() 

if __name__ == "__main__":
    main()
    print(f"Processen för del 1.2 tog {round(end-start, 2)} sekuder")