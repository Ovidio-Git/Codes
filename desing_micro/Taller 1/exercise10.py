import numpy as np 

def funtion_g(x0):
    return np.array([2*x0[0], 50*x0[1]])


def funtion_x(x, alpha, g):
    return x - alpha * g  


def steepest_descent():
    memory = []
    x0 = np.array([0.5, 0.5])
    alpha = 0.01
    k=funtion_g(x0)
    memory.append(k)
    for i in range(3):
        k=funtion_x(x0, alpha, k)
        memory.append(k)
        x0 = k
        k=funtion_g(k)
        memory.append(k)
        
    print(memory)
    

def run():
    steepest_descent()


if __name__ == '__main__':
    run()