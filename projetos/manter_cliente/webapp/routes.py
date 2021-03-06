from flask import (
    Flask, render_template, request, redirect
)
from manter.database import Database
from manter.entities import Cliente
from manter.dao import DaoCliente
# importando a variavel app do __init__.py
from . import app
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cliente/add")
def cliente_add():
    return render_template('cadastro_cliente.html', cliente=None)

@app.route("/cliente/edit/<id>")
def cliente_edit(id):
    # buscar na dao o cliente
    # find_by_id(id) - recupera 1 cliente
    dao = DaoCliente()
    cliente = dao.find_by_id(id)
    return render_template(
        'cadastro_cliente.html',
        cliente=cliente
    )

@app.route("/save", methods=["POST"])
def save():
    # recebe os campos do formulario
    # criar o objeto cliente
    # chamar a dao que salva no banco de dados
    id = request.form.get("id")
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    cliente = Cliente(nome, cpf, email)
    dao = DaoCliente()
    if id:
        cliente.id = id
        dao.update(cliente)
    else:
        dao.save(cliente)
    return findall()

@app.route("/delete/<id>")
def delete(id):
    dao = DaoCliente()
    dao.delete(id)
    # return findall()
    return redirect("/cliente/findall/")

@app.route('/restore')
def restore():
    Database.create_db()
    return redirect("/cliente/findall")

@app.route("/update")
def update():
    # alem dos atributos eh necessario o ID
    # cliente = Database.find(id)
    # atualiza os campos...
    # Database.update(cliente)
    return "manter.html"

@app.route("/cliente/findall/")
def findall():
    dao = DaoCliente()
    clientes = dao.findall()
    return render_template("manter.html", clientes=clientes)
