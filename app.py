from flask import Flask, render_template, request, redirect
from model.comidas import mostrar_comidas, rec_destaque
from model.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    comidas = mostrar_comidas()
    destaque = rec_destaque()
    return render_template("index.html", exibir_comidas=comidas, recuperar_destaque=destaque)

@app.route("/produto")
def segunda_pagina():
    return render_template("produto.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usuario = Usuario(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")

app.run(debug=True)