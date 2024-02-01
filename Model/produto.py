from dataclasses import dataclass
from datetime import datetime
from typing import Any
from Data.base import db

@dataclass
class Produto(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    id_oficina: int = db.Column(db.Integer)
    id_fornecedor: int = db.Column(db.Integer)
    codigo: int = db.Column(db.Integer)
    descricao: str = db.Column(db.String(50))
    preco: float = db.Column(db.Float)
    preco_custo: float = db.Column(db.Float)
    estoque: int = db.Column(db.Integer)
    tipo: int = db.Column(db.Integer)
    data_criacao: datetime = db.Column(db.DateTime)
    data_atualizacao: datetime = db.Column(db.DateTime)

  