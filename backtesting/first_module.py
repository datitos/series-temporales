"""
first_module.py
====================================
The core module of this incredible, never seen before package.
"""


import numpy as np
import matplotlib.pyplot as plt

def sum(a, b):
    '''
    Returns the sum between "a" and "b"
    
    Args:
        a (float) : First number
        b (float) : Second number

    Returns:
        sum (float) : a and b sum
    '''
    return a + b

def matmul(a, b):
    '''
    Returns the matrix multiplication between "a" and "b"
    
    Args:
        a (np.array) : First matrix
        b (np.array) : Second matrix

    Returns:
        matmul (np.array) : a and b matmul
    '''
    return np.matmul(a, b).tolist()

def substract(a,b):
    '''
    Returns the substraction between "a" and "b"
    
    Args:
        a (float) : First number
        b (float) : Second number

    Returns:
        sub (float) : a and b substraction
    '''
    return a - b

def hi():
    '''
    Returns hello

    Returns:
        hello (string) : hello
    '''
    return 'Hello'

def randomwalk(length):
    '''
    Returns a random walk of length = length
    
    Args:
        length (int) : random walk length
        
    Returns:
        rw (np.array) : array with a random walk
    '''
    pasos=np.random.randint (-1,2,length)
    return pasos.cumsum()

def maximo(list):
    '''
    Returns the max value in a list
    
    Args:
        list (list) : list with a max to look for
        
    Returns:
        max (int/float) : max value found in list
    '''
    max_val = float('-inf') 
    for c in list:
        if c > max_val:
             max_val = c
    return max_val




def plot_random_walks():
    ''''
    Simulate 12 random walks, plot them.
    
    Returns:
        plot (plt.figure) : plot
    '''
    N = 100000
    random_walks = []

    plt.figure(figsize = (15,7))

    #Genera y grafica 12 random walks en el primer subplot
    f = plt.subplot(2, 1, 1)
    for i in range(12):
        random_walks.append(randomwalk(N))
        plt.plot(random_walks[i])
        plt.title('12 caminatas al azar')

    plt.xticks([])
    #Recupero los limites del primer subplot
    #asi los uso en los siguientes dos subplots
    ymin, ymax = f.get_ylim()

    #Busco los RW que mas y menos se alejan
    dic = {i:np.sum(abs(rw)) for i,rw in enumerate(random_walks)}
    menos_se_aleja = min(dic, key = dic.get)
    mas_se_aleja = max(dic, key = dic.get)

    #Plot del que menos se aleja
    plt.subplot(2, 2, 3)
    plt.plot(random_walks[menos_se_aleja])
    plt.ylim([ymin, ymax ])
    plt.xticks([])
    plt.title('Caminata que menos se aleja')

    #Plot del que mas se aleja
    plt.subplot(2, 2, 4)
    plt.plot(random_walks[mas_se_aleja])
    plt.ylim([ymin, ymax ])
    plt.xticks([])
    plt.title('Caminata que mas se aleja')

    plt.show()

