from flask import Flask, render_template
from model.comidas import mostrar_comidas

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    comidas = mostrar_comidas()
    return render_template("index.html", exibir_comidas=comidas)

@app.route("/produto")
def segunda_pagina():
    return render_template("produto.html")

if __name__=="__main__":
    app.run(debug=True)     