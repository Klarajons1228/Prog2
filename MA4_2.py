#!/usr/bin/env python3.9

from person import Person
import time
import matplotlib.pyplot as plt
from numba import njit

def main():
    f = Person(5)
    print(f.get())
    f.set(7)
    print(f.get())

if __name__ == '__main__':
    main()


def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
 
def time_fib_py(n):
    start = time.time()
    fib_py(n)
    end = time.time()
    return end - start

@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return(fib_numba(n-1) + fib_numba(n-2))

def time_fib_numba(n):
    fib_numba(n)
    start = time.time()
    fib_numba(n)
    end = time.time()
    return end - start

def time_fib_c(n):
    start = time.time()
    f=Person(n)
    f.fib()
    end = time.time()
    
def plott():
    fig = plt.figure()#figsize =(10, 7))
    ax = fig.add_subplot()
    fib_numba = []
    fib_py=[]
    fib_c=[]
    #numb = [20,21,22,23,24,25,26,27,28,29,30]
    numb = [30,31,32,33,34,35,36,37,38,39,50,41,42,43,44,45]
    for n in numb:
        fib_numba.append(time_fib_numba(n))
        fib_py.append(time_fib_py(n))
        fib_c.append(time_fib_c(n))
    
    plt.scatter(numb,fib_numba,color = 'blue',label='numba')
    plt.scatter(numb,fib_py,color='red',label='python')
    #plt.scatter(numb,fib_c,color='green',label='c++')
    plt.legend()
    plt.title("Tidtagning för fibonacci med olika typer av språk")
    plt.show()
    
plott()

print("time for numba; n=47 ",time_fib_numba(47))

print("time for c++; n=47",time_fib_c(47) )