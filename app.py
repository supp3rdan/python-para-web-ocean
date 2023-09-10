from flask import Flask

app = Flask("Meu app")

@app.route('/')
def hello():
    return "Hello World"

@app.route('/nova')
def nova():
    return "Nova pagina implementada"