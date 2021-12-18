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
    pedidoM = PedidoMac(pedido=lanche, tamanho=tamanho)
    try:
        db.session.add(pedidoM)
        db.session.commit()
        id = db.session.query(PedidoMac).order_by(PedidoMac.id.desc()).first()
        return render_template('index.html', lanche=lanche, tamanho=tamanho, id=id, erro=0)
    except:
        return render_template('index.html', erro=1)
    