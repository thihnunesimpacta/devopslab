from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Message Custom. Realizando o Desafio CUSTOMIZAR A MENSAGEM do app PYTHON"