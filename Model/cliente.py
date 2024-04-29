from dataclasses import dataclass
from datetime import datetime
from typing import List
from Data.base import db

@dataclass
class Cliente(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    id_oficina: int = db.Column(db.Integer)
    nome: str = db.Column(db.String(50))
    cpf_cnpj: str = db.Column(db.String(11))
    fone: str = db.Column(db.String(11))
    logradouro: str = db.Column(db.String(50))
    cep: str = db.Column(db.String(8))
    numero: str = db.Column(db.String(5))
    bairro: str = db.Column(db.String(50))
    cidade: str = db.Column(db.String(50))
    uf: str = db.Column(db.String(2))
    complemento: str = db.Column(db.String(50))
    observacao: str = db.Column(db.String(200))
    data_criacao:datetime = db.Column(db.DateTime, default=datetime.now)
    data_atualizacao:datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    status: int = db.Column(db.Integer, default=1)
    
