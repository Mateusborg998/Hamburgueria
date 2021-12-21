from os import urandom
import re
from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

from model import app, db, PedidoMac

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    lanche = request.form.get('lanche')
    tamanho = request.form.get('tamanho')
    try:
        # Modelo para gerar o nº do pedido através do ID foi desativado - 19/12/21 by Mateus
        '''pedido = str(db.session.query(PedidoMac.id).order_by(PedidoMac.id.desc()).first())
        pedido = pedido[1:pedido.rfind(',')]
        pedido = int(pedido) + 1'''
        pedido = str(urandom(6).hex())
        pedidoM = PedidoMac(pedido=pedido, lanche=lanche, tamanho=tamanho)
        db.session.add(pedidoM)
        db.session.commit()
        return render_template('index.html', lanche=lanche, tamanho=tamanho, pedido=pedido, erro=0)
    except:
        return render_template('index.html', erro=1)

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    id = request.form.get('palavra')
    try:
        # Pesquisa retornando para o index.html foi desativado - 20/12/21 by Mateus
        '''pedido = str(db.session.query(PedidoMac.pedido).filter_by(pedido=id).first())
        lanche = str(db.session.query(PedidoMac.lanche).filter_by(pedido=id).first())
        tamanho = str(db.session.query(PedidoMac.tamanho).filter_by(pedido=id).first())
        return render_template('index.html', pedido=pedido[2:pedido.rfind("'")], lanche=lanche[2:lanche.rfind("'")], tamanho=tamanho[2:tamanho.rfind("'")])'''
        pedidos = db.session.query(PedidoMac).filter_by(pedido=id).all()
        return render_template('lista.html', pedidos=pedidos)
    except:
        return render_template('index.html', erro=2)

@app.route('/listar', methods=['GET'])
def listar():
    try:
        pedidos = db.session.query(PedidoMac).all()
        return render_template('lista.html', pedidos=pedidos)
    except:
        return render_template('lista.html', erro=2)

