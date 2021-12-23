from datetime import datetime
from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedido.db'
app.config['SECRET_KEY'] = 'Tonyhawks#1998'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    usuario = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))
    email = db.Column(db.String(50))
    date_create = db.Column(db.DateTime, default=datetime.now)
    pedidos = db.relationship('PedidoMac', backref='owned_user', lazy=True)

class PedidoMac(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    pedido = db.Column(db.String(50), unique=True)
    lanche = db.Column(db.String(50))
    tamanho = db.Column(db.String(50))
    date_create = db.Column(db.DateTime, default=datetime.now)
    owned = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
    def __repr__(self):
            return f'PedidoMac {self.lanche}'