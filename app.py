from flask import Flask, render_template, request, redirect, session, jsonify, flash
from model.comidas import mostrar_comidas, rec_destaque
from model.usuario import Usuario
from model.carrinho import recuperar_carrinho

app = Flask(__name__)
app.secret_key = "webservice_lanches"

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

@app.route("/login")
def login():
    return render_template("login.html")

@app.get("/cadastro_login")
def cadastro_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    resultado = Usuario.logar(usuario, senha)
    if not resultado:
        session["usuario_logado"] = resultado
        return redirect("/cadastro")
    else:
        return("/")
    
@app.route("/login/post", methods=["POST"])
def logar():
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    user = Usuario.logar(nome, senha)
    if user:
        session["usuario_logado"] = user
        return redirect("/")
    else:
        flash("Usuário ou senha inválidos!", "erro")
        flash("Tente novamente ou cadastre-se", "erro")
        return redirect("/login")

@app.route("/api/get/carinho", methods = ["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
        login = session["usuario_logado"]["usuario"]
        carrinho = recuperar_carrinho(login)
        return jsonify(carrinho), 200
    else:
        return jsonify(("message","Usuário não logado")), 401
app.run(debug=True)
