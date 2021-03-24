import numpy as np 

def enterprise():

def funtion_g(x0):
    return np.array([2*x0[0], 50*x0[1]])


def funtion_x(x, alpha, g):
    return x - alpha * g  

def printf(vector):
    for i in range (len(vector)//2):
        if i == 1: continue
        print(f'='*40)
        print(f'valor de g = {vector[i]}')
        print(f'valor de x = {vector[i+1]}')

def steepest_descent():
    memory = []
    x0 = np.array([0.5, 0.5])
    alpha = 0.035
    k=funtion_g(x0)
    memory.append(k)
    for i in range(3):
        k=funtion_x(x0, alpha, k)
        memory.append(k)
        x0 = k
        k=funtion_g(k)
        memory.append(k)

        
    printf(memory)
    

def run():
    steepest_descent()


if __name__ == '__main__':
    run()



#                                 OUTPUT DEL ALGORITMO


# Para el punto 1 con un alpha igual a 0.01
# ========================================
# valor de g = [ 1. 25.]
# valor de x = [0.49 0.25]
# ========================================
# valor de g = [ 0.98 12.5 ]
# valor de x = [0.4802 0.125 ]

# Para el punto 2 con un alpha igual a 0.035
# ========================================
# valor de g = [ 1. 25.]
# valor de x = [ 0.465 -0.375]
# ========================================
# valor de g = [  0.93 -18.75]
# valor de x = [0.43245 0.28125]

# podemos ver que alfa es un  valor que in