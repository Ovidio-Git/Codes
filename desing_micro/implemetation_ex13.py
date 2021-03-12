from ejercicio13 import Astronaut

def action(resul):
	spacetravel = Astronaut(launching='m')
	if resul == 'l': 
		spacetravel.Launching_on()
	else:
		print("what up bro")

def menu(sms):

	while True:
		menu =  str(input(sms))
		action(menu)
		if menu == 'e':
			print("exittt maann")



def run ():

	
	sms='''
         welcome a this travel
         press  [l] for start launching

		'''
	menu(sms)






if __name__ == '__main__':
	run()
