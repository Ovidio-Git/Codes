from flask import Flask

# Creamos una nueva instancia llamada app
app = Flask(__name__)


# Cuando el browser realice una peticion al 
# servidor este va a ir a la ruta raiz 
# lo que este devoldera sera la funcion hello
# que se encuentra en esta ruta especifica

@app.route('/')
def hello():
	return "Hello world, i launching a web page"

if __name__ == '__main__':
	app.run()

