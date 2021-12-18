from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect

from model import app, db, PedidoMac

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    '''if request.method == 'POST':
        lanche = request.form['lanche']
        tamanho = request.form['tamanho']
        return redirect(url_for('cadastrar', lanche=lanche, tamanho=tamanho))
    else:'''
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar(lanche, tamanho):
    pedidoM = PedidoMac(pedido=lanche, tamanho=tamanho)
    db.session.add(pedidoM)
    db.session.commit()
    return '<h1>Pedido realizado!</h1>'