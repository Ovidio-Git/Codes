
# Escriba un programa que cree dos archivos en formato txt: el primero
# debe imprimir los números enteros desde 0 hasta 100, el segundo debe
# imprimir los números enteros desde 50 hasta 200. Luego escriba otro
# programa que lea ambos archivos y genere un archivo nuevo que
# contenga sólo números pares organizados de mayor a menor, estos
# números no deben estar repetidos

# ESTE ES EL PROGRAMA QUE LEE LOS DOS ARCHIVOS

def run():

	#reading file 1
	with open('data1.txt', 'r') as file1:
		aux = file1.read().split()
		setdata = [int(aux[i]) for i in range(0,len(aux))] #convert to integer list

	#reading file 2
	with open('data2.txt', 'r') as file2:
		aux = file2.read().split()
		setdata2 = [int(aux[i]) for i in range(0,len(aux))] #convert to integer list



	

#	with open ( 'output.txt','r' ) as out:
#		for i in range (0,200):
#			if (set1[i]%2==0):
#				out.write(f'{set[i]}')

if __name__ == '__main__':
	run()
