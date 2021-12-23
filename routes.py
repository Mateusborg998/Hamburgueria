from os import urandom
import re
from flask import Flask, render_template, request

from model import app, db, PedidoMac

@app.route('/', methods=['POST', 'GET'])
def login():
    return render_template('login.html', off=1)

@app.route('/registrar', methods=['POST', 'GET'])
def registrar():
    return render_template('registrar.html', off=1)

@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    lanche = request.form.get('lanche')
    tamanho = request.form.get('tamanho')
    try:
        pedido = str(urandom(6).hex())
        pedidoM = PedidoMac(pedido=pedido, lanche=lanche, tamanho=tamanho)
        db.session.add(pedidoM)
        db.session.commit()
        return render_template('index.html', lanche=lanche, tamanho=tamanho, pedido=pedido, erro=0)
    except:
        return render_template('index.html', erro=1)

@app.route('/pesquisar', methods=['POST', 'GET'])
def pesquisar():
    id = request.form.get('palavra')
    try:
        pedidos = db.session.query(PedidoMac).filter_by(pedido=id).all()
        return render_template('lista.html', pedidos=pedidos)
    except:
        return render_template('index.html', erro=2)

@app.route('/listar', methods=['GET', 'POST'])
def listar():
    try:
        pedidos = db.session.query(PedidoMac).all()
        return render_template('lista.html', pedidos=pedidos)
    except:
        return render_template('lista.html', erro=2)

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    id = request.form.get('id')
    pedido = request.form.get('pedido')
    botaoExcluir = request.form.get('excluir')
    botaoEditar = request.form.get('editar')
    lanche = request.form.get('lanche')
    tamanho = request.form.get('tamanho')

    if botaoEditar == 'editar' and botaoExcluir != 'excluir':
        try:
            pedido = db.session.query(PedidoMac).filter_by(id=id).first()
            pedido.lanche = lanche
            pedido.tamanho = tamanho
            db.session.commit()
            pedidos = db.session.query(PedidoMac).all()
            return render_template('lista.html', pedidos=pedidos, msg=1)
        except:
            pedidos = db.session.query(PedidoMac).all()
            return render_template('lista.html', pedidos=pedidos, erro=1)   
    else:
        try:
            pedido = db.session.query(PedidoMac).filter_by(id=id).first()
            db.session.delete(pedido)
            db.session.commit()
            pedidos = db.session.query(PedidoMac).all()
            return render_template('lista.html', pedidos=pedidos, msg=2)
        except:
            pedidos = db.session.query(PedidoMac).all()
            return render_template('lista.html', pedidos=pedidos, erro=2)
