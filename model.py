from datetime import datetime
from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedido.db'
app.config['SECRET_KEY'] = 'Tonyhawks#1998'

db = SQLAlchemy(app)

class PedidoMac(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido = db.Column(db.String(50), unique=True)
    lanche = db.Column(db.String(50))
    tamanho = db.Column(db.String(50))
    date_create = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
            return f'PedidoMac {self.lanche}'
