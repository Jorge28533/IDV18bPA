


'''
def lista():
	x = int(input("Escoje un numero:  "))
	lista = [8, 3, 6, 5, 1, 10]
	m =	lista > x
	print(m)
'''
def Junta():
	myList = [3, 7, 5, 3, 45, 32, 2, 1, 87, 9, 3, 5,78]
	Lista = [3, 7, 5, 3, 6, 4, 3]
	print(myList)
	print(Lista)
	myList.extend(Lista)
	myList = list(set(myList)) 
	print("Lista Conbinada = ")
	print(myList)


def Devuelve():
	La = ["gato","perro","pajaro","lajartija"]
	print(La)
	z = La.pop()
	#print(z)
	m = La.pop()
	#print(m)
	t = La.pop()
	#print(t)
	y = La.pop()
	#print(y)
	lista3 = [z, m, t, y]
	print(lista3)
	
#numx = int(input("Escoje un numero:  "))s

def main():
	print("1.Lista, 2.Junta, 3.Devuelve:  ")
	print("Nota :  1.Lista todavia no terminada")

	numero = int(input("Escoje una Funcion:  "))

	if(numero == 1):
		lista()	
	
	if(numero == 2):
		Junta()

	if(numero == 3):
		Devuelve()

'''
def lista():
	x = int(input("Escoje un numero:  "))
	lista = [8, 3, 6, 5, 1, 10]
	m =	lista > x
	print(m)

#numx = int(input("Escoje un numero:  "))
'''

if __name__ == '__main__':
	main()