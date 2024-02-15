from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from Data.base import db
@dataclass
class Carro(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    id_oficina:int = db.Column(db.Integer)
    id_cliente:int = db.Column(db.Integer)
    placa: str = db.Column(db.String(7))
    modelo:str = db.Column(db.String(50))
    marca:str = db.Column(db.String(50))
    cor:str = db.Column(db.String(50))
    ano_fabricacao:int = db.Column(db.Integer)
    ano_modelo:int = db.Column(db.Integer) 
    status:int = db.Column(db.Integer)
    observacao:str = db.Column(db.String(200))
    data_criacao:datetime = db.Column(db.DateTime, default=datetime.now)
    data_atualizacao:datetime = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class statusCarro(Enum):
    pendente = 0
    em_andamento = 1
    finalizado = 2
    cancelado = 3



   