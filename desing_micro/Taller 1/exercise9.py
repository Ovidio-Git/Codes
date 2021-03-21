
def vector ():
    n = int(input('Ingrese el tamaño del vector a digitar: '))
    memory = []
    for i in range(n):
        aux = int(input(f'Ingrese el dato numero {i+1} en su vector: '))
        memory.append(aux)
    return memory


def run ():
    print(vector())


if __name__ == '__main__':
    run()